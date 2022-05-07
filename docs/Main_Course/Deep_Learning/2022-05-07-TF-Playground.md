---
template: overrides/blogs.html
---

# TensorFlow Playground简介

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

本人在学习深度学习时，对可视化的好处深有体会：如果对数据、模型结构、模型输出等信息有直观的理解，将更容易发现其中可能出现的错误，这有利于优化模型，并且自己对于相关知识点的认识也更加深刻。对于TensorFlow框架而言，Google做了一个非常有趣的应用来展示神经网络的工作原理 - [TensorFlow Playground](https://playground.tensorflow.org/ "TensorFlow Playground")。

## 2 产品特征

这是TensorFlow Playground的主页，它提供了在线训练神经网络（仅限于多层感知机）的基本功能。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/TF_Playground.png"  />
  <figcaption>TensorFlow Playground的主页</figcaption>
</figure>

该产品开放了多种参数可供调试，设置好参数后，点击开始就能训练一个神经网络！这给深度学习的开发者提供了许多优化解决方案的思路，比如：

- `任务类型`：分类或是回归。
- `输入数据`：如数据的分布、数据集分割的比例、数据里存在的噪音和批量大小。
- `特征`：特征的变换。
- `模型架构`：隐藏层的数量、隐藏层里神经元的数量、神经元激活函数的类型、正则化的参数、输出的维度等。
- `模型预测结果`：模型决策边界。

这些影响因素并未涵盖实际工作中的方方面面，但它提供了许多不错的切入点，和一个可供实验的平台。这对于了解原理非常有帮助，因为你可以通过测试很方便地验证你的设想！

### 3 总结

TensorFlow Playground对于初学者是一个非常好的试验产品，不妨动手去调整那些参数，检查模型效果是否与你的预期相同，如果结果不理想，想办法通过调整那些参数让模型的性能变得更好，这其实就是实际工作中你需要面对的工作流，而TensorFlow Playground成为一个非常不错的开始！希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
