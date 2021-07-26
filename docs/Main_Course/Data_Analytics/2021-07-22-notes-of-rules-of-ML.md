---
template: overrides/blogs.html
---

# 读《Rules of Machine Learning》有感（上）

!!! info 
    作者：Void，发布于2021-07-26，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/mhEt3WCvwKNuFSv8tVlPeA)

## 1 引言

第一次听到[《Rules of Machine Learning》](http://martin.zinkevich.org/rules_of_ml/)，就被它的题目吓了一跳。是什么样的神仙敢起这样的题目，在这里指点江山？  
看到作者和来源后，好吧，原来是谷歌的大神。那我们就来看看这篇雄心勃勃的文章能教会我们什么吧。  
由于文章较长(有3个阶段，43条rule)，本文是这一系列的上篇(包含第一阶段)。本文仅基于自己有限的经验与知识，在翻译的基础上加了一些自己的理解，欢迎讨论。

## 2 概述

文章开篇先来了个概述。

```
To make great products:
do machine learning like the great engineer you are, not like the great machine learning expert you aren’t.
```

实际工作中，最优先的是工程上的实现，是否清楚地定义了问题，是否有一个解决问题的solid的pipeline。其次才是fancy的算法用来锦上添花。  

## 3 在使用机器学习以前

```
Rule #1: Don’t be afraid to launch a product without machine learning.
```

简单的模型，直接的rule永远是你的baseline。它可能没有那么好，但是在你一无所有时，它足够有效。

```
Rule #2: First, design and implement metrics
```

设计好评价指标，做好记录。

```
Rule #3: Choose machine learning over a complex heuristic
```

当你的规则过于复杂时，请使用机器学习。机器学习之所以神奇，就是因为它能学到各种复杂的关系。并且模型更新起来比较简单。

## 4 你的第一个pipeline

```
Rule #4: Keep the first model simple and get the infrastructure right.
```

有一个足够solid的baseline，因为后续的一切都将基于它。

```
Rule #5: Test the infrastructure independently from the machine learning
```

虽然infra大概率已经提供好了，你还是可以带有质疑的眼光去检查它。这不仅可以加深你对infra的理解，甚至可能帮助你发现祖传bug。

```
Rule #6: Be careful about dropped data when copying pipelines.
```

不同的场景可能对数据的要求不同(有的需要历史数据，有的只需要最新数据)。另外，多留个心眼检查下数据。可能你没注意的小细节(如join时，同个key的多条记录)，会使最终的结果和你预想的不同。

```
Rule #7: Turn heuristics into features, or handle them externally.
```

已有的有效的rule可以成为模型的特征，也可以直接使用它们(如黑白名单)。

## 5 监控

```
Rule #8: Know the freshness requirements of your system.
```

根据模型重要性，监控模型的表现。

```
Rule #9: Detect problems before exporting models.
```

尽量在模型上线前发现所有问题。

```
Rule #10: Watch for silent failures.
```

除了模型的评价指标，监控好模型的依赖，如背后的数据，特征等等是否有缺失等异常情况。这一点其实很tricky，总会有数据存在问题，那么这一问题会对模型造成多大影响呢？

```
Rule #11: Give feature column owners and documentation.
```

做好文档，可能大公司或多或少都存在文档不全的问题。。

## 6 你的第一个目标

```
Rule #12: Don’t overthink which objective you choose to directly optimize.
```

不要纠结于优化哪一个目标。其实对于这一点，我的理解是优化目标有重要性之分。如在某些场景中，抓到坏人比冤枉好人带来的好处更大。那么模型首先该关注的应该是catch rate。很难做到新的模型在各种维度下都优于已有的解决方案。

```
Rule #13: Choose a simple, observable and attributable metric for your first objective.
```

给你的模型选择一个简单，可观测，可归因的评价指标。复杂的、不直接的请交给策略分析师们。

```
Rule #14: Starting with an interpretable model makes debugging easier.
```

一开始选择解释性强的模型，便于debug。不要一上来就来fancy的算法，这只会增加你发现问题的难度。

```
Rule #15: Separate Spam Filtering and Quality Ranking in a Policy Layer.
```

不同任务的背景不同，不要希望在A任务表现好的模型一定在B任务表现的好。

## 7 小结

这15条rule主要聚焦的是具体建模前的步骤，虽然有一丢丢宽泛，但提供了很好的大方向，是建模工作的基石。这些rule相信是前人踩了不少坑，总结出来的经验之谈。值得常看常新。  

下篇将涉及更为具体的建模内容，讨论有关特征工程以及优化模型方面的rule，敬请期待。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
