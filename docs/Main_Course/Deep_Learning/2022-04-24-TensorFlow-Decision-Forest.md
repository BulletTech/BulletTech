---
template: overrides/blogs.html
---

# 使用TensorFlow Decision Forests构建树模型

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

一直以来深度学习和传统机器学习都有在各自领域出色的框架，如构建神经网络，基本上会选择使用TensorFlow和PyTorch。在现实工作中应对表格型数据时，传统的树模型表现仍然十分强劲。可是在很长一段时间里，深度学习框架并没有API构建树模型，直到`TensorFlow Decision Forests`的出现。

`TensorFlow Decision Forests`提供了一系列API构建基于决策树的模型，如分类回归树（CART），随机森林，梯度提升树等，使用`TensorFlow Decision Forests`，可以使用像构建神经网络一样的范式，构建树模型。本文将一探究竟！

## 2 获取数据

如往常一样，先导入依赖，并下载数据。在此使用一个表格型数据集预测企鹅的种类。

```python
import tensorflow_decision_forests as tfdf

import os
import numpy as np
import pandas as pd
import tensorflow as tf
import math

# Download the dataset
!wget -q https://storage.googleapis.com/download.tensorflow.org/data/palmer_penguins/penguins.csv -O /tmp/penguins.csv

# Load a dataset into a Pandas Dataframe.
dataset_df = pd.read_csv("/tmp/penguins.csv")

# Display the first 3 examples.
dataset_df.head(3)
```

|   species  |   island  |   bill_length_mm  |   bill_depth_mm  |   flipper_length_mm  |   body_mass_g  |   sex  |   year  |
|---|---|---|---|---|---|---|---|
|   Adelie  |   Torgersen  |   39.1  |   18.7  |   181.0  |   3750.0  |   male  |   2007  |
|   Adelie  |   Torgersen  |   39.5  |   17.4  |   186.0  |   3800.0  |   female  |   2007  |
|   Adelie  |   Torgersen  |   40.3  |   18.0  |   195.0  |   3250.0  |   female  |   2007  |

指定标签字段，并将标签类别转换为整型数据。

```python
label = "species"

classes = dataset_df[label].unique().tolist()
print(f"Label classes: {classes}")

dataset_df[label] = dataset_df[label].map(classes.index)
```

## 3 分割并处理数据

将数据分割成训练集和测试集：

```python
def split_dataset(dataset, test_ratio=0.30):
  """Splits a panda dataframe in two."""
  test_indices = np.random.rand(len(dataset)) < test_ratio
  return dataset[~test_indices], dataset[test_indices]


train_ds_pd, test_ds_pd = split_dataset(dataset_df)
print("{} examples in training, {} examples for testing.".format(
    len(train_ds_pd), len(test_ds_pd)))
```

并且将`Pandas DataFrame`转化为`TensorFlow Dataset`，利于简化后续的程序并提升效率。

```python
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=label)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_ds_pd, label=label)
```

到这一步即可把数据注入模型进行训练了。不同于传统的机器学习框架，`TensorFlow Decision Forests`对于树模型的实现有如下优点：

- 自动处理了数值型和类别型的变量，无需对类别型变量做编码，也无需对数值型变量做归一化。算法对于缺失值也能很好地处理！
- 超参数基本与其他框架类似，同时，默认参数在大多数情况下都能给出不错的结果。
- 训练前，无需compile模型，并且训练时不需要验证集，验证集仅用于展示性能指标

注意，这并不代表使用`TensorFlow Decision Forests`可以省去所有的特征工程，但它的确能节约很多时间。

## 4 建模

使用`TensorFlow Decision Forests`构建树模型和使用TensorFlow构建神经网络非常类似：

```python
# 构建随机森林
model = tfdf.keras.RandomForestModel()

# 训练模型
model.fit(x=train_ds)

# 评估模型
model.compile(metrics=["accuracy"])
evaluation = model.evaluate(test_ds, return_dict=True)
print()

for name, value in evaluation.items():
  print(f"{name}: {value:.4f}")
```

输出为：

```python
1/1 [==============================] - 1s 706ms/step - loss: 0.0000e+00 - accuracy: 0.9608

loss: 0.0000
accuracy: 0.9608
```

## 5 可视化树模型

`TensorFlow Decision Forests`提供了原生API对树进行可视化，在此选择森林里的一颗树进行展示。

```python
with open("plot.html", "w") as f:
  f.write(tfdf.model_plotter.plot_model(model, tree_idx=0, max_depth=3))

from IPython.display import IFrame
IFrame(src='./plot.html', width=700, height=600)
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/ForestsViz.png"  />
  <figcaption>可视化树</figcaption>
</figure>

同时在`model.summary()`方法里也有许多重要的信息，如输入特征、特征重要性、节点信息等（篇幅有限，在此不一一展开）。同时训练过程中的精度和损失也可以可视化：

```Python
import matplotlib.pyplot as plt

logs = model.make_inspector().training_logs()

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot([log.num_trees for log in logs], [log.evaluation.accuracy for log in logs])
plt.xlabel("Number of trees")
plt.ylabel("Accuracy (out-of-bag)")

plt.subplot(1, 2, 2)
plt.plot([log.num_trees for log in logs], [log.evaluation.loss for log in logs])
plt.xlabel("Number of trees")
plt.ylabel("Logloss (out-of-bag)")

plt.show()
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/Trainin_log.png"  />
  <figcaption>训练过程</figcaption>
</figure>

## 6 总结

`TensorFlow Decision Forests`对于TensorFlow的生态进行了补强，对于表格型数据的建模，给数据科学家们又提供了新的思路。其现在还处于初期阶段（v0.2.3），但已经有许多可用的高质量API，更多的功能可查看[文档](https://www.tensorflow.org/decision_forests/api_docs/python/tfdf 'TensorFlow Decision Forests文档')。希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
