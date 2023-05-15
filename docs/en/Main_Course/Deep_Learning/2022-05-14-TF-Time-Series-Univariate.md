---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - time series
---

# 使用TensorFlow进行单变量时间序列预测

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485305&idx=1&sn=b8a2cf6c598ed9cf06a8950e892edc93&chksm=eb90f40ddce77d1bebf7d5703bf298c87692fd275731ac9bc1238996937d3da42f274ad85f22&token=709422112&lang=zh_CN#rd)

## 1 Introduction


This article will use TensorFlow to solve the problem of time sequence prediction. There is a very detailed but lengthy TensorFlow official website
[Tutorial] (https://www.tensorflow.org/tutorials/structured_data/time_series "time Series foreasting")))))))
Therefore, this article will peel the cocoon and pump the cocoon, and use an easy -to -understand method to spend a single variable time sequence predicting the core content.


## 2 Bitcoin price data set


### 2.1 Get Data


This article uses Bitcoin historical price data (October 2013 to May 2021) for prediction. Please note that this article does not constitute investment suggestions!


```python
!wget https://raw.githubusercontent.com/mrdbourke/tensorflow-deep-learning/main/extras/BTC_USD_2013-10-01_2021-05-18-CoinDesk.csv


import pandas as pd
import matplotlib.pyplot as plt
Import us
import tensorflow as tf
from tensorflow.keras as layers


df = pd.read_csv("/content/BTC_USD_2013-10-01_2021-05-18-CoinDesk.csv",
parse_dates=["Date"],
index_col=["Date"]) # Parse the date column


df.tail()
```


Return as:


| Date | Currency | Closing Price (USD) | 24h Open (USD) | 24h High (USD) | 24h Low (USD) |
|---:|---:|---:|---:|---:|---:|
| 2021-05-14 | BTC | 49764.132082 | 49596.778891 | 51448.798576 | 46294.720180 |
| 2021-05-15 | BTC | 50032.693137 | 49717.354353 | 51578.312545 | 48944.346536 |
| 2021-05-16 | BTC | 47885.625255 | 49926.035067 | 50690.802950 | 47005.102292 |
| 2021-05-17 | BTC | 45604.615754 | 46805.537852 | 49670.414174 | 43868.638969 |
| 2021-05-18 | BTC | 43144.471291 | 46439.336570 | 46622.853437 | 42102.346430 |


The closing price is here to predict:


```python
bitcoin_prices = pd.DataFrame(df["Closing Price (USD)"]).rename({"Closing Price (USD)":"Price"},axis=1)
bitcoin_prices.head()
```


| Date | Price |
|---:|---:|
| 2013-10-01 | 123.65499 |
| 2013-10-02 | 125.45500 |
| 2013-10-03 | 108.58483 |
| 2013-10-04 | 118.67466 |
| 2013-10-05 | 121.33866 |


View the price trend of Bitcoin through the chart:


```python
plt.plot(bitcoin_prices["Price"])
plt.ylabel("Bitcoin price")
plt.xlabel("Date")
```


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/Bitcoin_price.png"  />

<figcaption> Bitcoin price trend </figcaption>
</figure>




### 2.2 Making time window


The expected data format is `
[0,1,2,3,4,5,6] -> [7] ``, even if the price of the past seven days is predicted to the next day.Here, the [TimeSeries_dataset_from_Array] provided by TensorFlow (https://www.tensorflow.org/api_docs/python/tims/timeSeries_from_array "TI Meseries_dataset_from_array "))
The API is divided into the window.


```python


timesteps = bitcoin_prices.index.to_numpy()
prices = bitcoin_prices["Price"].to_numpy()


Horizon = 1 # Predict the price of the next day
Window_size = 7 # Based on the price of the past 7 days


input_data = prices[:-HORIZON]
targets = prices[WINDOW_SIZE:]
dataset = tf.keras.preprocessing.timeseries_dataset_from_array(
input_data, targets, sequence_length=WINDOW_SIZE)
for batch in dataset:
inputs, targets = batch
assert np.array_equal(inputs[0], prices[:WINDOW_SIZE])
assert np.array_equal(targets[0], prices[WINDOW_SIZE])


print(f"First Input:{inputs[0]}, Target:{targets[0]}")
print(f"Second Input:{inputs[1]}, Target:{targets[1]}")


break
```


Back to the following, the data is correctly transformed into an expected format.


```python
First Input:[123.65499 125.455   108.58483 118.67466 121.33866 120.65533 121.795  ], Target:123.033
Second Input:[125.455   108.58483 118.67466 121.33866 120.65533 121.795   123.033  ], Target:124.049
```


### 2.3 Data


Use time to divide the training set and verification set. Only the example does not leave the test set, and the actual on -demand operation can be operated on demand.


```python
# tf.keras.preprocessing.timeseries_dataset_from_array returns BatcheD DataSet, so first of the Unbatch to facilitate dividing data data
dataset = dataset.unbatch()


test_split = 0.2
split_index = int(len(list(dataset)) * (1-test_split))


# After the division is split, then divide the BATCH to add one dimension, otherwise it will not be able to meet the model data dimension requirements
train_dataset = dataset.take(split_index).batch(batch_size=32)
test_dataset = dataset.skip(split_index).batch(batch_size=32)
```


## 3 modeling


This article does not pursue the ultimate prediction accuracy, so only uses the full connection layer to build a model, the code is as follows:


```python
tf.random.set_seed(42)
tf.keras.backend.clear_session()


# 1. Build a model
model = tf.keras.models.Sequential(
[
layers.Input(WINDOW_SIZE),
layers.Dense(128, activation="relu"),
layers.Dense(HORIZON, activation="linear")
]
, name="model_dense_base")


# 2. Compile model
model.compile(loss='mae',
optimizer=tf.keras.optimizers.Adam(),
metrics=['mae'])




# Create callback to save the best model checkpoint
def create_model_checkpoint(model_name, save_path="model_checkpoint"):
return tf.keras.callbacks.ModelCheckpoint(filepath=os.path.join(save_path, model_name),
verbose=0,
save_best_only=True)


# 3. Training model
model.fit( train_dataset,
epochs=100,
verbose=0,
validation_data=test_dataset,
callbacks=[create_model_checkpoint(model_name=model.name)]
)


```


Load the best models back to evaluate:


```python
model = tf.keras.models.load_model("model_checkpoint/model_dense_base")
model.evaluate(test_dataset)
```


The return is as follows, and the average absolute error (MAE) shows that the predicted price average and the real price difference is more than 700 US dollars.


```python
18/18 [==============================] - 1s 6ms/step - loss: 759.4327 - mae: 759.4327
[759.4326782226562, 759.4326782226562]
```


Considering that the model structure is very simple, there is room for improvement in the result. Optimization is optimized according to this process, it can be predicted more accurately.


## 4 Summary


This article made a benchmark for a single -variable time sequence prediction task. Among them, TensorFlow's `tf.ots.preprocessing.timeSeries_dataset_from_array`api simplifies the work of many processing time windows. After that Essence


## 5 Related reading materials


-
[Forecasting: Principles and Practice](https://otexts.com/fpp3/index.html)


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>