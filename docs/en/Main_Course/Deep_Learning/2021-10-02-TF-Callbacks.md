# Introduction to various Keras Callbacks

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-06-06, Reading time: about 6 minutes, WeChat Official Account Article Link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484578&idx=1&sn=54593557289d011ac6aff472597a731b&chksm=eb90f7d6dce77ec0d896ff1149f89f4c6d9bab7753be123ef269aa781a3ae88012bfa90ce2e0&token=221998215&lang=zh_CN#rd)

## 1 Introduction

In tensorflow.keras, callbacks can run along with the model's life cycle during `fit`, `evaluate` and `predict` processes. At present, tensorflow.keras has built many types of callbacks available for users to prevent overfitting, visualize the training process, debug, save model checkpoints, and generate TensorBoard, etc. Through this article, we will learn how to use various callbacks in tensorflow.keras and how to customize callbacks.

## 2 Using Callbacks

Using callbacks is very simple. First, define the callbacks, then pass the defined callbacks to the `callbacks` parameter in `model.fit()`, `model.evaluate()`, and `model.predict()`.

Take the most common `ModelCheckpoint` as an example. The usage process is as follows:

```python
...
model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=filePath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max')

model.fit(x, y, callbacks=model_checkpoint_callback)
```

In this way, when the model is trained, the model checkpoints will be stored in the corresponding position for later use. In addition to ModelCheckpoint, there are many other types of callbacks available for use in TensorFlow 2.0. Let's explore them.

### 2.1 EarlyStopping

This callback can monitor the specified evaluation metric. During the training process, when the evaluation metric stops increasing, the training will end early to prevent overfitting. Its default parameters are as follows:

```python
tf.keras.callbacks.EarlyStopping(monitor='val_loss',
        min_delta=0,
        patience=0,
        verbose=0,
        mode='auto',
        baseline=None,
        restore_best_weights=False)
```

The parameters are as follows:

- monitor: the evaluation metric monitored by callbacks.
- min_delta: the smallest metric improvement that will be counted.
- patience: the number of epochs to wait before stopping training when the evaluation metric stops improving.
- verbose: whether to print logs.
- mode: the mode of monitoring metrics, such as whether to monitor if the metric is decreasing, increasing, or automatically inferred based on the metric name.
- baseline: the baseline of the monitored metric. When the result of the model training is below the standard line, the training will stop.
- restore_best_weights: whether to restore the model from the epoch with the best training effect. If set to False, the model weights will be restored from the last step.

### 2.2 LearningRateScheduler

This callback can adjust the learning rate during the model training process. Generally, the learning rate can be appropriately reduced as the number of training increases to help the model converge to the global optimum. Therefore, this callback needs to be used together with a learning rate scheduler. At the beginning of each epoch, the schedule function will obtain the latest learning rate and use it in the current epoch:

```python
tf.keras.callbacks.LearningRateScheduler(
    schedule, verbose=0
)

# The scheduling function calls the initial learning rate before 10 epochs, and then the learning rate decreases exponentially
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

Compared with LearningRateScheduler, ReduceLROnPlateau does not adjust the learning rate according to the pre-set schedule. It reduces the learning rate when the evaluation metric stops improving.

```python
tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss', factor=0.1, patience=10, verbose=0,
    mode='auto', min_delta=0.0001, cooldown=0, min_lr=0, **kwargs
)
```

Important parameters are:

- factor: the degree of learning rate reduction, new_lr = lr * factor.
- cooldown: the number of epochs to wait before monitoring the evaluation metric again.
- min_lr: the minimum allowed learning rate.

### 2.4 TensorBoard

TensorBoard can conveniently display the model architecture and the training process. This callback can generate TensorBoard logs, and you can view the visualization results in TensorBoard after the training is completed.

```python
tf.keras.callbacks.TensorBoard(
    log_dir='logs', histogram_freq=0, write_graph=True,
    write_images=False, write_steps_per_second=False, update_freq='epoch',
    profile_batch=2, embeddings_freq=0, embeddings_metadata=None, **kwargs
)
```

Important parameters are:

- log_dir: the path to the log output.
- histogram_freq: the frequency of calculating the activation function and weight histograms. If set to 0, the histograms will not be calculated.
- write_graph: whether to visualize the graph in TensorBoard.
- update_freq: a string that can be 'batch', 'epoch', or an integer. Loss and evaluation metrics will be written to TensorBoard after the specified processing completes. If set to an integer, it means that the loss and evaluation metrics will be written to TensorBoard after the specified number of samples have been trained.
- write_images: whether to write weight histograms and other variables as images.
- write_steps_per_second: whether to write the number of steps per second during processing.
- profile_batch: the batch for profiling. The default value is 2, and -1 means that all batches will be profiled.

### 2.5 CSVLogger

As the name suggests, this callback can write the training process to a CSV file.

```python
tf.keras.callbacks.CSVLogger(
    filename, separator=',', append=False
)
```

Important parameters:

- append: whether to continue writing logs to existing files.

### 2.6 TerminateOnNaN

Stop training when the loss becomes NaN.

```python
tf.keras.callbacks.TerminateOnNaN()
```

### 2.7 Custom Callback

In addition to the above callbacks, there are other callbacks available on the [TensorFlow official website]('https://www.tensorflow.org/api_docs/python/tf/keras/callbacks' 'tf.keras.callbacks'). When using multiple callbacks, you can pass multiple callbacks into a list, or use [tf.keras.callbacks.CallbackList](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/CallbackList 'tf.keras.callbacks.CallbackList'). In addition, you can also customize callbacks, which requires inheriting `keras.callbacks.Callback` and then overriding methods at different training stages.

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

## 3 Conclusion

This article summarizes some commonly used tf.keras.callbacks. In actual work, please use them as needed and check the official documentation of tf.keras.callbacks to confirm the parameter values.
 
Hope this sharing is helpful to you, and welcome to leave a comment in the comment section to discuss!