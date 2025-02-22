---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - nlp
---

# Text Classification with TensorFlow

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-06-06，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485273&idx=1&sn=d672fbcc65edeb115f628ad231caeca8&chksm=eb90f42ddce77d3b680b48c9cda52db5f96e3d3a64fc1bf94537dae7efa1a9f8908016572e35&token=200682583&lang=zh_CN#rd)


## 1 Introduction


In natural language processing, text classification is a very common application. This article will introduce the use of TensorFlow to develop text classification models based on embedded. Because the API of TensorFlow has changed rapidly and compatible, this article is used in this article to 4 4 of 2022 4On the 16th, the latest version of TensorFlow (TF) and related libraries mainly includes: `tensorflow (v2.8.0)`, `tensorflow datasets (TFDS v4.0.1)` and `tensorFlow text (tf_text v2.8.1)` `BUG, first check the version of the TensorFlow related library.The main APIs used in this workflow are:


- tf.strings
- tfds
- tf_text
- tf.data.Dataset
- tf.keras (Sequential & Functional API)




## 2 Get data


TensorFlow DataSets (TFDS) contains a lot
[Example data] (https://www.tensorflow.org/datasets 'tensorflow datasets data set') is used for research trials. This article uses classic movie review data to conduct research on emotional dual -class tasks.First use the TFDS API to load the data directly. As a result, there will be a [tf.data.dataSet] (https://www.tersorflow.org/api_docs/python/data/dataSet 'tf.data.dataSet')
In the object.


```python
import collections
import pathlib


import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization


import tensorflow_datasets as tfds
import tensorflow_text as tf_text


import plotly.express as px
import matplotlib.pyplot as plt




# Training set.
train_ds = tfds.load(
'imdb_reviews',
split='train[:80%]',
shuffle_files=True,
as_supervised=True)


# Validation set - a tf.data.Dataset object
val_ds = tfds.load(
'imdb_reviews',
split='train[80%:]',
shuffle_files=True,
as_supervised=True)




# Check the count of records
print(train_ds.cardinality().numpy())
print(val_ds.cardinality().numpy())
```


The return value is:


```
20000
5000
```


Use the following method to view a sample data:


```python
for data, label in  train_ds.take(1):
print(type(data))
print('Text:', data.numpy())
print('Label:', label.numpy())
```


The return value is:


```
<class 'tensorflow.python.framework.ops.EagerTensor'>
Text: b"This was an absolutely terrible movie. Don't be lured in by Christopher Walken or Michael Ironside. Both are great actors, but this must simply be their worst role in history. Even their great acting could not redeem this movie's ridiculous storyline. This movie is an early nineties US propaganda piece. The most pathetic scenes were those when the Columbian rebels were making their cases for revolutions. Maria Conchita Alonso appeared phony, and her pseudo-love affair with Walken was nothing but a pathetic emotional plug in a movie that was devoid of any real meaning. I am disappointed that there are movies like this, ruining actor's like Christopher Walken's good name. I could barely sit through it."
Label: 0
```


## 3 Text Pre -processing


This section uses the API of TF_TEXT and TF.STINGS processing text to process the data. TF.Data.DataSet can easily map the corresponding functions into the data, recommended learning and use.


### 3.1 Conversion text


The characters in the classification task have not contributed to the model prediction of the model. Therefore, using the `map` operation to the DataSet to turn all the characters into a lowercase, be sure to pay attention to the data format in tf.data.dataSet.


```python
train_ds = train_ds.map(lambda text, label: (tf_text.case_fold_utf8(text), label))
val_ds = val_ds.map(lambda text, label: (tf_text.case_fold_utf8(text), label))
```


### 3.2 Text Format


This step is formatted by the regular expression of the text, such as adding spaces before and after the punctuation, which is conducive to subsequent steps to use spaces.


```python
str_regex_pattern = [("[^A-Za-z0-9(),!?\'\`]", " "),("\'s", " \'s",) ,("\'ve", " \'ve"),("n\'t", " n\'t"),("\'re", " \'re"),("\'d", " \'d")
,("\'ll", " \'ll"),(",", " , "),("!", " ! "),("\(", " \( "),("\)", " \) "),("\?", " \? "),("\s{2,}", " ")]


for pattern, rewrite in str_regex_pattern:
train_ds = train_ds.map(lambda text, label: (tf.strings.regex_replace(text, pattern=pattern, rewrite=rewrite), label))
val_ds = val_ds.map(lambda text, label: (tf.strings.regex_replace(text, pattern=pattern, rewrite=rewrite), label))


