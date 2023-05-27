---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
---

# Customizing Models with tf.keras

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published: June 6th, 2021, Read Time: About 6 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/z2uBxwe8UNDXWMDNS_k-Gg)

## 1 Introduction

tf.keras provides many convenient APIs for building deep learning models. However, some situations require custom layers and models. In this article, we will focus on customizing models and use the customization methods in TensorFlow 2.x to provide more flexibility for the solution.

## 2 Custom Layers

### 2.1 Creating Layers without Weights

When custom layers do not require weights, `tf.keras.layers.Lambda` can be very convenient, as shown below:

```python
exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))
```

Then this custom layer can be used in the Sequential API and Functional API like other layers to build models. It can even be called like calling a Python function:

```python
print(exponential_layer(2.0).numpy())
```

Output:

```python
7.389056
```

### 2.2 Creating Layers with Weights

If you need to create layers with weights, it is usually to inherit the `tf.keras.layers.Layer` class and override the `__init__`, `build`, and `call` methods, as shown below:

```python
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

The custom layer can be called like the built-in layers in tf.keras:

```python
input_ = Input((1,))
output = Linear(units=1)(input_)
model = Model(input_, output)
model.compile(optimizer='Adam', loss="mse")
model.summary()
```

Output:

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

Please note that if you want to serialize the custom layer as part of the Functional API model, you need to implement the `get_config()` method. The `__init__()` method of the base Layer class accepts some keyword arguments, especially `name` and `dtype`. It is best to pass these arguments to the parent class in `__init__()` and include them in the layer's configuration, [as shown below]('https://www.tensorflow.org/guide/keras/custom_layers_and_models#%E5%8F%AF%E9%80%89%E6%8B%A9%E5%9C%A8%E5%B1%82%E4%B8%8A%E5%90%AF%E7%94%A8%E5%BA%8F%E5%88%97%E5%8C%96'):

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

If the behavior of the custom layer is different during training and inference, such as with Dropout or BatchNormalization layers, `training` parameters need to be added to the `call` function to distinguish the behavior of the model under different running states, as shown below:

```python
class CustomDropout(keras.layers.Layer):
    def __init__(self, rate, **kwargs):
        super(CustomDropout, self).__init__(**kwargs)
        self.rate = rate

    def call(self, inputs, training=None):
        if training:
            return tf.nn.dropout(inputs, rate=self.rate)
        return inputs
```

### 2.3 Customizing Losses and Metrics

When customizing losses, use labels and predicted values as parameters, and then use TensorFlow operators to calculate the loss for each instance.

```python
def huber_fn(y_true,y_pred):
  error=y_true-y_pred
  is_small_error=tf.abs(error)<1
  squared_loss=tf.square(error)/2
  linear_loss=tf.abs(error)-0.5

return tf.where(is_small_error,squared_loss,linear_loss)
```

When customizing evaluation metrics, you can inherit the `tf.keras.metrics.Metric` class and override the `__init__`, `update_state`, and `result` methods, [as shown in the example](https://tf.wiki/zh_hans/basic/models.html#id26):

```python
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

The `update_state()` method works when the instance of the custom evaluation metric class is called, receiving labels, predicted values, and other custom parameters in a batch to update defined variables. The `result()` method calculates and returns the final result, which is executed after the `update_state()` method.

## 3 Conclusion

The above examples introduce how to customize keras models, which can add flexibility to daily workflows. In practical work, you need to repeatedly scrutinize and ensure that there are no errors.

I hope this sharing will help you. Welcome to leave a message in the comment area for discussion!

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>