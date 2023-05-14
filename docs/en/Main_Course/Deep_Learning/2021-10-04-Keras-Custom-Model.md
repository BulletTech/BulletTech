---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
---

# 使用tf.keras自定义模型

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/z2uBxwe8UNDXWMDNS_k-Gg)

## 1 Introduction


TF.KERAS provides many APIs that are convenient for calling to build deep learning models, but in some cases, custom layers and models need to be customized. Therefore, in this article, we will focus on custom models.The solution provides more flexibility.


## 2 custom layer


### 2.1 Create a layer without weight


When the custom layer does not require weight, it is very convenient to use `tf.keras.Layers.lambda`. The example is as follows:


```python
exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))
```


Then this custom layer can be used to build a model in the Sequeential API and Functional API like other layers.You can even call it like calling the Python function:


```Python
print(exponential_layer(2.0).numpy())
```


The output is:


```Python
7.389056
```


### 2.2 Create a heavy layer


If you need to create a heavy layer, it is usually inherited the three methods of inheriting the three methods of `TF.KERAS.Layers.Layer`, and rewrite the three methods of` __init__`, `built` and` call`. The example is as follows:


```Python
class Linear(keras.layers.Layer):
def __init__(self, units=32):
super(Linear, self).__init__()
self.units = units


def build(self, input_shape):
self.w = self.add_weight(
shape=(input_shape[-1], self.units),
initializer="random_normal",
trainable=True,
)
self.b = self.add_weight(
shape=(self.units,), initializer="random_normal", trainable=True
)


def call(self, inputs):
return tf.matmul(inputs, self.w) + self.b
```


The custom layer can be called like tf.keras built -in layers:


```Python
input_ = Input((1,))
output = Linear(units=1)(input_)
model = Model(input, output)
model.compile(optimizer='Adam', loss="mse")
model.summary()
```


The output is:


```python
Model: "model_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_2 (InputLayer)         [(None, 1)]               0
_________________________________________________________________
linear_1 (Linear)            (None, 1)                 2
=================================================================
Total params: 2
Trainable params: 2
Non-trainable params: 0
_________________________________________________________________
```


Please note that if you want to serialize a custom layer as a part of the Functional API model, you need to implement the get_config () method. The __init __ () method of the basic layer class will accept some keyword parameters, especially name and dtype.It is best to pass these parameters to the parent class in __init __ () and include it in the layer configuration,
[Example] ('https://www.tensorflow.org/guide/keras/custom_layers_and_models #%E5%8F%AF%E9%89%8b%A9C%A8%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1%E5%B1 Because82%E4%B8%8A%E5%90%AF%E7%94%A8%E5%BA%8F%E5%97%E5%8C%96 ''
as follows:


```python
class Linear(keras.layers.Layer):
def __init__(self, units=32, **kwargs):
super(Linear, self).__init__(**kwargs)
self.units = units


def build(self, input_shape):
self.w = self.add_weight(
shape=(input_shape[-1], self.units),
initializer="random_normal",
trainable=True,
)
self.b = self.add_weight(
shape=(self.units,), initializer="random_normal", trainable=True
)


def call(self, inputs):
return tf.matmul(inputs, self.w) + self.b


def get_config(self):
config = super(Linear, self).get_config()
config.update({"units": self.units})
return config


```


If in the training and reasoning phase, the behavior of the custom layer is different. For example, the Dropout or BatchNormAlization layer needs to add the `Training` parameter to the class to distinguish the behavior of different operating conditions in the call function. The example is as follows:


```Python
class CustomDropout(keras.layers.Layer):
def __init__(self, rate, **kwargs):
super(CustomDropout, self).__init__(**kwargs)
self.rate = rate


def call(self, inputs, training=None):
if training:
return tf.nn.dropout(inputs, rate=self.rate)
return inputs
```


### 2.3 Custom Loss and Metrics


When custom Loss, use the label and predictive value as a parameter, and then calculate the loss of each instance with the operator of TensorFlow.


```python
def huber_fn(y_true,y_pred):
Error = y_tue-y_pred
is_small_error=tf.abs(error)<1
squared_loss=tf.square(error)/2
linear_loss=tf.abs(error)-0.5


return tf.where(is_small_error,squared_loss,linear_loss)
```


When customized evaluation indicators, you can inherit the three methods of `tf.keras.metrics.metric`, and rewrite the three methods:
[Example] (https://tf.wiki/zh_hans/basic/models.html#id26 'Simple and rude TensorFlow 2.0')
as follows:


```Python
class SparseCategoricalAccuracy(tf.keras.metrics.Metric):
def __init__(self):
super().__init__()
self.total = self.add_weight(name='total', dtype=tf.int32, initializer=tf.zeros_initializer())
self.count = self.add_weight(name='count', dtype=tf.int32, initializer=tf.zeros_initializer())


def update_state(self, y_true, y_pred, sample_weight=None):
values = tf.cast(tf.equal(y_true, tf.argmax(y_pred, axis=-1, output_type=tf.int32)), tf.int32)
self.total.assign_add(tf.shape(y_true)[0])
self.count.assign_add(tf.reduce_sum(values))


def result(self):
return self.count / self.total
```


The update_state () method works when calling the instance of the custom evaluation index class. It receives the definition variables in a batch instance label, predictive value, and other custom parameters.The result () method is calculated and returned the final result, which will be executed after the update_state () method.


## 3 Summary


The above example introduces how to customize the keras model, which can add flexibility to the daily workflow. In actual work, it is necessary to repeatedly be considered to ensure correctly.


I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>