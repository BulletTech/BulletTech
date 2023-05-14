---
template: overrides/blogs.html
tags:
  -Deep Learning
  -tensorflow
---

# Keras Introduction to various callbacks

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-06-06, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-solid-Link:] (https://mp.weixin.qqqpom/s ?__biz=mzi4mjk3nzgxoq==&mid=2247484578IDX=1&Sn=5459357289d011ac6aff47259731b&Chksm=eb9d6d6d6DCec0d8d8d8d8d8d8d8d8d8 96FF1149F89F4C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6C6BA

## 1 Introduction

In TensorFlow.keras, Callbacks can operate in the life cycle of the model of `` `Evaluate` and` Predict`. At present, Tensorflow.keras has built many types of callbacks for users to useThe visualization training process, error correction, preservation model Checkpoints, and generating Tensorboard.Through this article, let's learn how to use various callbacks in TensorFlow.keras, and how to customize callbacks.

## 2 Use CallBacks

The steps of using callbacks are very simple. First define the callbacks, and then pass the defined callbacks in the `Model.fit`,` Model.evaluate` and `Model.predict` to the parameter of the` callbacks` parameter.

Taking the most common `ModelCheckpoint` as an example, the use process is as follows:

`` `python
Elastic
MODEL_CHECKPOINT_CALLBACK = tf.keras.callbacks.modelcheckpoint (
    filepath = filepath,
    save_weights_only = true,
    Monitor = 'Val_accuracy',
    MODE = 'MAX')

Model.fit (x, y, callbacks = model_checkpoint_callback)
`` `

In this way, during model training, the model checkpoints will be stored in the corresponding location for follow -up use.In addition to ModelCheckpoint, in TensorFlow 2.0, there are many other types of callbacks for use, let us find out.

### 2.1 Earlystopping

This callback can monitor the setting indicators. During the training process, the evaluation index will no longer rise, and the training will end early to prevent the model from overfitting. The default parameters are as follows:

`` `python
tf.keras.callBacks.earlystopping (Monitor = 'Val_loss',
        min_delta = 0,
        patience = 0,
        Verbose = 0,
        MODE = 'Auto',
        baseline = None,
        restore_best_weights = false)
`` `

Each parameter:

-MONITOR: evaluation indicator of Callbacks monitoring.
-MIN_DELTA: The minimum measurement of the measurement indicator.
-Patience: When the evaluation indicators are not improved, the number of waiting epochs that is waiting will stop training after the number is not improved.
-Verbose: Whether to print a log.
-Mode: Set the mode of monitoring indicators, such as whether the monitoring index decreases, rises, or automatically infer according to the indicator name.
-Baseline: The benchmark of the monitoring index. When the model training result is not as good as the standard line, the training will stop.
-Restore_best_weights: Whether the EPOCH recovery model with the best training effect is set to False, it will restore the model weight recovery model from the last Step model.

### 2.2 LearningralscheDuler

This callback can adjust the learning rate during the model training process. Generally speaking, as the number of training times becomes more, appropriately reducing the learning rate is conducive to model convergence. Therefore, this callback needs to be used with a learning rate schedul.At the beginning of each EPOCH, the Schedule function will get the latest learning rate and use it in the current EPOCH:

`` `python
tf.keras.callBacks.learningraateScheduler (
    scheedule, VERBOSE = 0
Cure

# The scheduling function is to call the initial learning rate before 10 EPOCH, and then the learning rate is decreased in the index
DEF SCHEDULER (EPOCH, LR):
  if epoch <10:
    Return lr
  else:
    Return LR * tf.math.exp (-0.1)

Model = tf.keras.models.sequential ([tf.keras.layers.dense (10)])
MODEL.COMPILE (tf.keras.optimizers.sgd (), Loss = 'MSE')
callback = tf.keras.callbacks.learningratescheduler (scheduler)
history = Model.fit (np.arange (100) .Reshape (5, 20), np.zeros (5),
                    epochs = 15, callbacks = [callback], Verbose = 0)

`` `

### 2.3 ReducelronPlateau

Compared to LearninglateScheduler, ReducelronPlateau does not adjust the learning rate according to the pre -set scheduling, it will reduce the learning rate when the evaluation index stops raising.

`` `python
tf.keras.callBacks.ReducelronPlateau (
    Monitor = 'Val_loss', Factor = 0.1, Patient = 10, Verbose = 0,
    mode = 'auto', min_delta = 0.0001, cooldown = 0, min_lr = 0, ** kwargs
Cure
`` `

Important parameters:

-Factor: The degree of learning rate is reduced, new_lr = lr * factor.
-COOLDOWN: Epochs waiting for re -monitoring evaluation indicators.
-MIN_LR: The minimum learning rate is allowed.

### 2.4 Tensorboard

Tensorboard can easily display the model architecture and training process. This callback can generate a tensorboard log. When the training is over, you can view visualization results in Tensorboard.

`` `python
tf.keras.callbacks.Tensorboard (
    log_dir = 'LOGS', Histogram_freq = 0, Write_graph = TRUE,
    Write_images = false, write_Steps_per_SECOND = false, update_freq = 'Epoch',
    Profile_batch = 2, Embeddings_freq = 0, Embeddings_metadata = None, ** KWARGS
Cure
`` `

Important parameters:

-LOG_DIR: The path of the log output.
-Histogram_freq: Calculate the frequency of the activation function and the weight of the weight of the weight. If it is set to 0, the histogram is not calculated.
-WRITE_GRAPH: Whether to visualize images in Tensorboard.
-update_freq: The value is `BATCH` or` Epoch` or integer. After the specified process is over, the loss and evaluation indicators will be written into Tensorboard.If it is set to an integer, it means that the loss and evaluation indicators are written into Tensorboard after the number of sample training is set.

### 2.5 csvlogger

As the name suggests, this callback can write the training process into the CSV file.

`` `python
tf.keras.callbacks.csvlogger (
    Filename, sections = ',', append = false
Cure
`` `

Important parameters:

-Papend: Whether the existing files continue to write to the log.

### 2.6 Terminateonnan

Stop training when the loss becomes NAN.

`` `python
tf.keras.callbacks.terminateonnan ()
`` `

### 2.7 Custom Callback

In addition to the above callback, there are some callbacks to query [tensorflow official website] Using multipleWhen callbacks, you can use a list to pass multiple callbacks in, or use [tf.ots.callbacks.callbacklist] (https://www.tensorflow.org/api_docs/tf/callbacks/cs/cs/cs/c allbacklist 'tf.keras.callbacks.callbacklist ').In addition, you can also customize the callback. You need to inherit the method of `Keras.Callbacks.Callback`, and then rewrite the method of different training stages.

`` `python
Training_finished = false

class mycallback (TF.KERAS.Callbacks.callback):
  def on_train_end (seld, logs = none):
    Global Training_finished
    Training_finished = TRUE

Model = tf.keras.sequential ([tf.keras.layers.dense (1, input_shape = (1,))
MODEL.COMPILE (loss = 'Mean_squared_error')

          callbacks = [mycallback ()]))

Assert Training_finished == TRUE
`` `

## 3 Summary

This article summarizes a number of commonly used tf.keras.callbacks. In actual work, please use it on demand, and check the official documentation of tf.ots.callbacks to confirm the parameters.

I hope this sharing will help you, please leave a message in the comment area!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>