```


### 3.3 Build a watch table


Use the training set constructor (be careful not to use the verification or test set, which will lead to information leakage). This step is to map the character to the corresponding index, which is conducive to the transformation of the data into a model for the model that can be trained and predictable.


```python
# Do not use validation set as that will lead to data leak
train_text = train_ds.map(lambda text, label: text)


tokenizer = tf_text.WhitespaceTokenizer()


unique_tokens = collections.defaultdict(lambda: 0)
sentence_length =  []
for text in train_text.as_numpy_iterator():
tokens = tokenizer.tokenize(text).numpy()
sentence_length.append(len(tokens))
for token in tokens:
unique_tokens[token] += 1


# check out the average sentence length -> ~250 tokens
print(sum(sentence_length)/len(sentence_length))


# print 10 most used tokens - token, frequency
d_view = [ (v,k) for k,v in unique_tokens.items()]
d_view.sort(reverse=True)
for v,k in d_view[:10]:
print("%s: %d" % (k,v))
```


The return value shows that the words used in high -frequency are common characters in English:


```
b'the': 269406
b',': 221098
b'and': 131502
b'a': 130309
b'of': 116695
b'to': 108605
b'is': 88351
b'br': 81558
b'it': 77094
b'in': 75177
```


You can also use the chart to visually display the frequency of each word, which is conducive to helping the size of the choice.


```python
fig = px.scatter(x=range(len(d_view)), y=[cnt for cnt, word in d_view])
fig.show()
```


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/vocab_plot.png"  />

<FIGCAPTION> Frequency distribution of words </figcaption>
</figure>


As can be seen from the figure, among more than 70,000 characters, many characters appear very low, so the choice of vocabulary is 20,000.


### 3.4 Construction of Word Map


Use TensorFlow's `tf.lookup.StaticVocabularTable` to map the characters, which can map characters to the corresponding index and test with a simple sample.


```python
keys = [token for cnt, token in d_view][:vocab_size]
values = range(2, len(keys) + 2)  # Reserve `0` for padding, `1` for OOV tokens.


num_oov_buckets =1


# Note: must assign the key_dtype and value_dtype when the keys and values are Python arrays
init = tf.lookup.KeyValueTensorInitializer(
keys= keys,
values= values,
key_dtype=tf.string, value_dtype=tf.int64)


table = tf.lookup.StaticVocabularyTable(
init,
num_oov_buckets=num_oov_buckets)


# Test the look up table with sample input
input_tensor = tf.constant(["emerson", "lake", "palmer", "king"])
print(table[input_tensor].numpy())
```


The output is:


```
array([20000,  2065, 14207,   618])
```


Next, you can map the text to the index, construct a function for transformation, and use it to the data set:


```Python
def text_index_lookup(text, label):
tokenized = tokenizer.tokenize(text)
vectorized = table.lookup(tokenized)
return vectorized, label


train_ds = train_ds.map(text_index_lookup)
val_ds = val_ds.map(text_index_lookup)
```


### 3.5 Configuration Data set


With the help of TF.Data.DataSet's `Cache` and` PreFETCH`api, it can effectively improve performance. The `Cache` method loads data in memory to quickly read and write, while` prefetch` can process data synchronously when model predictions, Improve time utilization.




```Python
AUTOTUNE = tf.data.AUTOTUNE


def configure_dataset(dataset):
return dataset.cache().prefetch(buffer_size=AUTOTUNE)


train_ds = configure_dataset(train_ds)
val_ds = configure_dataset(val_ds)
```


The text is different, but the neural network needs to enter the data with a fixed dimension. Therefore, the padding of the data ensures that the length is consistent and in batches.


```python
BATCH_SIZE = 32
train_ds = train_ds.padded_batch(BATCH_SIZE  )
val_ds = val_ds.padded_batch(BATCH_SIZE  )
```


### 3.6 Treatment Test set


The test set used to verify the performance of the model can also be processed in the same way to ensure that the model can be predicted normally:


```Python
# Test set.
test_ds = tfds.load(
'imdb_reviews',
split='test',
# batch_size=BATCH_SIZE,
shuffle_files=True,
as_supervised=True)


test_ds = test_ds.map(lambda text, label: (tf_text.case_fold_utf8(text), label))


for pattern, rewrite in str_regex_pattern:
test_ds = test_ds.map(lambda text, label: (tf.strings.regex_replace(text, pattern=pattern, rewrite=rewrite), label))


test_ds = test_ds.map(text_index_lookup)
test_ds = configure_dataset(test_ds)
test_ds = test_ds.padded_batch(BATCH_SIZE  )
```


## 4 Establish a model


### 4.1 Use Sequential API to build convolutional neural networks


```Python
vocab_size += 2 # 0 for padding and 1 for oov token


