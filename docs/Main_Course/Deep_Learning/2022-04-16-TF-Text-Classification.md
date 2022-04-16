---
template: overrides/blogs.html
---

# 使用TensorFlow进行文本分类

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485273&idx=1&sn=d672fbcc65edeb115f628ad231caeca8&chksm=eb90f42ddce77d3b680b48c9cda52db5f96e3d3a64fc1bf94537dae7efa1a9f8908016572e35&token=200682583&lang=zh_CN#rd)


## 1 前言

在自然语言处理中，文本分类是非常普遍的应用，本文将介绍使用TensorFlow开发基于嵌入（Embedding）的文本分类模型，由于TensorFlow的API变化迅速且兼容性感人，因此本文均使用的截至2022年4月16日最新版的TensorFlow(tf)及相关库，主要包括：`TensorFlow（v2.8.0）`，`TensorFlow Datasets（tfds v4.0.1）`和`TensorFlow Text（tf_text v2.8.1）`，如遇bug，请首先检查TensorFlow相关库的版本。此工作流主要使用的API有：

- tf.strings
- tfds
- tf_text
- tf.data.Dataset
- tf.keras (Sequential & Functional API)


## 2 获取数据

TensorFlow Datasets（tfds）里含有非常多的[示例数据](https://www.tensorflow.org/datasets 'TensorFlow Datasets数据集')用于研究试验，本文使用经典的电影评论数据，进行情感二分类任务的研究。首先使用tfds的API直接加载数据，结果将存在一个[tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset 'tf.data.Dataset')对象中。

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

BATCH_SIZE = 32

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

返回值为：

```
20000
5000
```

使用如下方法查看一条示例数据:

```python
for data, label in  train_ds.take(1):
  print(type(data))
  print('Text:', data.numpy())
  print('Label:', label.numpy())
```

返回值为:

```
<class 'tensorflow.python.framework.ops.EagerTensor'>
Text: b"This was an absolutely terrible movie. Don't be lured in by Christopher Walken or Michael Ironside. Both are great actors, but this must simply be their worst role in history. Even their great acting could not redeem this movie's ridiculous storyline. This movie is an early nineties US propaganda piece. The most pathetic scenes were those when the Columbian rebels were making their cases for revolutions. Maria Conchita Alonso appeared phony, and her pseudo-love affair with Walken was nothing but a pathetic emotional plug in a movie that was devoid of any real meaning. I am disappointed that there are movies like this, ruining actor's like Christopher Walken's good name. I could barely sit through it."
Label: 0
```

## 3 文本预处理

该小节使用tf_text和tf.stings的处理文本的API对数据进行处理，tf.data.Dataset能够很方便地将对应的函数映射到数据中，推荐学习和使用。

### 3.1 转换文字大小写

分类任务中字符大小写对模型预测没有贡献，因此对dataset使用`map`操作把所有字符转为小写，务必注意tf.data.Dataset里的数据格式。

```python
train_ds = train_ds.map(lambda text, label: (tf_text.case_fold_utf8(text), label))
val_ds = val_ds.map(lambda text, label: (tf_text.case_fold_utf8(text), label))
```

### 3.2 文本格式化

该步骤对文本使用正则表达式进行格式化处理，如标点前后加上空格，利于后续步骤使用空格分词。

```python
str_regex_pattern = [("[^A-Za-z0-9(),!?\'\`]", " "),("\'s", " \'s",) ,("\'ve", " \'ve"),("n\'t", " n\'t"),("\'re", " \'re"),("\'d", " \'d")
,("\'ll", " \'ll"),(",", " , "),("!", " ! "),("\(", " \( "),("\)", " \) "),("\?", " \? "),("\s{2,}", " ")]

for pattern, rewrite in str_regex_pattern:
  train_ds = train_ds.map(lambda text, label: (tf.strings.regex_replace(text, pattern=pattern, rewrite=rewrite), label))
  val_ds = val_ds.map(lambda text, label: (tf.strings.regex_replace(text, pattern=pattern, rewrite=rewrite), label))

```

### 3.3 构建词表

使用训练集构造词表（注意不要使用验证集或者测试集，会导致信息泄露），该步骤将字符映射到相应的索引，利于将数据转化为模型能够进行训练和预测的格式。

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

返回值显示，高频使用的词都是英语中常见的字符：

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

也可以使用图表直观地展示每个词的使用频率，这一步有利于帮助选择词表的大小。

```python
fig = px.scatter(x=range(len(d_view)), y=[cnt for cnt, word in d_view])
fig.show()
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/vocab_plot.png"  />
  <figcaption>词的使用频率分布</figcaption>
</figure>

由图可见，在七万多个字符中，许多字符出现的频率极低，因此选择词表大小为两万。

### 3.4 构建词表映射

使用TensorFlow的`tf.lookup.StaticVocabularyTable`对字符进行映射，其能将字符映射到对应的索引上，并使用一个简单的样本进行测试。

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

输出为：

```
array([20000,  2065, 14207,   618])
```

接下来就可以将文本映射到索引上了，构造一个函数用于转化，并将它作用到数据集上：

```Python
def text_index_lookup(text, label):
  tokenized = tokenizer.tokenize(text)
  vectorized = table.lookup(tokenized)
  return vectorized, label

train_ds = train_ds.map(text_index_lookup)
val_ds = val_ds.map(text_index_lookup)
```

### 3.5 配置数据集

借助tf.data.Dataset的`cache`和`prefetch`API，能够有效提高性能，`cache`方法将数据加载在内存中用于快速读写，而`prefetch`则能够在模型预测时同步处理数据，提高时间利用率。


```Python
AUTOTUNE = tf.data.AUTOTUNE

def configure_dataset(dataset):
  return dataset.cache().prefetch(buffer_size=AUTOTUNE)

train_ds = configure_dataset(train_ds)
val_ds = configure_dataset(val_ds)
```

文本长短不一，但神经网络需要输入数据具有固定的维度，因此对数据进行padding确保长度一致，并分批次。

```python
BATCH_SIZE = 32
train_ds = train_ds.padded_batch(BATCH_SIZE  )
val_ds = val_ds.padded_batch(BATCH_SIZE  )
```

### 3.6 处理测试集

用于验证模型性能的测试集也可以使用同样的方式处理，确保模型可以正常预测：

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

## 4 建立模型

### 4.1 使用Sequential API构建卷积神经网络

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

# 在SGD中使用momentum将显著提高收敛速度
loss = losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)

model.compile(loss=loss, optimizer=optimizer, metrics='accuracy')

print(model.summary())
```

输出为：

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

 global_max_pooling1d (Globa  (None, 128)              0         
 lMaxPooling1D)                                                  

 dropout (Dropout)           (None, 128)               0         

 dense (Dense)               (None, 2)                 258       

=================================================================
Total params: 2,622,178
Trainable params: 2,622,178
Non-trainable params: 0
_________________________________________________________________
```

接下来即可训练、评估模型：

```Python
# early stopping reduces the risk of overfitting
early_stopping = tf.keras.callbacks.EarlyStopping(patience=10)
epochs = 100
history = model.fit(x=train_ds, validation_data=val_ds,epochs=epochs, callbacks=[early_stopping])

loss, accuracy = model.evaluate(test_ds)

print("Loss: ", loss)
print("Accuracy: {:2.2%}".format(accuracy))
```

考虑到模型结构简单，效果还可以接受：

```
782/782 [==============================] - 57s 72ms/step - loss: 0.4583 - accuracy: 0.8678
Loss:  0.45827823877334595
Accuracy: 86.78%
```

### 4.2 使用Functional API构建双向LSTM

步骤与使用Sequential API类似，但Functional API更为灵活。

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

输出为：

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

同样地，对模型进行训练与预测：


```Python
history_2 = lstm_model.fit(x=train_ds, validation_data=val_ds, epochs=epochs, callbacks=[early_stopping])

loss, accuracy = lstm_model.evaluate(test_ds)

print("Loss: ", loss)
print("Accuracy: {:2.2%}".format(accuracy))
```

考虑到模型结构简单，效果还可以接受：

```
782/782 [==============================] - 84s 106ms/step - loss: 0.4105 - accuracy: 0.8160
Loss:  0.4105057716369629
Accuracy: 81.60%
```

## 5 总结

关于文本分类，还有许多新的技术可以尝试，上述工作流中也还有许多决策可以做试验（炼丹），本文旨在使用最新的TensorFlow API过一遍文本分类任务中的重要知识点和常用API，实际工作中仍有许多地方可以优化。希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
