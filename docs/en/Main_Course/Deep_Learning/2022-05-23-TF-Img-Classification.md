---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - cnn
---

# 使用TensorFlow进行图片分类

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485322&idx=1&sn=fa14d124716d769143ffcee9d29a7fba&chksm=eb90f4fedce77de8426ec72754e8394dd937a839744131e383155aa99a74caa236cdbaaf13a0&token=762444875&lang=zh_CN#rd)

## 1 Introduction


This article will use TensorFlow to discuss the tasks classification of multiple categories. The main content includes the loading of picture data, data enhancement, model training and migration learning, and Tensorboard. All APIs are based on TensorFlow V2.8.0.The following code runs in Google Colab, because Google provides free GPUs to speed up significantly.


## 2 processing pictures


Load the original picture data containing the target 10 types.


```python
import zipfile
Import us
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


# The function of the picture
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



# 显示
def list_files(startpath):
for root, dirs, files in os.walk(startpath):
level = root.replace(startpath, '').count(os.sep)
indent = ' ' * 4 * (level)
print('{}{}/'.format(indent, os.path.basename(root)))
subindent = '' * 4 * (Level + 1)
for f in files:
Print ('{} {}. format (subindent, f))


# Walk through 10_food_classes directory and list number of files
for dirpath, dirnames, filenames in os.walk("10_food_classes_all_data"):
print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")
```


It can be seen from the output that there are pictures such as ice cream, steak, pizza and other pictures in the data.


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
There are 0 directories and 250 images in '10_food_classes_all_data/test/ramen'.
There are 0 directories and 250 images in '10_food_classes_all_data/test/steak'.
There are 10 directories and 0 images in '10_food_classes_all_data/train'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/chicken_wings'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/pizza'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/grilled_salmon'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/sushi'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/fried_rice'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/ice_cream'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/chicken_curry'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/hamburger'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/ramen'.
There are 0 directories and 750 images in '10_food_classes_all_data/train/steak'.
```


Take out all the tags:


```py
class_names = os.listdir("10_food_classes_all_data/train/")
train_dir = "10_food_classes_all_data/train/"
test_dir = "10_food_classes_all_data/test/"
```


At the same time, use tensorflow
[tensorflow.keras.preprocessing.image.ImageDataGenerator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator "ImageDataGenerator")
API processes and enhances the picture. In short, the API can effectively generate the picture to generate the picture based on the file directory, and enhance the picture according to the set operation.Note that `Data enhancement can only be used for training sets.


```py
train_datagen_augmented = ImageDataGenerator(rescale=1/255.,
rotation_range = 20, #r
shear_range = 0.2, #cut picture
zoom_range = 0.2, #Scaling picture
width_shift_range = 0.2, #left and right translation
height_shift_range = 0.2, #
horizontal_flip = true) #


Train_date days = Image Current (Rescale = 1/255.)


Test_date days = Image Current (Rescale = 1/255.)




# 生 生 生
train_data = train_datagen_augmented.flow_from_directory(train_dir,
target_size=(224,224),
batch_size=32,
shuffle=True)


test_data = test_datagen.flow_from_directory(test_dir,
target_size=(224,224),
batch_size=32
)
```


## 3 modeling


### 3.1 baseline model


First do a convolutional neural network as the baseline model:


