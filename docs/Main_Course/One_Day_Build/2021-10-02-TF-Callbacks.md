---
template: overrides/blogs.html
---

# Keras各种Callbacks介绍

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

在tensorflow.keras中，Callbacks能在`fit`、`evaluate`和`predict`过程中加入伴随着模型的生命周期运行，目前tensorflow.keras已经构建了许多种Callbacks供用户使用，用于防止过拟合、可视化训练过程、纠错、保存模型checkpoints和生成TensorBoard等。这篇文章，我们来了解一下如何使用tensorflow.keras里的各种Callbacks，以及如何自定义Callbacks。

## 2 使用Callbacks

使用Callbacks的步骤很简单，先定义Callbacks，然后在`model.fit`、`model.evaluate`和`model.predict`中把定义好的Callbacks传到`callbacks`参数里即可。

以最常见的`ModelCheckpoint`为例，使用过程如下示例：

```python
...
model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=filePath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max')

model.fit(x, y, callbacks=model_checkpoint_callback)
```

这样在模型训练时，就会将模型checkpoints存在对应的位置供后续使用。除了ModelCheckpoint，在Tensorflow 2.0中，还有许多其他类型的callbacks供使用，让我们一探究竟。

### 2.1


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
