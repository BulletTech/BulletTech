---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
---

# Introduction to TensorFlow Playground

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), published on 2021-06-06, reading time: about 6 minutes, article link on WeChat Official Account: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485294&idx=1&sn=deef8a34853332612aa43bff8de23bf0&chksm=eb90f41adce77d0c78b4c510645f1a04ba7644f7ed53e039b09e91e900f04cfae88a28a2d1e3&token=1726922856&lang=zh_CN#rd)

## 1. Introduction

When I was learning deep learning, I deeply felt the benefits of visualization: if you have an intuitive understanding of data, model structure, and model output, it will be easier to identify any errors that may occur, which is helpful for optimizing the model, and your understanding of related knowledge will also be deeper. Regarding the TensorFlow framework, Google has developed a very interesting application for displaying how neural networks work - [TensorFlow Playground](https://playground.tensorflow.org/ "TensorFlow Playground").

## 2. Product Features

This is the homepage of TensorFlow Playground, which provides basic functions for online training of neural networks (limited to multilayer perceptrons).

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/TF_Playground.png"  />
  <figcaption>The homepage of TensorFlow Playground</figcaption>
</figure>

The product offers many parameters for debugging. After setting the parameters, you can train a neural network by clicking "start"! This provides many optimization solutions for deep learning developers, such as:

- `Task Type`: Classification or regression.
- `Input Data`: The distribution of data, the proportion of data set splitting, noise in the data, and batch size.
- `Features`: Feature transformation.
- `Model Architecture`: The number of hidden layers, the number of neurons in the hidden layers, the type of neuron activation function, regularization parameters, output dimensions, etc.
- `Model Prediction Results`: The decision boundary of the model.

These influencing factors do not cover all aspects of actual work, but they provide many good entry points and an experimental platform. This is very helpful for understanding the principles, because you can easily verify your ideas through testing!

## 3. Conclusion

TensorFlow Playground is a very good experimental product for beginners. Try adjusting those parameters and check whether the model effect is the same as your expectations. If the result is not ideal, try to improve the performance of the model by adjusting those parameters. Actually, this is the workflow you need to face in actual work, and TensorFlow Playground is a very good start! I hope this sharing can help you, and feel free to leave a message in the comment section for discussion!

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>