```py


# Draw the training curve
def plot_loss_curves(history):
"""
Returns separate loss curves for training and validation metrics.
"""
loss = history.history['loss']
val_loss = history.history['val_loss']


accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']


epochs = range(len(history.history['loss']))


# Plot loss
plt.plot(epochs, loss, label='training_loss')
plt.plot(epochs, val_loss, label='val_loss')
plt.title('Loss')
plt.xlabel ('Epochs')
plt.legend ()


# Plot accuracy
plt.figure()
plt.plot(epochs, accuracy, label='training_accuracy')
plt.plot(epochs, val_accuracy, label='val_accuracy')
plt.title('Accuracy')
plt.xlabel ('Epochs')
plt.legend ()




# Modeling
tf.random.set_seed(42)
tf.keras.backend.clear_session()


cnn_model = tf.keras.models.Sequential([
layers.Conv2D(filters=10, kernel_size=(3,3), activation="relu",
input_shape=(224, 224, 3)),
layers.MaxPooling2D(pool_size=2),


layers.Conv2D(filters=10, kernel_size=(3,3), activation="relu"),
layers.MaxPooling2D(pool_size=2),


layers.Flatten(),
layers.Dropout(0.5),
layers.Dense(10, activation="softmax")
])


cnn_model.compile(loss=tf.keras.losses.CategoricalCrossentropy(),
optimizer=tf.keras.optimizers.Adam(),
steps_per_execution = 50,
metrics="accuracy")




def create_tensorboard_callback(dir_name, experiment_name):
log_dir = dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)
print(f"Saving tensorboard callback log file to {log_dir}")
return tensorboard_callback




tf_board_callback =  create_tensorboard_callback(dir_name="vision_model",
experiment_name="VGG_base")


history_cnn = cnn_model.fit(train_data,
steps_per_epoch=len(train_data),
epochs=5,
validation_data=test_data,
validation_steps=len(test_data),
callbacks=[tf_board_callback])


cnn_model.evaluate(test_data)
```


The output is as follows, the accuracy is poor and unsatisfactory:


```py
79/79 [==============================] - 12s 148ms/step - loss: 1.8068 - accuracy: 0.3852
[1.8068159818649292, 0.38519999384880066]
```


Check the training process, you can find that the curve trend is normal. If you deepen the model or have a longer training time, you should achieve better accuracy.


```py
plot_loss_curves(history_cnn)
```


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/cnn_loss.png"  />

<figcaption> Change of loss </figcaption>
</figure>


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/cnn_accuracy.png"  />

<figcaption> accuracy change </figcaption>
</figure>


### 3.2 Migration Learning


Another angle of improving model performance is to use migration learning.Migration learning will be used in other tasks that have already performed very well, applying it to its own tasks, usually better than building a model from zero, because its model architecture and training process are done.A lot of optimization.The number of use layers here is very deep and the performance is very good
[Xception](https://arxiv.org/abs/1610.02357, "Xception: Deep Learning with Depthwise Separable Convolutions")
Model.


```py
# Load the pre -trained xception model
base_model = tf.keras.applications.xception.Xception(weights='imagenet', include_top=False)
avg = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
output = tf.keras.layers.Dense(len(class_names), activation='softmax')(avg)
model = tf.keras.Model(inputs=base_model.input, outputs=output)


# Usually frozen the weight of the pre -training model, because they have undergone good training and are already optimized
for layer in base_model.layers:
layer.trainable = False


optimizer = tf.keras.optimizers.SGD(lr=0.2, momentum=0.9, decay=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])


epochs = 5
tf_board_callback_2 =  create_tensorboard_callback(dir_name="vision_model",
experiment_name="Xception")


history = model.fit(train_data, epochs=epochs, validation_data=test_data,
callbacks=[tf_board_callback_2])


model.evaluate(test_data)
```


The output is as follows, the performance dump a few streets on the baseline:


```py
79/79 [==============================] - 31s 390ms/step - loss: 0.5771 - accuracy: 0.8388
[0.5770677924156189, 0.8388000130653381]
```


Check the training process in Tensorboard:


```py
# The following command is only applicable to Google Colab
%load_ext tensorboard
%tensorboard --logdir="vision_model/Xception/20220522-120512/"
```


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/tensorboard.png"  />

<FIGCAPTION> Tensorboard Display Training Process </figCaption>
</figure>


At the same time, you can download the calculation diagram of the model in Tensorboard. It can be seen that the Xception is far more complicated than the baseline model, so it is not surprising that its performance far exceeds the baseline.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/xception_train.png"  />

<figcaption> Model Architecture </figcaption>
</figure>


## 4 Summary


This article covers important APIs related to TensorFlow with neural networks for picture classification tasks, such as `tensorflow.keras.preprocessing.image.imageDataGENERATOR`,` tensorboard callback` and how to load pre -training models.I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>