---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - cnn
---

# Introduction to Convolutional Neural Network Explainer

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on June 6, 2021, Reading time: about 6 minutes, WeChat Public Account Article link: [: fontawesome-solid-link:] (https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485314&idx=1&sn=02d6f35c358ab4a596f3aaabc2704547&chksm=eb90f4f6dce77de0553c383583e4347835b15c44cf1d142fb028ed450f70e0e65e0528e314d4&token=762444875&lang=zh_CN)


## 1 Introduction

In the article [Introduction to TensorFlow Playground] (https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid= 2247485294 & idx = 1 & sn = deef8a34853332612aa43bff8de23bf0 & chksm = eb90f41adce77d0c78b4c510645f1a04ba7644f7ed53e039b09e91e900f04cfae88a28a2d1e3 & token = 1726922856 & lang = zh_CN #rd), the author introduced a product that uses visualization to understand neural networks (CNNs). This article will share a similar website - `CNN Explainer`, which focuses on explaining `Convolutional Neural Networks` in a visual way. The product shows convolutional neural networks and related knowledge points in a very intuitive way. The CNN Explainer website address is: https://poloclub.github.io/cnn-explainer/.

## 2 Product Features

The header of the CNN Explainer website is a convolutional neural network used for image classification. The input is the three channels of the image (red, green, and blue), and the style of the image after each layer of calculation in the network is also displayed. Hover over the mouse to see the input of each convolution kernel.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/cnn_explainer_home.png"  />
  <figcaption>CNN Interpreter</figcaption>
</figure>

Clicking on a convolutional layer displays the convolution operation, and the convolution kernel scans the input image step by step to form the output:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/conv.png"  />
  <figcaption>Convolution operation</figcaption>
</figure>

Clicking on the exclamation mark will take you to the corresponding documentation and examples. For example, for the convolution operation, you can experience its working principle by adjusting the parameters of the input and convolution kernel. The animation will change according to the input, and it also comes with detailed document instructions and reference links. The developers of the product are really attentive!

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/conv_tool.png"  />
  <figcaption>Interactive understanding of convolution operation</figcaption>
</figure>

The operation diagram and formula of the ReLU activation function commonly used in convolutional layers can also be displayed by clicking on the corresponding layer:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/ReLU.png"  />
  <figcaption>ReLU activation function diagram</figcaption>
</figure>

Similarly, the diagram and formula of the MaxPooling layer are also displayed in an imageable way, and the maximum value in the input is taken out as the output:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/MaxPooling.png"  />
  <figcaption>Max Pooling diagram</figcaption>
</figure>

Finally, the output layer uses a different degree of highlight to display the predicted category of the model.

## 3 Summary

The CNN Explainer shows the important technical principles such as convolution operation, ReLU function, Softmax function, pooling, and flattening layer in a very vivid way. You can also upload your own images for the model to make predictions, so please try it out for yourself! I hope this share is helpful to you and welcome to leave a message in the comment section for discussion!

