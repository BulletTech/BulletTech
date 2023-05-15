---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - cnn
---


# 卷积神经网络解释器简介

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485314&idx=1&sn=02d6f35c358ab4a596f3aaabc2704547&chksm=eb90f4f6dce77de0553c383583e4347835b15c44cf1d142fb028ed450f70e0e65e0528e314d4&token=762444875&lang=zh_CN#rd)


## 1 Introduction


exist
[TensorFlow Play Playground profile] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq=&mid=2247485294&IDX=1&SN=Deeef8a3485332AA43BFF8DE2 3BF0 & chksm = EB90F41Adce777778B4C510645F1A04ba7644F7ED53E039B09E900F04CFAE88A2D1E3 & Token = 1726922856 & Lang = zh_cn#RD)
In this article, the author introduces a product that recognizes neural networks (CNN) in a visual method. This content will share a similar website-`CNN Explainer`, which focuses on explaining in a visual way to explain` convolutional neural networks`, This product also shows the convolutional neural network and its related knowledge points in a very intuitive way.The address of the CNN Explaineer website is: https://poloclub.github.io/cnn-erxplainer/.


## 2 Product characteristics


The head of the CNN Explaineer website is a convolutional neural network for picture classification. The input is the three channels (red, green and blue) of the picture.If you come out, you can see the input of each convolution nucleus.




<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/cnn_explainer_home.png"  />

<figcaption> CNN interpreter </figcaption>
</figure>


Click on the convolution layer, the animation will show convolution operation, sweep the input picture step by step by step, form an output:


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/conv.png"  />

<figcaption> convolution operation </figcaption>
</figure>


Click the exclamation mark to jump to the corresponding documentation and examples. For example, for convolution operations, you can experience its working principle by adjusting the parameters of the input and convolution kernels.Document description and reference link.Product developers are really attentive!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/conv_tool.png"  />

<figcaption> Interactive understanding of convolution operations </figcaption>
</figure>


The operating schematic diagram and formula of the RELU activation function commonly used in convolution layers can also be displayed by clicking the corresponding layer:


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/ReLU.png"  />

<figcaption> RELU activation function schematic diagram </figcaption>
</figure>


Similarly, the schematic diagram and formula of the MaxPooling layer also vividly displayed, and the maximum value in the input was taken out as the output:




<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/MaxPooling.png"  />

<fIgcaption> Max Pooling Schematic diagram </figcaption>
</figure>


Finally, the output layer shows the model of the model prediction to varying degrees.


## 3 Summary


CNN Explainer showed important technical principles such as convolution operation, RELU function, SoftMax function, pooling, and flat layer in a very vivid way. You can also upload your own pictures for the model to predict it. Please try it yourself!I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>