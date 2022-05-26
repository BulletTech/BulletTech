---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
---

# 使用tf.keras自定义模型

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/z2uBxwe8UNDXWMDNS_k-Gg)

## 1 前言

tf.keras提供了许多方便调用的API构建深度学习模型，但有些情况需要自定义层和模型，因此在这篇文章里，我们将着眼自定义模型，使用TensorFlow 2.X里的自定义方法为解决方案提供更多灵活性。

## 2 自定义层

### 2.1 创建没有权重的层

当自定义层无需权重时，使用`tf.keras.layers.Lambda`会非常方便，示例如下：

```python
exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))
```

然后这个自定义层可以像其他层一样在Sequential API和Functional API中使用以构建模型。甚至可以像调用Python函数一样调用它：

```Python
print(exponential_layer(2.0).numpy())
```

输出为：

```Python
7.389056
```

### 2.2 创建具有权重的层

如需创建具有权重的层，通常是继承`tf.keras.layers.Layer`类，并重写`__init__`、`build`和`call`三个方法，示例如下：

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

自定义的层可以像tf.keras内置的层一样被调用：

```Python
input_ = Input((1,))
output = Linear(units=1)(input_)
model = Model(input_, output)
model.compile(optimizer='Adam', loss="mse")
model.summary()
```

输出为：

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

请注意，如果要将自定义层作为Functional API模型的一部分进行序列化，需实现get_config()方法，基础Layer类的__init__()方法会接受一些关键字参数，尤其是name和dtype。最好将这些参数传递给__init__()中的父类，并将其包含在层配置中，[示例]('https://www.tensorflow.org/guide/keras/custom_layers_and_models#%E5%8F%AF%E9%80%89%E6%8B%A9%E5%9C%A8%E5%B1%82%E4%B8%8A%E5%90%AF%E7%94%A8%E5%BA%8F%E5%88%97%E5%8C%96' '可选择在层上启用序列化')如下：

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

如果在训练和推理阶段，自定义层的行为不同，比如Dropout或者BatchNormalization层，则需要在call函数里加入`training`参数来区分模型不同运行状态下的行为，示例如下：

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

### 2.3 自定义loss和metrics

自定义loss时，使用标签和预测值作为参数，然后用TensorFlow的算子计算每个实例的损失。

```python
def huber_fn(y_true,y_pred):
  error=y_true-y_pred
  is_small_error=tf.abs(error)<1
  squared_loss=tf.square(error)/2
  linear_loss=tf.abs(error)-0.5

return tf.where(is_small_error,squared_loss,linear_loss)
```

自定义评估指标时，可以继承`tf.keras.metrics.Metric`类，并重写`__init__`、`update_state`和`result`三个方法，[示例](https://tf.wiki/zh_hans/basic/models.html#id26 '简单粗暴Tensorflow 2.0')如下：

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

update_state()方法在调用自定义评价指标类的实例时起作用，它接收一个批次实例中标签、预测值和其他自定义的参数来更新定义的变量。result()方法则计算并返回最终的结果，它会在update_state()方法之后执行。

## 3 总结

上述例子介绍了如何自定义keras模型，能够为日常的工作流更添灵活性，实际工作中，还需反复推敲，确保正确无误。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
