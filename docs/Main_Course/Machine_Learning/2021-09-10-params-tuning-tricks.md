---
template: overrides/blogs.html
tags:
  - machine learning
---

# 神经网络调参技巧

!!! info
    作者：Void，发布于2021-09-10，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484538&idx=1&sn=ae97eac88e44ae8b2f0466cf09e606c0&chksm=eb90f70edce77e1852aaf09ccca473b088b91d870f63c326166f7921d02ae7bb97e614b491ad&scene=178&cur_album_id=2045821482966024195#rd)

## 1 引言

最近向知乎大神学习了一波神经网络的调参技巧，也搜到了深度学习专家Andrej Kapathy的一篇博客[《A Recipe for Training Neural Networks》](https://karpathy.github.io/2019/04/25/recipe/)。在此结合这几篇文章和自己的一些经验，做一篇神经网络调参的小技巧分享。

## 2 损失曲线分析

有了Tensorboard, MLflow等可视化工具，训练过程中的损失曲线很容易观测。曲线的形状往往可以直观地反应模型训练的状况。

- 常见的损失曲线往往一开始下降较快，后面逐渐趋缓。如果发现曲线接近线性，则可能学习率较小，损失下降不够充分。
- 曲线波动过于剧烈，可能的原因是batch size太小。batch size也不是越大越好，batch size小的时候，每个batch计算的梯度方向没有那么精确，batch间的方差较大，反而容易逃离鞍点。batch size可以作为一个超参数调节。经验上，batch size可以为数据量的根号大小。
- 训练集和验证集曲线差距较大，可能是训练集发生了过拟合。反之，若差距太小，则可能模型拟合不够。
- loss最小的点未必是评价指标最优的点。比如在二分类问题中，loss最小的点未必是auc最大的点。有效的方法是，打印出每一个epoch的模型表现。
- 在实际使用过程中，我还遇到过验证集loss一路向上的情况，奇怪的是选出的模型在测试集上表现并不差，似乎并不是由于过拟合造成的。这一现象在知乎上也有[讨论](https://www.zhihu.com/question/318399418/answer/1202932315)，大家的观点是验证集的loss并不能完全反应最终模型的好坏。

## 3 学习率调整

对神经网络来说，学习率的调整优先级较高。调参的顺序可以是学习率、epoch个数 - batch size - 学习率衰减参数。

- 可以尝试使用学习率的warm up。
- 学习率衰减的参数在不同模型和任务下往往不同。
- 一般以10倍间隔来进行参数搜索。


## 4 dropout层

dropout层可以很好地减少过拟合。另一方面，还可以认为是一种模型ensemble的方式，推荐大家使用。

## 5 优化器

Adam优化器是对参数比较稳健的优化器，包括不合适的学习率。

## 6 ensemble

我们甚至可以用不同的随机数种子来ensemble模型。

## 7 Swish激活函数

Swish激活函数其实已经提出来很久了，但是最近Kaggle的高分方案中它却屡屡出现。它的形式是：f(x) = x · sigmoid(x)。是一个平滑且非单调的函数。  
在提出的它的论文中，作者指出了在神经网络层数大于40层以后，Swish激活函数优于ReLU等其他激活函数。在浅层神经网络中，它对模型结果是否有所提升，仍需要我们自己去尝试。

## 8 batch normalization

batch normalization在norm的时候，使每个独立样本看到了同一个batch内其他样本的信息，起到了一定的正则化的效果。  
0均值也使输入位于激活函数的饱和区，加快收敛速度。

## 9 小结

调参有科学也有艺术的成分。在实际使用过程中，不妨尝试一下上述经验之谈。可能某些tips恰好适用于你的模型和任务，助你模型表现一飞冲天。


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
