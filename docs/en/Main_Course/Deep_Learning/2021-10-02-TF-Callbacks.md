---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
---

# Keras各种Callbacks介绍

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484578&idx=1&sn=54593557289d011ac6aff472597a731b&chksm=eb90f7d6dce77ec0d896ff1149f89f4c6d9bab7753be123ef269aa781a3ae88012bfa90ce2e0&token=221998215&lang=zh_CN#rd)

## 1 Introduction


In TensorFlow.keras, Callbacks can operate in the life cycle of the model of `` `Evaluate` and` Predict`. At present, Tensorflow.keras has built many types of callbacks for users to useThe visualization training process, error correction, preservation model Checkpoints, and generating Tensorboard.Through this article, let's learn how to use various callbacks in TensorFlow.keras, and how to customize callbacks.


## 2 Use CallBacks


The steps of using callbacks are very simple. First define the callbacks, and then pass the defined callbacks in the `Model.fit`,` Model.evaluate` and `Model.predict` to the parameter of the` callbacks` parameter.


Taking the most common `ModelCheckpoint` as an example, the use process is as follows:


```python
...
model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
filepath=filePath,
save_weights_only=True,
monitor='val_accuracy',
mode='max')


model.fit(x, y, callbacks=model_checkpoint_callback)
```


In this way, during model training, the model checkpoints will be stored in the corresponding location for follow -up use.In addition to ModelCheckpoint, in TensorFlow 2.0, there are many other types of callbacks for use, let us find out.


### 2.1 EarlyStopping


This callback can monitor the setting indicators. During the training process, the evaluation index will no longer rise, and the training will end early to prevent the model from overfitting. The default parameters are as follows:


```python
tf.keras.callbacks.EarlyStopping(monitor='val_loss',
min_delta = 0,
patience=0,
verbose=0,
fashion = 'car',
baseline=None,
restore_best_weights=False)
```


Each parameter:


-MONITOR: evaluation indicator of Callbacks monitoring.
-MIN_DELTA: The minimum measurement of the measurement indicator.
-Patience: When the evaluation indicators are not improved, the number of waiting epochs that is waiting will stop training after the number is not improved.
-Verbose: Whether to print a log.
-Mode: Set the mode of monitoring indicators, such as whether the monitoring index decreases, rises, or automatically infer according to the indicator name.
-Baseline: The benchmark of the monitoring index. When the model training result is not as good as the standard line, the training will stop.
-Restore_best_weights: Whether the EPOCH recovery model with the best training effect is set to False, it will restore the model weight recovery model from the last Step model.


### 2.2 LearningRateScheduler


This callback can adjust the learning rate during the model training process. Generally speaking, as the number of training has increased, appropriately reducing the learning rate is conducive to model convergence in the global optimal point. Therefore, this callback needs to be used with a learning rate schedul.At the beginning of each EPOCH, the Schedule function will get the latest learning rate and use it in the current EPOCH:


```python
tf.keras.callbacks.LearningRateScheduler(
schedule, verbose=0
)


# The scheduling function is to call the initial learning rate before 10 EPOCH, and then the learning rate is decreased in the index
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


Compared to LearninglateScheduler, ReducelronPlateau does not adjust the learning rate according to the pre -set scheduling, it will reduce the learning rate when the evaluation index stops raising.


```python
tf.keras.callbacks.ReduceLROnPlateau(
monitor='val_loss', factor=0.1, patience=10, verbose=0,
mode='auto', min_delta=0.0001, cooldown=0, min_lr=0, **kwargs
)
```


Important parameters:


-Factor: The degree of learning rate is reduced, new_lr = lr * factor.
-COOLDOWN: Epochs waiting for re -monitoring evaluation indicators.
-MIN_LR: The minimum learning rate is allowed.


### 2.4 TensorBoard


Tensorboard can easily display the model architecture and training process. This callback can generate a tensorboard log. When the training is over, you can view visualization results in Tensorboard.


```python
tf.keras.callbacks.TensorBoard(
log_dir='logs', histogram_freq=0, write_graph=True,
write_images=False, write_steps_per_second=False, update_freq='epoch',
profile_batch=2, embeddings_freq=0, embeddings_metadata=None, **kwargs
)
```


Important parameters:


-LOG_DIR: The path of the log output.
-Histogram_freq: Calculate the frequency of the activation function and the weight of the weight of the weight. If it is set to 0, the histogram is not calculated.
-WRITE_GRAPH: Whether to visualize images in Tensorboard.
-update_freq: The value is `BATCH` or` Epoch` or integer. After the specified process is over, the loss and evaluation indicators will be written into Tensorboard.If it is set to an integer, it means that the loss and evaluation indicators are written into Tensorboard after the number of sample training is set.


### 2.5 CSVLogger


As the name suggests, this callback can write the training process into the CSV file.


```python
tf.keras.callbacks.CSVLogger(
filename, separator=',', append=False
)
```


Important parameters:


-Papend: Whether the existing files continue to write to the log.


### 2.6 TerminateOnNaN


Stop training when the loss becomes NAN.


```python
tf.keras.callbacks.TerminateOnNaN()
```


### 2.7 Custom Callback


In addition to the above callback, there are some callbacks to query
[TensorFlow Official Website] BacksEnter, or use [tf.keras.callbacks.callbacklist] (https://www.tensorflow.org/api_docs/python/tf/callbacks/callbacklist 'tf.kerbacks .Callbacklist '))
EssenceIn addition, you can also customize the callback. You need to inherit the method of `Keras.Callbacks.Callback`, and then rewrite the method of different training stages.


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


## 3 Summary


This article summarizes a number of commonly used tf.keras.callbacks. In actual work, please use it on demand, and check the official documentation of tf.ots.callbacks to confirm the parameters.


I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>