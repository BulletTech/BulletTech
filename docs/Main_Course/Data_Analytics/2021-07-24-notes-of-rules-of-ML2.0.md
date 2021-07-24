---
template: overrides/blogs.html
---

# 读《Rules of Machine Learning》有感（下）

!!! info 
    作者：Void，发布于2021-07-22，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/XwtXpa1hOKrN6fIC-zpyKw)

## 1 引言

第一次听到[《Rules of Machine Learning》](http://martin.zinkevich.org/rules_of_ml/)，就被它的题目吓了一跳。是什么样的神仙敢起这样的题目，在这里指点江山？  
看到作者和来源后，好吧，原来是谷歌的大神。那我们就来看看这篇雄心勃勃的文章能教会我们什么吧。  
由于文章较长(有3个阶段，43条rule)，本文是这一系列的上篇(包含第一阶段)。本文仅基于自己有限的经验与知识，在翻译的基础上加了一些自己的理解，欢迎讨论。

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



## 7 小结

这15条rule主要聚焦的是具体建模前的步骤，虽然有一丢丢宽泛，但提供了很好的大方向，是建模工作的基石。这些rule相信是前人踩了不少坑，总结出来的经验之谈。值得常看常新。  

下篇将涉及更为具体的建模内容，讨论有关特征工程以及优化模型方面的rule，敬请期待。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
