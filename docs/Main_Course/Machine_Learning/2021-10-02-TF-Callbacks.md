---
template: overrides/blogs.html
---

# Keras各种Callbacks介绍

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

在tensorflow.keras中，callbacks能在`fit`、`evaluate`和`predict`过程中加入伴随着模型的生命周期运行，目前tensorflow.keras已经构建了许多种callbacks供用户使用，用于防止过拟合、可视化训练过程、纠错、保存模型checkpoints和生成TensorBoard等。这篇文章，我们来了解一下如何使用tensorflow.keras里的各种callbacks，以及如何自定义callbacks。

## 2 使用callbacks

使用callbacks的步骤很简单，先定义callbacks，然后在`model.fit`、`model.evaluate`和`model.predict`中把定义好的callbacks传到`callbacks`参数里即可。

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

这样在模型训练时，就会将模型checkpoints存储在对应的位置供后续使用。除了ModelCheckpoint，在Tensorflow 2.0中，还有许多其他类型的callbacks供使用，让我们一探究竟。

### 2.1 EarlyStopping

这个callback能监控设定的评价指标，在训练过程中，评价指标不再上升时，训练将会提前结束，防止模型过拟合，其默认参数如下：

```python
tf.keras.callbacks.EarlyStopping(monitor='val_loss',
        min_delta=0,                                 patience=0,                                 
        verbose=0,     
         mode='auto',                                 baseline=None,                                 
         restore_best_weights=False)
```

其中各个参数：

- monitor：callbacks监控的评价指标。
- min_delta：计作指标提升的最小度量。
- patience：当评价指标没有提升时，等待的epochs数量，超过此数没有提升后训练将停止。
- verbose：是否打印日志。
- mode：设定监控指标的模式，如监控指标是否下降、上升或者根据指标名字自动推断。
- baseline：监控指标的基准，当模型训练结果不及标准线，训练将停止。
- restore_best_weights：是否从训练效果最好的epoch恢复模型，如果设置成False，将从最后一个step的模型权重恢复模型。

### 2.2 LearningRateScheduler

这个callback能在模型训练过程中调整学习率，通常而言，随着训练次数的变多，适当地降低学习率有利于模型收敛在全局最优点，因此这个callback需要搭配一个学习率调度器使用，在每个epoch开始时，schedule函数会获取最新的学习率并用在当前的epoch中：

```python
tf.keras.callbacks.LearningRateScheduler(
    schedule, verbose=0
)

# 调度函数在10个epoch前调用初始学习率，随后学习率呈指数下降
def scheduler(epoch, lr):
  if epoch < 10:
    return lr
  else:
    return lr * tf.math.exp(-0.1)

model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
model.compile(tf.keras.optimizers.SGD(), loss='mse')
callback = tf.keras.callbacks.LearningRateScheduler(scheduler)
history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
                    epochs=15, callbacks=[callback], verbose=0)

```

### 2.3 ReduceLROnPlateau

相比于LearningRateScheduler，ReduceLROnPlateau不是按照预先设定好的调度调整学习率，它会在评价指标停止提升时降低学习率。

```python
tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss', factor=0.1, patience=10, verbose=0,
    mode='auto', min_delta=0.0001, cooldown=0, min_lr=0, **kwargs
)
```

其中重要参数：

- factor：学习率降低的程度，new_lr = lr * factor。
- cooldown：重新监控评价指标前等待的epochs。
- min_lr：允许的学习率最小值。

### 2.4 TensorBoard

TensorBoard能很方便地展示模型架构、训练过程，这个callback能生成TensorBoard的日志，当训练结束后可以在TensorBoard里查看可视化结果。

```python
tf.keras.callbacks.TensorBoard(
    log_dir='logs', histogram_freq=0, write_graph=True,
    write_images=False, write_steps_per_second=False, update_freq='epoch',
    profile_batch=2, embeddings_freq=0, embeddings_metadata=None, **kwargs
)
```

其中重要参数：

- log_dir：日志输出的路径。
- histogram_freq：计算激活函数和权重直方图的频率，如果设置为0，则不计算直方图。
- write_graph：是否在TensorBoard中可视化图像。
- update_freq：`batch`或`epoch`或整数，将在指定的过程结束后将损失和评价指标写入TensorBoard。如果设置为整数，则意味着在设定数量的样本训练完后将损失和评价指标写入TensorBoard。

### 2.5 CSVLogger

顾名思义，这个callback能将训练过程写入CSV文件。

```python
tf.keras.callbacks.CSVLogger(
    filename, separator=',', append=False
)
```
其中重要参数：
- append：是否接着现有文件继续写入日志。

### 2.6 TerminateOnNaN

在损失变为NaN时停止训练。

```python
tf.keras.callbacks.TerminateOnNaN()
```

### 2.7 自定义callback

除了上述callback外，还有一些callback可以查询[TensorFlow官网]('https://www.tensorflow.org/api_docs/python/tf/keras/callbacks' 'tf.keras.callbacks')，在使用多个callbacks时，可以使用列表将多个callbacks传入、或者使用[tf.keras.callbacks.CallbackList](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/CallbackList 'tf.keras.callbacks.CallbackList')。除此之外，也可以自定义callback，需要继承`keras.callbacks.Callback `，然后重写在不同训练阶段的方法。

```python
training_finished = False

class MyCallback(tf.keras.callbacks.Callback):
  def on_train_end(self, logs=None):
    global training_finished
    training_finished = True

model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
model.compile(loss='mean_squared_error')
model.fit(tf.constant([[1.0]]), tf.constant([[1.0]]),
          callbacks=[MyCallback()])

assert training_finished == True
```

## 3 总结

本文总结了若干常用的tf.keras.callbacks，实际工作中，请按需使用，并且查看tf.keras.callbacks的官方文档确认参数取值。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
