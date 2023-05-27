---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - cnn
---

# Image Classification with TensorFlow

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published: June 6, 2021, Read Time: about 6 minutes, WeChat Official Account link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485322&idx=1&sn=fa14d124716d769143ffcee9d29a7fba&chksm=eb90f4fedce77de8426ec72754e8394dd937a839744131e383155aa99a74caa236cdbaaf13a0&token=762444875&lang=zh_CN#rd)

## 1 Introduction

In this article, we will discuss the task of multi-category image classification using TensorFlow, including image data loading, data enhancement, model training, transfer learning and the use of TensorBoard. All the APIs are based on TensorFlow v2.8.0. The following code is executed in Google Colab since Google provides free GPUs that can significantly accelerate the training process.

## 2 Image Processing

Load the original image data containing 10 categories of targets.

```python
import zipfile
import os
import matplotlib.pyplot as plt
import datetime


import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.ops.gen_array_ops import shape
from tensorflow.keras import layers


!wget https://storage.googleapis.com/ztm_tf_course/food_vision/10_food_classes_all_data.zip

# Unzip the downloaded file
zip_ref = zipfile.ZipFile("10_food_classes_all_data.zip", "r")
zip_ref.extractall()
zip_ref.close()

# Function to process the image
def load_and_process_image(file_name, img_shape=224):
  """
  Read an image and process it, reshape it to (img_shape, img_shape, color_channels)
  """
  # read the image
  img = tf.io.read_file(file_name)

  # decode the read file into a tensor
  img = tf.image.decode_image(img)

  # resize the image
  img = tf.image.resize(img, size=[img_shape, img_shape])

  # scale the image
  img = img/255.

  return img

# Display files
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

# Walk through 10_food_classes directory and list number of files
for dirpath, dirnames, filenames in os.walk("10_food_classes_all_data"):
  print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")
```

It can be seen from the output that the data contains images of ice cream, steak, pizza, etc.

```py
There are 2 directories and 0 images in '10_food_classes_all_data'.
There are 10 directories and 0 images in '10_food_classes_all_data/test'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/chicken_wings'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/pizza'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/grilled_salmon'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/sushi'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/fried_rice'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/ice_cream'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/chicken_curry'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/hamburger'.
There are 0 directories and