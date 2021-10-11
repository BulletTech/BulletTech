---
template: overrides/blogs.html
---

# 算法中的multi家族

!!! info
    作者：Void，发布于2021-10-10，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/t_QkSxjtcFpX9pdx_OcXtA)

## 1 前言

在机器学习中，有一些multi-X的任务，如multi-class(多分类)，multi-label(多标签)，multi-task(多任务)等任务。今天，我们就来一起研究下multi家族。

## 2 multi-class任务

多分类任务是指每条数据有一个标签，但标签有多个类别(大于2)。多分类任务与常见的二分类任务相比，区别不大。需要注意的是，此时，损失函数由二分类问题中经过sigmoid函数后，计算的二元交叉熵转变为经过softmax函数后，计算的多元交叉熵。

$$
J=-\sum_{i=1}^{K} y_{i} \log \left(p_{i}\right)
$$

多分类任务的评价指标也有所不同。常见二分类问题的评价指标有：准确率(Precision)、召回率(Recall)和F1值(F1-score)。这些都是建立在二分类的混淆矩阵(2维)的基础上。  
对于多分类问题，这三个评价指标又分别存在micro和macro两类。如在sklearn.metrics.f1_score中average有以下几种参数：{'micro', 'macro', 'samples','weighted', 'binary'} or None。  
对于macro，我们分别计算每个类别的准确率、召回率和F1值，然后取平均得到最终的评价指标。考虑到类别不平衡，我们可以算平均时加上权重(weighted)。  
对于micro，我们计算总体的混淆矩阵然后计算最终的评价指标。

## 3 multi-label任务

多标签任务是指每条数据有多个标签。例如，预测一位病人是否患有多种疾病。  
最简单的处理方式是把它当做多个二分类任务来处理。但是，这样既费时费力，同时多个标签之间往往会存在相关关系。  
常见的做法是仍然在同一个模型中进行训练(一个loss)。处理方式是对最后分类层(n个结点表示n个标签)的输出作用sigmoid函数，然后分别计算二元交叉熵并取平均。更高级的做法是使用序列模型或图模型，它们的好处是可以考虑到不同标签之间的依赖关系。

## 4 multi-task任务

多任务学习是指同时学习多个任务(有多个loss)，如预测用户是否点击和是否转发。一般来说多个任务是同步学习的，当然也可以采用异步的模式(更像是预训练，在任务A的基础上用任务B做微调)。  

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/multitask.png" width="500" />
</figure>

常见的多任务学习的模型结构如图(a)所示，底层参数完全共享，顶层参数随不同任务而不同。这种方式要求不同任务的输入变量需要保持一致，这一点往往是很难做到的(不同任务有各自独有的特征)。因此如(c)所示的MMOE(Multi-gate Mixture-of-Experts)的结构出现了。它允许我们有共享也有独有的部分，它们的权重由gate通过学习来决定。  
多任务学习的好处可能有以下几点：  

- 缓解冷启动问题，如新任务数据量较小。
- 提高模型的鲁棒性。不同的任务往往有不同的噪声。


## 5 总结

本文总结了在机器学习任务中常出现的multi家族。理清它们的概念有利于身心健康，更能让你灵活地使用不同任务解决实际问题。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
