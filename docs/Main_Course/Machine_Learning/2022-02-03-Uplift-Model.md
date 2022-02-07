---
template: overrides/blogs.html
---

# 因果推断 Uplift Model

!!! info
    作者：Echo，发布于2022-02-03，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()


## 1 背景介绍

春节宅家期间，跟小伙伴线上交（ma)流（jiang）的时候发现我们被同一个游戏广告刷屏了（毕竟欢乐的方式有很多，然而欢乐豆的获取方式着实单一）。在被动反复观看了很多个30秒之后，小伙伴成为了它的用户。而我被它的营销成本打动了，决定来研究一下背后的营销策略。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/chat2223.jpg" width="500"/>
</figure>

开始之前让我们复习一下用户的四个象限。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/用户四象限.png" width="500"/>
</figure>

横纵坐标分别是用户在有无干预情况下的购买情况，干预以发放优惠券为例。
- Persuadables：干预敏感型用户，只有发优惠券才会购买，不发则不买。
- Sure things：自然转化型用户，不管发不发，都会购买。
- Lost causes：心如磐石型用户，不管发不发都不买。
- Sleeping dogs：南辕北辙型用户，不发优惠券会买，发了反而不买。

生产环境中，发放优惠券的目的是为了提高最终的转化率。常用的响应模型（Response Model）一般以是否购买商品为因变量进行建模，来预测发放优惠券后用户购买的概率。但这个模型侧重相关性，只看自变量是否和因变量相关，无法区分用户的购买行为是否是由发放优惠券导致，识别不出自然转换人群，因此也无法识别优惠券的效用。考虑到营销是需要成本的，干预敏感型用户才能反映出营销活动的作用，所以更有效的估计是针对某种treatment（干预）对个体行为（如购买）的**因果效应**（如带来的增量）进行建模，即增量模型（Uplift Model）。根据图灵奖得主Judea Pearl指出的因果关系三层级，可知这是一个反事实因果推断。感兴趣的小伙伴可以移步《The Book of Why: The New Science of Cause and Effect》追根溯源。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/因果推断.png" width="500"/>
</figure>


## 2 理论依据

定义X为用户特征（如性别，年龄，收入等），T代表treatment（有无干预，1为有，0为无），Y表示因变量结果（如点击率/转化率等）。Uplift Model旨在预测ITE（Individual Treatment Effect），$\tau_{i}=Y_{i}(1)-Y_{i}(0)$ 可以表示为用户在有无干预时的转化概率之差，也就是独立样本的treated和control的潜在结果的差值。Uplift Model的目标为最大化$\tau_{i}$。考虑到不可能对同一个用户既知道发优惠券的结果又知道不发优惠券的结果（这就是反事实之处），模型因此强依赖于条件独立假设CIA(Conditional Independent Assumption)，即要求用户特征和干预策略相互独立。

$$
\left\{Y_{i}(1), Y_{i}(0)\right\} \perp T_{i} \mid X_{i}
$$

实际应用中可以通过A/B test随机试验得到使用干预策略和不干预策略的两组样本，且两组样本的特征分布一致。只有在CIA假设下，用所有样本的因果效应的期望的估计值来代表总体用户才是无偏的，可得条件平均干预效应 CATE(Conditional Average Treatment Effect)为

$$
\tau\left(X_{i}\right)=E\left[Y_{i}(1) \mid X_{i}\right]-E\left[Y_{i}(0) \mid X_{i}\right]=E\left[Y_{i}^{o b s} \mid X_{i}=x, T=1\right]-E\left[Y_{i}^{o b s} \mid X_{i}=x, T=0\right]
$$

其中 $Y_{i}^{o b s}=T_{i} Y_{i}(1)+\left(1-T_{i}\right) Y_{i}(0)$.

## 3 模型

### 3.1 改造树模型

传统树模型的分裂规则为信息增益。目标是最大化分裂前后的信息差异，希望特征分裂之后下游节点的**正负样本分布**更加悬殊。在Uplift model中类似，每个节点内都观察实验组和对照组的因变量的分布，目的是希望特征分裂之后可以把uplift更高和更低的人群区分开来，也就是分裂后，相比于上游节点，下游节点的**实验组和对照组间的正负样本分布差异**更大。通常可以用距离来衡量这种差异，如KL散度（KL divergence）、欧氏距离、卡方距离等等。这个方法优点是直接对增量建模，更精准。缺点是模型改造成本较高。

### 3.2 差分响应模型

- Two model approach
分别对A/B test的实验组和对照组独立建模，得到用户行为概率，两模型的概率期望相减即为uplift score。在预测时用两模型分别对同一用户预测，两预测值相减即为预测的因果效应。优点是简单，且可套用现有的分类模型。缺点也很明显，照猫画虎，本质上还是用响应模型来模拟增量模型，容易累计误差。

- One model approach
合并实验组和对照组，将Treatment作为分类变量加入用户特征中，因此只需要对所有样本建一个模型。优点是避免误差累计，可套用现有模型。缺点是本质上依然是响应模型，而且，训练数据打通之后，很难说X和T还是不是满足条件独立假设…

### 3.3 模型评估

考虑到增量模型的反事实之处，我们无法通过测试集的混淆矩阵来计算准确率，召回率，AUC等等指标。但在满足CIA假定的前提下，所有样本特征同分布，我们可以对实验组和对照组样本分别预估uplift score，降序排列，分别截取十分位数（decile），计算该区间内两组样本转化率的差异，来代表这个区间的uplift，从而能对齐实验组和对照组数据，实现间接评估。对uplift绘制累计直方图，则可得到Gini曲线等来衡量不同uplift model的好坏。

## 3 示例代码

Python有pylift包可供使用，也有详尽的[官方文档](https://pylift.readthedocs.io/en/latest/quick-start.html '官方文档')可供参考。示例代码如下。

```python
import numpy as np
import pandas as pd
#模拟数据集
df = {'X1':list(np.random.normal(10,5,100)),
      'X2':list(np.random.normal(11,5,100)),
      'X3':list(np.random.normal(20,5,100)),
      'Treatment':list(np.random.randint(0,2,100)), #实验组1/对照组0
      'Converted':list(np.random.randint(0,2,100))} #随机生成的0-1因变量
df = pd.DataFrame(df)
df.head()

#以下为官方示例代码
from pylift import TransformedOutcome
up = TransformedOutcome(df1, col_treatment='Treatment', col_outcome='Converted')

up.randomized_search()
up.fit(**up.rand_search_.best_params_)

up.plot(plot_type='aqini', show_theoretical_max=True)
print(up.test_results_.Q_aqini)

```

输出结果如下，我随机生成的数据集过于随机……所以图看起来奇奇怪怪。通常应该斜率为正，建议大家搞点真实数据来试试。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/output_upliftmodel.png" width="500"/>
</figure>

在模型评估上pylift提供了6种图，简介如下。具体可参考官方文档。
<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/uplift_model_evaluation.png" width="500"/>
</figure>


## 4 总结

uplift model侧重因果关系而不是相关关系。因此建模和评估上与传统响应模型略有不同。本质上还是反事实因果推断及条件概率。值得强调的是，uplift model依赖于CIA假设，对数据要求很高，实际应用时需要注意样本的选取。

以上，希望这次的分享对你有帮助，欢迎在评论区留言讨论。下次见朋友们~

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
