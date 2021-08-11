---
template: overrides/blogs.html
---

# Kaggle tips

!!! info 
    作者：Void，发布于2021-07-20，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/XwtXpa1hOKrN6fIC-zpyKw)

## 1 引言

Kaggle作为最有名的数据科学竞赛平台(没有之一)，提供了各种高质量的比赛，也形成了友善、开源的社区氛围。各种大神总是慷慨地分享自己的知识和经验。  
本文整理了在Kaggle大宝库中所见所得的一些有用的tips。

## 2 Tips

[Chris Deotte](https://www.kaggle.com/cdeotte)是Kaggle社区一位活跃的大神，是Competitions，Datasets，Notebooks，Discussion的全科Grandmaster。在Discussion板块中更是排名世界第一(以讨论帖所得的奖牌数排名)。从他的讨论帖中总是能收获许多经验、知识。  

他有一篇关于特征工程的文章：  

- label encoding要训练集和测试集一起做。主要是防止测试集出现新的类别。这里需要注意的是，如果是涉及到label的处理，如woe，则需要训练集处理好，验证集按照字典去查找对应的值，以防止数据泄露。
- 空值处理。对于树模型来说，会将空值的样本基于增益分给左子树和右子树。一种处理方式是将空值填充为-999，这样这些样本也能参与结点的分裂。至于这种方式是否能提升模型表现，需要用验证结果来说话。
- 由于Kaggle竞赛题常会遇到数据量太大的问题，此时我们需要减少数据的内存占用。Kaggle上有一个经典的memory_reduce的函数可以很好地减少数据大小。
- 对于类别变量，对于树模型，在label encoding之后可以把它当作类别或是数字。至于哪种方法好，还是需要看验证结果。
- 将某个特征拆分成多个特征。如将金额拆分成整数和小数部分。不知道有没有用。
- 特征组合。类别变量的组合或是数字变量的加减乘除
- Frequency Encoding(等各种encoding)
- Group by之后的一些统计量
- 归一化。一般来说归一化都没有太大的问题(对于神经网络是必须的。有趋势的数据也可以去除趋势)
- 去除极端值的影响。

## 3 小结


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
