---
template: overrides/blogs.html
---

# 读《Rules of Machine Learning》有感

!!! info 
    作者：Void，发布于2021-07-22，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/XwtXpa1hOKrN6fIC-zpyKw)

## 1 引言

第一次听到《Rules of Machine Learning》，就被它的勇气吓了一跳。是什么样的神仙敢起这样的题目，在这里指点江山？  
看到作者和来源后，好吧，原来是谷歌的大神。那我们就来看看这篇雄心勃勃的文章能教会我们什么吧。本文仅基于自己有限的经验与知识，欢迎讨论。

## 2 概述

文章开篇先来了个概述。

```
To make great products:
do machine learning like the great engineer you are, not like the great machine learning expert you aren’t.
```

实际工作中，最优先的是工程上的实现，是否清楚的定义了问题，是否有一个解决问题的solid的pipeline。其次才是fancy的算法用来锦上添花。  

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

虽然infra大概率已经提供好了，你还是可以带有质疑的眼光去检查它。不仅可以加深你对infra的理解，甚至可能发现祖传bug。

```
Rule #6: Be careful about dropped data when copying pipelines.
```

不同的场景可能对数据的要求不同。另外，多留个心眼检查下数据。可能你没注意的小细节(如join时，同个key的多条记录)，会使最终的结果和你预想的不同。

```
Rule #7: Turn heuristics into features, or handle them externally.
```

已有的有效的rule可以成为模型的特征，也可以直接使用它们(如黑名单)。

## 5 监控

```
Rule #8: Know the freshness requirements of your system.
```



## 3 小结


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
