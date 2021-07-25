---
template: overrides/blogs.html
---

# 读《Rules of Machine Learning》有感（下）

!!! info 
    作者：Void，发布于2021-07-22，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/XwtXpa1hOKrN6fIC-zpyKw)

## 1 引言

这篇是[《Rules of Machine Learning》](http://martin.zinkevich.org/rules_of_ml/) 读后感的下篇。主要涉及了具体建模的部分，包括特征工程，分析及优化。

## 2 特征工程

当阶段一的系统搭建完毕后，阶段二要做的是加入尽可能多的有效特征。此时，模型表现的提升是相对容易的。

```
Rule #16: Plan to launch and iterate.
```

做好持续迭代的准备。

```
Rule #17: Start with directly observed and reported features as opposed to learned features.
```

从简单、直观的特征出发。所谓learned features可以是别的模型的打分等。加入此类特征会增加依赖性，如某天某个模型retire了，这个特征就用不了了。  
然而，这里并不是说完全不能使用此类特征。

```
Rule #18: Explore with features of content that generalize across contexts.
```

使用跨场景的特征。比如客户在A产品上的数据有利于对B产品建模。同时，这也可以处理冷启动问题。

```
Rule #19: Use very specific features when you can.
```

如果数据量够大，使用尽可能多的简单特征而不是少数复杂特征。不要害怕使用id类非常稀疏的特征。

```
Rule #20: Combine and modify existing features to create new features in human-understandable ways.
```

特征工程要有一定的含义。对连续特征离散化或者类别特征的交叉要有一定的业务含义，不能乱交叉。  
特征组合可以试试Shap。Shap可以给出特征交互对label的影响，可以指导特征组合。

```
Rule #21: The number of feature weights you can learn in a linear model is roughly proportional to the amount of data you have.
```

特征数量要和样本数量匹配(有统计理论支撑)。  

- 千级数据对应几十个特征
- 千万级的数据对应十万级的特征

看上去是差两个数量级。

```
Rule #22: Clean up features you are no longer using.
```

去除无用的特征。如无必要，勿增实体，这也符合奥卡姆剃刀原理。剔除此类特征不仅可以使模型更clean，甚至可以提升模型表现。  
另外，覆盖率太低的特征不一定不能用。如某特征覆盖率只有1%，但是这1%都是正样本，那么这也是一个非常有效的特征。

## 3 人为分析机器学习系统

```
Rule #23: You are not a typical end user.
```

不识庐山真面目，只缘生在此山中。作为模型的开发者，你不是一个真正客观的终端用户。可以让真正的终端用户或者其他同事检查模型表现。

```
Rule #24: Measure the delta between models.
```

比较新老模型的表现。通常来说，我们要求新模型的表现会优于老模型。检查表现差异，可以给你一些模型在哪些方面做出改变的insights。

```
Rule #25: When choosing models, utilitarian performance trumps predictive power.
```

选择模型时，实用性指标的好坏比预测能力更重要。比如我们用模型分数的cutoff去拒绝坏的交易时，排序的准确性比预测值本身更为重要。很多时候这两者是一致的。但是我们也可以基于我们实用的具体需求，调整模型，比如给分数更高(排序更前)的样本更大的权重。

```
Rule #26: Look for patterns in the measured errors, and create new features.
```

通过case study去构造新的特征。  
可以构造多个同类的特征，然后让模型去选择有效的特征。

```
Rule #27: Try to quantify observed undesirable behavior.
```

将观察到的负面现象量化。比如你觉得模型排序准确率不够，那么如何定义排序准确率呢？只有给出明确的量化指标，才能对此进一步优化。

```
Rule #28: Be aware that identical short-term behavior does not imply identical long-term behavior.
```

模型测试的效果不等于长期的泛化能力。模型是否真正学到了pattern，还是只是过拟合了样本，这是一个令人头大的问题。

## 4 训练与上线的差异

训练和上线之间往往会存在差异。最好或者说为数不多的办法是做好监控。

```
Rule #29: The best way to make sure that you train like you serve is to save the set of features used at serving time, and then pipe those features to a log to use them at training time.
```

最好的方法是将真实线上的数据log下来作为训练数据。这可以大大减少两者之间的差异性。

```
Rule #30: Importance weight sampled data, don’t arbitrarily drop it!
```

不要随意丢弃采样样本。同时，对采样概率为30%的样本，训练时要给10/3的权重。这种校准对基于预测值的模型很重要，对基于排序的模型影响不大。

```
Rule #31: Beware that if you join data from a table at training and serving time, the data in the table may change.
```

上线时，数据可能相较训练时已经发生了变化。特别是一些字典类的特征，比如每个id对应的历史坏样本率等等。此类数据应该会有及时的更新。

```
Rule #32: Re-use code between your training pipeline and your serving pipeline whenever possible.
```

尽量复用训练和上线时的代码。这里主要说的是上线会用一些流式数据。工程方面，会有对基于这些数据的特征的支持。有了特征只需要丢到已经训练好的模型中即可。

```
Rule #33: If you produce a model based on the data until January 5th, test the model on the data from January 6th and after.
```

测试数据要在训练数据之后。

```
Rule #34: In binary classification for filtering (such as spam detection or determining interesting e-mails), make small short-term sacrifices in performance for very clean data.
```

如果你已经有选择的给用户展示邮件，那么你的训练数据将是有偏的。比较好的做法是用一个没有任何干扰的control group作为训练集。不需要太大，1%，2%就好。

```
Rule #35: Beware of the inherent skew in ranking problems.
```

算法会对线上的数据产生改变，从而影响未来会见到的数据。感觉这一点只能在模型迭代时，重新做分析了。

```
Rule #36: Avoid feedback loops with positional features
```

这点是和推荐算法相关。用户的点击与排序位置本身有关(人们倾向于点击第一个item)。如果没有位置特征，会把这类效应算到其他特征中去，导致模型估计不准。

```
Rule #37: Measure Training/Serving Skew.
```

评估训练和上线时模型表现的不同。可以做一些gap analysis。常见的可能原因有：使用了时间敏感的特征，过拟合等等。

## 5 增长趋缓，优化模型

建模的初步阶段，新模型的提升是明显的，全方位的。随着逐步优化，模型的提升不再那么显著。同时，不同指标可能出现有好有坏的情况。有趣的，有挑战性的阶段出现了。

```
Rule #38: Don’t waste time on new features if unaligned objectives have become the issue.
```

最终目标要明确，清晰。比如要看的是catch rate或是点击率等。

```
Rule #39: Launch decisions are a proxy for long-term product goals.
```

模型的目标往往是简单的，策略往往是复杂的。比如拒绝坏交易会减少损失，但是会带来交易量的下降。这些就需要做策略时去权衡。

```
Rule #40: Keep ensembles simple.
```

ensemble要简单，如可以做一个等权的相加。

```
Rule #41: When performance plateaus, look for qualitatively new sources of information to add rather than refining existing signals.
```

模型表现陷入瓶颈时，加入新的信息源以及新的特征往往是最有效的。同时，合理调整你对模型表现的预期。

```
Rule #42: Don’t expect diversity, personalization, or relevance to be as correlated with popularity as you think they are.
```

又是推荐领域的内容，常用的优化目标是代表流行度的点击率等。但是人们往往又会去追求个性化推荐，推荐内容多样等目标。可行的操作是采用后续的处理优化个性化及多样性。或者将他们直接加入优化目标。

```
Rule #43: Your friends tend to be the same across different products. Your interests tend not to be.
```

好友关系往往是稳定的。但是不同场景下的个性化特征往往是不同的。这并不是说我们不能在场景B中使用场景A的数据。跨场景的数据往往是有用的。

## 7 小结

这15条rule主要聚焦的是具体建模前的步骤，虽然有一丢丢宽泛，但提供了很好的大方向，是建模工作的基石。这些rule相信是前人踩了不少坑，总结出来的经验之谈。值得常看常新。  

下篇将涉及更为具体的建模内容，讨论有关特征工程以及优化模型方面的rule，敬请期待。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