def create_model(vocab_size, num_labels, dropout_rate):
model = tf.keras.Sequential([
tf.keras.layers.Embedding(vocab_size, 128, mask_zero=True),


tf.keras.layers.Conv1D(32, 3, padding="valid", activation="relu", strides=1),
tf.keras.layers.MaxPooling1D(pool_size=2),


tf.keras.layers.Conv1D(64, 4, padding="valid", activation="relu", strides=1),
tf.keras.layers.MaxPooling1D(pool_size=2),


tf.keras.layers.Conv1D(128, 5, padding="valid", activation="relu", strides=1),
tf.keras.layers.GlobalMaxPooling1D( ),


tf.keras.layers.Dropout(dropout_rate),


tf.keras.layers.Dense(num_labels)
])
return model


tf.keras.backend.clear_session()
model = create_model(vocab_size=vocab_size, num_labels=2, dropout_rate=0.5)


#Momentum in SGD will significantly increase the convergence speed
loss = losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)


model.compile(loss=loss, optimizer=optimizer, metrics='accuracy')


print(model.summary())
```


The output is:


```
Model: "sequential"
_________________________________________________________________
Layer (type)                Output Shape              Param #
=================================================================
embedding (Embedding)       (None, None, 128)         2560256


conv1d (Conv1D)             (None, None, 32)          12320


max_pooling1d (MaxPooling1D  (None, None, 32)         0
)


conv1d_1 (Conv1D)           (None, None, 64)          8256


max_pooling1d_1 (MaxPooling  (None, None, 64)         0
1D)


conv1d_2 (Conv1D)           (None, None, 128)         41088


globalmaxpooling1d (Global (None, 128) 0
MaxPooling1D)


dropout (Dropout)           (None, 128)               0


dense (Dense)               (None, 2)                 258


=================================================================
Total params: 2,622,178
Trainable params: 2,622,178
Non-trainable params: 0
_________________________________________________________________
```


Next, you can train and evaluate the model:


```Python
# early stopping reduces the risk of overfitting
early_stopping = tf.keras.callbacks.EarlyStopping(patience=10)
epochs = 100
history = model.fit(x=train_ds, validation_data=val_ds,epochs=epochs, callbacks=[early_stopping])


loss, accuracy = model.evaluate(test_ds)


print("Loss: ", loss)
print("Accuracy: {:2.2%}".format(accuracy))
```


Considering that the model structure is simple, the effect is acceptable:


```
782/782 [==============================] - 57s 72ms/step - loss: 0.4583 - accuracy: 0.8678
Loss:  0.45827823877334595
Accuracy: 86.78%
```


### 4.2 Use Functional API to build a two -way LSTM


Steps are similar to using Sequential API, but Functional API is more flexible.


```Python
input = tf.keras.layers.Input([None] )
x = tf.keras.layers.Embedding(
input_dim=vocab_size,
output_dim=128,
# Use masking to handle the variable sequence lengths
mask_zero=True)(input)


x = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64))(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dropout(dropout_rate)(x)
output = tf.keras.layers.Dense(num_labels)(x)


lstm_model = tf.keras.Model(inputs=input, outputs=output, name="text_lstm_model")


loss = losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)


lstm_model.compile(loss=loss, optimizer=optimizer, metrics='accuracy')


lstm_model.summary()
```


The output is:


```
Model: "text_lstm_model"
_________________________________________________________________
Layer (type)                Output Shape              Param #
=================================================================
input_5 (InputLayer)        [(None, None)]            0


embedding_5 (Embedding)     (None, None, 128)         2560256


bidirectional_4 (Bidirectio  (None, 128)              98816
nal)


dense_4 (Dense)             (None, 64)                8256


dropout_2 (Dropout)         (None, 64)                0


dense_5 (Dense)             (None, 2)                 130


=================================================================
Total params: 2,667,458
Trainable params: 2,667,458
Non-trainable params: 0
_________________________________________________________________
```


Similarly, train and predict the model:




```Python
history_2 = lstm_model.fit(x=train_ds, validation_data=val_ds, epochs=epochs, callbacks=[early_stopping])


loss, accuracy = lstm_model.evaluate(test_ds)


print("Loss: ", loss)
print("Accuracy: {:2.2%}".format(accuracy))
```


Considering that the model structure is simple, the effect is acceptable:


```
782/782 [==============================] - 84s 106ms/step - loss: 0.4105 - accuracy: 0.8160
Loss:  0.4105057716369629
Accuracy: 81.60%
```


## 5 Summary


Regarding text classification, there are many new technologies to try. There are also many decisions in the above workflow to test (alchemy). This article aims to use the latest TensorFlow API to pass the important knowledge points and commonly used API in text classification tasks and commonly used APIs in text classification tasks.There are still many places that can be optimized in actual work.I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>