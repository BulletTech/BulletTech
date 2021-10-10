---
template: overrides/blogs.html
---

# 算法中的multi家族

!!! info
    作者：Void，发布于2021-10-10，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

在机器学习中，有一些multi-X的任务，如multi-label(多标签)，multi-class(多分类)等任务。今天，我们就来一起研究下multi家族。

## 2 multi-class任务

多分类任务是指每条数据有一个标签，但标签有多个类别(大于2)。多分类任务与常见的二分类任务相比，区别不大。需要注意的是，此时，损失函数由二分类问题中经过sigmoid函数后，计算的二元交叉熵转变为经过softmax函数后，计算的多元交叉熵。

$$
J=-\sum_{i=1}^{K} y_{i} \log \left(p_{i}\right)
$$

多分类任务的评价指标也有所不同。常见二分类问题的评价指标有：准确率(Precision)、召回率(Recall)和F1值(F1-score)。这些都是建立在二分类的混淆矩阵(2维)基础上。  
对于多分类问题这三个评价指标又分别存在micro和macro两类。如在sklearn.metrics.f1_score中average有以下几种参数：{'micro', 'macro', 'samples','weighted', 'binary'} or None。  
对于macro，我们是分别计算每个类别的准确率、召回率和F1值，然后取平均得到最终的评价指标。考虑到类别不平衡，我们可以算平均时加上权重(weighted)。  
对于micro，我们是计算总体的混淆矩阵然后计算最终的评价指标。

## 3 multi-label任务

多标签任务是指每条数据有多个标签。例如，预测一位病人是否患有多种疾病。  
最简单的处理方式是把它当做多个二分类任务来处理。但是，这样既费时费力，同时多个标签之间往往会存在相关关系。


## 3 总结

上述例子介绍了如何自定义keras模型，能够为日常的工作流更添灵活性，实际工作中，还需反复推敲，确保正确无误。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
