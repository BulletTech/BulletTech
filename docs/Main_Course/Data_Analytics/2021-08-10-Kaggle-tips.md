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

- label encoding要训练集和测试集一起做。主要是防止测试集出现新的类别。这里需要注意的是，如果是涉及到label的处理，如WOE，则需要训练集处理好，验证集按照字典去查找对应的值，以防止数据泄露。
- 空值处理。对于树模型来说，会将空值的样本基于增益分给左子树和右子树。一种处理方式是将空值填充为-999，这样这些样本也能参与结点的分裂。至于这种方式是否能提升模型表现，需要用验证结果来说话。
- 由于Kaggle竞赛题常会遇到数据量太大的问题，此时我们需要减少数据的内存占用。Kaggle上有一个经典的memory_reduce的函数可以很好地减少数据大小。
- 对于树模型中的类别变量，在label encoding之后可以把它当作类别或是数字。至于哪种方法好，还是需要看验证结果。
- 将某个特征拆分成多个特征。如将金额拆分成整数和小数部分。不知道有没有用。
- 特征组合。类别变量的组合或是数字变量的加减乘除
- Frequency Encoding(等各种encoding)
- Group by之后的一些统计量
- 归一化。一般来说归一化都没有太大的问题(对于神经网络是必须的。有趋势的数据也可以去除趋势。)
- 去除极端值的影响。

在IEEE-CIS Fraud Detection这个竞赛中，Chris也拿了第一名。关于此竞赛的经验分享有：

- 赛题的关键是识别出客户的uid。但是不能直接把uid等id类变量作为特征，因为测试集中有很多新出现的uid。
- CatBoost模型在树模型中表现较好
- 变量的时间一致性：这里Chris所用的方式是对每一个变量用第一个月的数据去训练一个模型，然后看最后一个月的模型表现。如果表现较差，则说明这个变量可能只在过去起作用，这时应该丢弃这些变量。
- 低variance的数字变量往往是没有用的。sklearn.feature_selection中有VarianceThreshold来进行特征筛选。 

Chris还参加了一些图像、NLP相关的比赛，由于和自己的主营业务不太相关，这里就不做整理了。


## 3 小结

这些知识、经验虽然有一些针对比赛的奇淫技巧，但是它们对于日常建模仍然具有一定的指导意义，值得我们去思考、尝试。  
感谢这些大神们乐于分享的精神，能从Kaggle大社区中汲取知识和营养真是一种幸事。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
