---
template: overrides/blogs.html
tags:
  - DeepLearning
---


# 卷积神经网络解释器简介

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485314&idx=1&sn=02d6f35c358ab4a596f3aaabc2704547&chksm=eb90f4f6dce77de0553c383583e4347835b15c44cf1d142fb028ed450f70e0e65e0528e314d4&token=762444875&lang=zh_CN#rd)


## 1 前言

在[TensorFlow Playground简介](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485294&idx=1&sn=deef8a34853332612aa43bff8de23bf0&chksm=eb90f41adce77d0c78b4c510645f1a04ba7644f7ed53e039b09e91e900f04cfae88a28a2d1e3&token=1726922856&lang=zh_CN#rd)这篇文章里，笔者介绍了一个用可视化的方法认识神经网络（CNN）的产品，本次内容将分享一个类似的网站 - `CNN Explainer`，它专注于用可视化的方式讲解`卷积神经网络`，该产品同样以非常直观的方式展示了卷积神经网络及其相关知识点。CNN Explainer网站地址为：https://poloclub.github.io/cnn-explainer/。

## 2 产品特性

CNN Explainer网站的头部即是一个用于图片分类的卷积神经网络，输入是图片的三个通道（红，绿和蓝），其中图片在网络的每一层计算后呈现的样式也被展示出来，悬浮鼠标即可看到每个卷积核的输入。


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/cnn_explainer_home.png"  />
  <figcaption>CNN 解释器</figcaption>
</figure>

点击卷积层，动画将显示卷积操作，卷积核一步一步地扫过输入图片，形成输出：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/conv.png"  />
  <figcaption>卷积操作</figcaption>
</figure>

点击感叹号即可跳转到对应的文档和示例，比如针对卷积操作，你可以通过调整输入和卷积核的参数来体会它的工作原理，动画将根据输入进行变化，同时还附有详细的文档说明和参考链接。产品的开发者真是非常用心了！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/conv_tool.png"  />
  <figcaption>交互式地理解卷积操作</figcaption>
</figure>

卷积层常用的ReLU激活函数的操作示意图和公式也可以通过点击相对应的层展示：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/ReLU.png"  />
  <figcaption>ReLU激活函数示意图</figcaption>
</figure>

同样地，MaxPooling层的示意图和公式也形象地展示了出来，输入里的最大值被取了出来作为输出：


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/MaxPooling.png"  />
  <figcaption>Max Pooling示意图</figcaption>
</figure>

最后输出层用不同程度高亮的方式展示了模型预测的类别。

## 3 总结

CNN Explainer以非常生动的方式展示了卷积操作、ReLU函数、Softmax函数、池化、展平层等重要技术原理，并且你还可以上传自己的图片让模型进行预测，请自己尝试吧！希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
