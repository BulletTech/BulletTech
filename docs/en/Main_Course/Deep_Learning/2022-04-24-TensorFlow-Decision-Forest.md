---
template: overrides/blogs.html
tags:
  -Deep Learning
  -tensorflow
---

# Use TensorFlow DECISION FORESTS to build a tree model

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-06-06, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-solid-Link:] (https://mp.weixin.qqqpom/s ?__biz=mzi4mjk3nzgxoq===2247485279&IDX=1&SN=D31A0146B9B82AD1E64C02F134382BDCE77D3D3D2E 8E5C3A8E4F6DA3019652A0A8FB3CF74D8E7527C944CE4866840B660BF & Token = 709422112 & Lang = zh_cn#RD)

## 1 Introduction

In -depth learning and traditional machine learning have always been excellent frameworks in their respective fields. If they build neural networks, they will basically choose to use TensorFlow and PyTorch.When dealing with table -type data in real work, the traditional tree model performance is still very strong.However, for a long time, the deep learning framework did not build a tree model until the appears of the `tensorFlow decision forests`.

`TensorFlow Decision Forests` provides a series of API -based models based on decision -making trees, such as classified regression trees (CART), random forests, gradients, etc., use the `TensorFlow Decision Forests`, you can use a paradigm like a neural network.Build a tree model.This article will be found!

## 2 Get data

As usual, first import dependencies and download data.Use a table type dataset here to predict the type of penguin.

`` `python
Import tensorFlow_Decision_Forests as tfdf

Import OS
import numpy as np
Import Pandas as PD
Import Tensorflow as tf
import math

# Download the dataset
! wget -q https://storage.googleapis.com/download.tensorflow.org/data/palmer_penguins/penguins.csv-o /TMP/penguins.CSV

# Load a dataset into a pandas dataframe.
dataset_df = pd.read_csv ("/tmp/penguins.csv"))

# Display the first 3 examples.
dataset_df.head (3)
`` `


| --- | --- | --- | --- | --- | --- | --- | --- |
| Adelie | Torgersen | 39.1 | 18.7 | 181.0 | 3750.0 | Male | 2007 |
| Adelie | Torgersen | 39.5 | 17.4 | 186.0 | 3800.0 | Female | 2007 |
| Adelie | Torgersen | 40.3 | 18.0 | 195.0 | 3250.0 | Female | 2007 |

Specify the labeling field and convert the tag category into integer data.

`` `python
label = "Species"

Classes = dataset_df [label] .unique (). Tolist ()
Print (F "Label Classes: {Classes}")

dataset_df [label] = dataset_df [label] .map (CLASSES.INDEX)
`` `

## 3 Divide and process data

Divide data into training sets and test sets:

`` `python
DEF SPLIT_DATASET (dataset, test_ratio = 0.30):
  "" "Splits a panda dataframe in two." "" "" "" "" "" "" "" "" "" "" "" "" ""
  test_indices = np.random.rand (len (dataset)) <test_ratio
  Return dataset [~ test_indices], dataset [test_indices]


Train_DS_PD, TEST_DS_PD = Split_dataset (dataset_df)
Print ("{} examples in trailing, {} examples for testing." Format (
    Len (Train_DS_PD), Len (TEST_DS_PD))))
`` `

And convert the `pandas dataframe` to` tensorflow dataset`, which is conducive to simplifying subsequent programs and improving efficiency.

`` `python
Train_ds = tfdf.keras.pd_dataframe_to_tf_dataset (train_ds_pd, label = label)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset (test_ds_pd, label = label)
`` `

At this step, you can train the data injection model.Different from the traditional machine learning framework, `tensorflow decision forests` has the following advantages for the realization of tree models:

-In automatically handle the variables of numerical and category types, no need to encode the category variables, nor does it need to be normalized for numerical variables.The algorithm can be handled well for the missing value!
-Surium is basically similar to other frameworks. At the same time, the default parameters can give good results in most cases.
-When training before training, no compile model is required, and no verification set is required during training. Verification set is only used to display performance indicators

Note that this does not mean that the use of the `tensorflow decision forests` can save all the feature engineering, but it does save a lot of time.

## 4 modeling

It is very similar to using the `TensorFlow Decision Forests` to build a tree model and use TensorFlow to build a neural network:

`` `python
#
Model = tfdf.kers.randomForestmodel ()

#
Model.fit (x = TRAIN_DS)

# 评 评
MODEL.COMPILE (Metrics = ["Accuracy"])
Evaluation = Model.evaluate (test_ds, return_dict = true)
Print ()

for name, value in event .Items ():
  Print (f "{name}: {value: .4f}")
`` `

The output is:

`` `python
1/1 [============================================================= =================================================================================================================================================================================== ====] -1S 706ms/STE -Loss -Loss: 0.0000E+00 -Accuracy:0.9608

loss: 0.0000
account: 0.9608
`` `

## 5 Visual Tree Model

`Tensorflow decision forests` provides native API visualization of trees. Here is a tree in the forest for display.

`` `python
With open ("plot.html", "w") as f:
  f.write (tfdf.model_plotter.plot_model (Model, Tree_idx = 0, Max_depth = 3)))

From ipython.display image iframe
Iframe (src = './Plot.html', width = 700, height = 600)
`` `

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/img/1_v/forestsviz.png"/>/>
  <figcaption> Visualized Tree </figcaption>
</Figure>

At the same time, there are many important information in the method of `Model.summary ()`, such as input features, characteristics importance, node information, etc. (limited space, do not start here).At the same time, the accuracy and losses in the training process can also be visually visual:

`` `Python
Import Matplotlib.pyplot as PLT

LOGS = MODEL.MAKE_INSPECTOR (). Training_logs ()

PLT.FIGURE (figsize = (12, 4))

PLT.SUBPLOT (1, 2, 1)
PLT.Plot
PLT.XLabel ("Number of Trees")
PLT.YLabel ("Accuracy (Out-OF-BAG)"))

PLT.SUBPLOT (1, 2, 2)
PLT.PLOT ([log.num_trees for log in logs], [log.evaluation.loss for log in logs])
PLT.XLabel ("Number of Trees")
PLT.YLabel ("Logloss (Out-OF-BAG)"))

plt.show ()
`` `

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/img/1_v/trainin_log.png"/>/>
  <figcaption> training process </figcaption>
</Figure>

## 6 Summary

`Tensorflow defision forests` reinforced the TensorFlow ecology, and provided new ideas for data scientists for modeling data.It is still in the initial stage (V0.2.3), but there are already many available high -quality APIs. More functions can be viewed [document] (https://www.tensorflow.org/decision_forests/api_docs/tfdf 'TensorFlow Decision Forests Document ').I hope this sharing will help you, please leave a message in the comment area!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>