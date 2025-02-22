---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - cnn
---

# 深度学习 101-搭建 ResNet 识别鲜花图像

!!! info
    作者：Jeremy，发布于 2021-11-07，阅读时间：约 6 分钟，微信公众号文章链接：[:fontawesome-solid-link:](http://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484833&idx=1&sn=ce699ce77f78c8f205fdaad306a6b043&chksm=eb90f6d5dce77fc322aafa60057257ec282407c5f7627c716239e4cd8849399e0f3cdb0d5a14#rd)

## 1 前言

ResNet 是一种经典的图像识别领域模型，在 2015 年图像识别领域多个竞赛中排行第一，并且性能上相较第二有大幅提升。在这篇文章里，我们就站在巨人们的肩膀上，搭建一个基于 ResNet 识别花卉图片（Oxford 102 Flowers）的神经网络吧。

## 2 ResNet 简介

在 ResNet 以前，由于存在梯度消失和梯度爆炸的问题，神经网路层数越深，网络越难以训练，导致深层网络的准确度出现下降。

ResNet 通过引入残差块（Residual block），将 a[l]添加到第二个 ReLU 过程中，直接建立 a[l]与 a[l+2]之间的隔层联系。表达式如下：

$$
\begin{gathered}
z^{[l+1]}=W^{[l+1]} a^{[l]}+b^{[l+1]} \\
a^{[l+1]}=g\left(z^{[l+1]}\right) \\
z^{[l+2]}=W^{[l+2]} a^{[l+1]}+b^{[l+2]} \\
a^{[l+2]}=g\left(z^{[l+2]}+a^{[l]}\right)
\end{gathered}
$$

[论文](https://arxiv.org/abs/1512.03385 'Deep Residual Learning for Image Recognition')作者推测模型对残差的拟合优化会比对随机权重的拟合更加容易（因为baseline就是恒等映射），所以在极端状况下，残差块的中间层没有激活，即W≈0，b≈0，则有：

$$
\begin{aligned}
a^{[l+2]} &=g\left(z^{[l+2]}+a^{[l]}\right) \\
&=g\left(W^{[l+2]} a^{[l+1]}+b^{[l+2]}+a^{[l]}\right) \\
&=g\left(a^{[l]}\right) \\
&=\operatorname{ReLU}\left(a^{[l]}\right) \\
&=a^{[l]}
\end{aligned}
$$

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Residual-block.jpg"/>
  <figcaption>残差块示例</figcaption>
</figure>

所以这种构造方式保证了深层的网络比浅层包含了更多（至少恒等）的图像信息。多个残差块推挤在一起，便形成了一个残差网络。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/ResNet-Paper.png"/>
  <figcaption>残差网络和普通深度神经网络对比</figcaption>
</figure>

## 3 用 ResNet 构造分类模型

在下列 demo 中，我们使用 keras 已有的 ResNet50预训练模型，对 Oxford 102 Flowers 数据集中的 10 种花卉图片进行多分类任务模型的构造。在工程上我们只需要修改 ResNet50 顶部的全连接层，对输入的图片数据进行裁剪，旋转，放大等数据增强，训练所有模型参数即可。代码如下：

```python

import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, load_model
from keras.applications import ResNet50
from keras.optimizers import Adam
from keras.layers import Flatten, Dense, Dropout, Input
from keras.callbacks import EarlyStopping, ModelCheckpoint
import numpy as np
import math

def fc_block(X,units,dropout,stage):
    fc_name = 'fc' + str(stage)
    X = Dense(units,activation ='elu',name = fc_name)(X)
    X = Dropout(dropout)(X)
    return X

def ResNet50_transfer():

    #call base_model
    base_model = ResNet50(
        include_top=False,
        weights="imagenet",
        input_tensor= Input(shape=img_size + (3,))
    )

    # freeze resnet layers' params
    for layer in base_model.layers:
        layer.trainable = False

    # top architecture
    X = base_model.output
    X = Flatten()(X)
    X = Dropout(0.4)(X)
    X = fc_block(X,fc_layer_units[0],dropout = 0.4,stage = 1)
    X = fc_block(X,fc_layer_units[1],dropout = 0.4,stage = 2)

    # output layer
    X = Dense(len(classes),activation='softmax',name = 'fc3_output')(X)

    # create model
    model = Model(inputs = base_model.input,outputs = X, name = 'ResNet50_transfer')

    return model

def generate_data(train_path,valid_path):
    # generate & augment training data
    train_datagen = ImageDataGenerator(rotation_range=30., shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    train_datagen.mean = np.array([123.675, 116.28 , 103.53], dtype=np.float32).reshape((3, 1, 1))
    train_data = train_datagen.flow_from_directory(train_path, target_size=img_size, classes=None)
    # generate training data
    valid_datagen = ImageDataGenerator()
    valid_datagen.mean = np.array([123.675, 116.28 , 103.53], dtype=np.float32).reshape((3, 1, 1))
    valid_data = train_datagen.flow_from_directory(valid_path, target_size=img_size, classes=None)
    return train_data, valid_data

def call_back():
    early_stopping = EarlyStopping(verbose=1, patience=10, monitor='val_loss')
    model_checkpoint = ModelCheckpoint(filepath='102flowersmodel.h5', verbose=1, save_best_only=True, monitor='val_loss')
    callbacks = [early_stopping, model_checkpoint]
    return callbacks

# path_to_img: 'dataset/flower_data_10/train/1//image_06734.jpg'
train_path = 'dataset/flower_data_10/train'
valid_path = 'dataset/flower_data_10/valid'

nb_epoch = 20
batch_size = 32
img_size = (224,224)

# output classes
classes = list(map(str,[1,2,3,4,5,6,7,8,9,10]))
rgb_mean = [123.68, 116.779, 103.939]
fc_layer_units = [512,64]

model = ResNet50_transfer()
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=1e-5), metrics=['accuracy'])
train_data, valid_data = generate_data(train_path,valid_path)
callbacks = call_back()
model.fit_generator(train_data, steps_per_epoch= math.ceil(train_data.samples / batch_size), epochs=nb_epoch,
                    validation_data=valid_data, validation_steps=math.ceil(valid_data.samples / batch_size),
                    callbacks=callbacks)
```

经过 20 个 epoch 的训练后，验证集的准确度已经达到了 0.8837。

## 4 小结

本文章简单地介绍了 ResNet 的特点，以及提供了搭建图片分类模型的代码模板。显卡配置较高的同学可以尝试搭建不同规模的 ResNet 网络观察网络深度对模型性能的影响；对于图像识别模型感兴趣的同学推荐细读 ResNet 论文: Deep Residual Learning for Image Recognition。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
