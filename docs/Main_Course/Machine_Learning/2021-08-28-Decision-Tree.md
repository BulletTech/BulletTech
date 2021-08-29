---
template: overrides/blogs.html
---

# 决策树学习笔记

!!! info
    作者：袁子弹起飞，发布于2021-08-28，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

决策树是非常经典的机器学习模型，日常工作中许多分类会回归问题都可以用决策树解决，很多更高级、先进的机器学习模型也基于决策树构建，为了夯实基础、正确运用决策树，今天我们来回顾一些决策树里最重要的技术细节。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-28/1630120948129-iris_tree.png"  />
  <figcaption>鸢尾花品种分类决策树示例</figcaption>
</figure>


## 2 算法重要细节

### 2.1 如何做预测

示例中深度为2的决策树的展示了做决策的过程和结论，对于150个样本点，在根节点上，决策树以花瓣长度（petal length）是否小于2.45厘米将数据分成两部分，花瓣长度小于2.45厘米的样本被分类成setosa，大于2.45厘米的数据继续以花瓣宽度（petal width）是否小于1.75厘米进行分类，小于的部分被认为是versicolor，大于的部分则是virginica。

图中的samples即为这个大类中的样本数量，如深度为1的左侧叶子节点中samples=50意味着花瓣长度（petal length）小于2.45厘米的样本有50个。而value则代表当前节点中训练数据的分布，如深度为2的左侧绿色节点中[0, 49, 5]表示这个节点中，有0个setosa，49个versicolor和5个virginica，总共54个samples。

### 2.2 预测的依据

在示例的决策树中，还要一个重要的指标叫做`gini - 基尼系数`，这个系数能衡量当前节点的不纯净度（impurity），直观来说，当一个节点里的所有样本都属于同一类时，节点的纯净度最高，基尼系数为0。基尼系数的定义为

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-28/1630138292390-gini.png"  />
  <figcaption>Gini</figcaption>
</figure>

其中$P~i,k~$是在i个节点中k类的样本占总体样本的比例。比如示例中深度为2的右侧节点的gini系数为$1-(0/46)^2^-(1/46)^2^-(45/46)^2^ ~= 0.043$。以最常用的Python机器学习库`Scikit-Learn`中的`DecisionTreeClassifier`类为例，起在实现分类和回归树（Classification and Regression Tree, CART）时，在选择分裂节点的过程中，决策树选择分裂节点和阈值的依据即与gini有关。其优化目标（损失函数）如下所示：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630206173092-CART_Loss.png"  />
  <figcaption>CART Loss</figcaption>
</figure>

其中$G~left/right~$分别为左侧和右侧节点的gini系数，而$m~left/right~$分别为左侧和右侧节点的样本数量。CART算法会做贪心搜索（greedy search），从根节点开始分裂，并在层层子节点中搜索能够有效减少gini的特征和阈值，直到分裂的层数到达最大深度（由max_depth参数定义）或已经找不到能够减少gini的节点。直观来说，找到最好的树是一个NP-complete问题，因此算法最终只会找到一个相对好的方案，而非最好的解决方案。

除了gini之外，熵（Entropy）也可以用来衡量分裂节点的效果，用以衡量混乱度，在决策树的节点中，当一个节点里的样本都属于同一类时，熵的值为0。其定义如下：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630205324586-Entropy.png"  />
  <figcaption>熵（Entropy）</figcaption>
</figure>

其中$P~i,k~$是在i个节点中k类的样本占总体样本的比例。比如示例中深度为2的右侧节点的熵为$-(1/46)log~2~(1/46)-(45/46)log~2~(45/46)~= 0.151$。在`Scikit-Learn`中使用`DecisionTreeClassifier`类时，可以通过设置`criterion`参数为`entropy`来使用熵作为衡量指标。但通常使用`gini`和`entropy`差别不大。主要的区别在于`gini`计算更快，并且使用`gini`会让树将样本划分得更加集中在特定节点，而使用`entropy`会让样本在树的分布更加均衡。

