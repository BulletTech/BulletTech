# Deep Learning 101 - Building ResNet for Flower Image Recognition

!!! info
    Author: Jeremy, Posted on Nov. 7, 2021, Reading Time: about 6 minutes, WeChat Official Account Article Link: [:fontawesome-solid-link:](http://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484833&idx=1&sn=ce699ce77f78c8f205fdaad306a6b043&chksm=eb90f6d5dce77fc322aafa60057257ec282407c5f7627c716239e4cd8849399e0f3cdb0d5a14#rd)

## 1 Introduction

ResNet is a classic model in the field of image recognition. In 2015, ResNet ranked first in multiple image recognition competitions and significantly improved performance over the second place. In this article, we will build a neural network based on ResNet to recognize flower images (Oxford 102 Flowers).

## 2 Introduction to ResNet

Before ResNet, there were problems with vanishing gradient and exploding gradient in neural networks. The deeper the neural network, the more difficult it was to train, and the accuracy of deep networks decreased.

ResNet introduces residual blocks. It adds a[l] to the second ReLU process and directly establishes a contact layer between a[l] and a[l+2]. The expression is as follows:

$$
\begin{gathered}
z^{[l+1]}=W^{[l+1]} a^{[l]}+b^{[l+1]} \\
a^{[l+1]}=g\left(z^{[l+1]}\right) \\
z^{[l+2]}=W^{[l+2]} a^{[l+1]}+b^{[l+2]} \\
a^{[l+2]}=g\left(z^{[l+2]}+a^{[l]}\right)
\end{gathered}
$$

The authors of the [paper](https://arxiv.org/abs/1512.03385 'Deep Residual Learning for Image Recognition') speculated that the model's optimization of residuals would be easier than random weight fitting (because the baseline is the identity mapping). Therefore, in extreme situations, the middle layer of residual blocks is not activated, W ≈ 0, b ≈ 0, and it can be simplified as:

$$
\begin{aligned}
a^{[l+2]} &=g\left(z^{[l+2]}+a^{[l]}\right) \\
&=g\left(W^{[l+2]} a^{[l+1]}+b^{[l+2]}+a^{[l]}\right) \\
&=g\left(a^{[l]}\right) \\
&=\operatorname{ReLU}\left(a^{[l]}\right) \\
&=a^{[l]}
\end{aligned}
$$

Therefore, this construction method ensures that deep networks contain at least the same (identity) image information as shallow networks. Multiple residual blocks pushed together forms a residual network.

## 3 Constructing a Classification Model with ResNet

In the following demo, we use the pre-trained ResNet50 model provided by Keras to construct a multi-classification task model for 10 kinds of flower images in the Oxford 102 Flowers dataset. In terms of engineering, we only need to modify the fully connected layer of ResNet50 and perform data enhancement such as cutting, rotating, and enlarging the input image data to train all model parameters. The code is as follows:

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

After 20 epochs of training, the accuracy on the validation set has reached 0.8837.

## 4 Conclusion

This article briefly introduces the characteristics of ResNet and provides a code template for building image classification models. Students with high GPU configuration can try building ResNet networks of different sizes to observe the impact of network depth on model performance. Students interested in image recognition models are recommended to read the ResNet paper, "Deep Residual Learning for Image Recognition."