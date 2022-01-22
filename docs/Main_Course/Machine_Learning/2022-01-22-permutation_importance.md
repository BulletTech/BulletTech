---
template: overrides/blogs.html
---

# 特征选择之Permutation Importance

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()


## 前言

在之前的博客中提到了一些常用的特征选择的技巧，本文继续针对这一话题进行研究，讲解一种新的检查特征重要性的方法：Permutation Importance。如有兴趣，推荐阅读相关前文：

- [决策树学习笔记](https://mp.weixin.qq.com/s/waV7HG3KWs-Qx574aUHj3Q)
- [如何做特征选择](https://mp.weixin.qq.com/s/Cuw1ugpxm-5lF_rUkAu56Q)

## Permutation Importance

Permutation Importance适用于表格型数据，其对于特征重要性的评判取决于该特征被随机重排后，模型表现评分的下降程度。其数学表达式可以表示为：

- 输入：训练后的模型m，训练集（或验证集）D
- 模型m在数据集D上的性能评分s
- 对于数据集D的每一个特征j
  - 对于K次重复实验中的每一次迭代k，随机重排列特征j，构造一个被污染的数据集D_c_{k,j}
  - 计算模型m在数据集D_c_{k,j}上的性能评分s_{k,j}
  - 特征j的重要性分数i_{j}则可以记作`i_{j} = s - \frac{1/K}\sum_{k=1}^{K}s_{k,j}`



希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
