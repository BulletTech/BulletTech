---
template: overrides/blogs.html
tags:
  - machine learning
---

# Tips for Tuning Neural Networks

!!! info
    Author: Void, publish date: 2021-09-10, reading time: approximately 10 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484538&idx=1&sn=ae97eac88e44ae8b2f0466cf09e606c0&chksm=eb90f70edce77e1852aaf09ccca473b088b91d870f63c326166f7921d02ae7bb97e614b491ad&scene=178&cur_album_id=2045821482966024195#rd)

## 1 Introduction

Recently, I learned some tips for tuning neural networks from a Zhihu expert and found a blog post by deep learning expert Andrej Kapathy, "A Recipe for Training Neural Networks". Combining these articles with my own experiences, I would like to share some small tips for tuning neural networks.

## 2 Loss Curve Analysis

With visualization tools like Tensorboard and MLflow, the loss curve during training is easy to observe. The shape of the curve can often intuitively reflect the status of model training.

- Typically, the loss curve drops rapidly at the beginning and gradually levels off. If the curve is close to linear, the learning rate may be too small and the loss drop is insufficient.
- If the curve fluctuates too much, it may be due to a small batch size. The batch size is not always better when larger. When the batch size is small, the gradient direction calculated for each batch is not so accurate, and the variation between batches is larger, which may lead to escaping from the saddle point. The batch size can be adjusted as a hyperparameter. Empirically, the batch size can be the square root of the data size.
- If there is a large difference between the training set and validation set curves, the model may be overfitting the training set. Conversely, if the difference is too small, the model may be underfitting.
- The point where the loss is the minimum is not necessarily the optimal point for the evaluation index. For example, in a binary classification problem, the point with the minimum loss is not necessarily the point with the maximum AUC. An effective method is to print the model performance for each epoch.
- In actual usage, I have also encountered the situation where the validation loss rises all the way, but strangely, the selected model performs well on the test set, and it does not seem to be caused by overfitting. This phenomenon has also been [discussed](https://www.zhihu.com/question/318399418/answer/1202932315) on Zhihu, and the consensus is that the validation loss does not completely reflect the quality of the final model.

## 3 Learning Rate Adjustment

For neural networks, adjusting the learning rate has a high priority in tuning. The order of tuning can be learning rate, epoch number, batch size, and learning rate decay parameter.

- Warm up can be used to adjust the learning rate.
- The learning rate decay parameter often varies with different models and tasks.
- The parameter search is generally performed in 10-fold intervals.

## 4 Dropout Layer

The dropout layer can effectively reduce overfitting. On the other hand, it can also be considered as a way of model ensemble, which is recommended for use.

## 5 Optimizer

The Adam optimizer is a stable optimizer for parameters, including inappropriate learning rates.

## 6 Ensemble

We can even use different random number seeds to ensemble models.

## 7 Swish Activation Function

The Swish activation function has been proposed for a long time, but it frequently appears in high-scoring solutions on Kaggle recently. Its form is: f(x) = x · sigmoid(x), which is a smooth and non-monotonic function.  
In its paper, the author points out that the Swish activation function is superior to other activation functions, ReLU, etc., when the number of layers in the neural network is over 40. In shallow neural networks, whether it improves the model result still needs our own experimentation.

## 8 Batch Normalization

During normalization with batch normalization, each independent sample sees information from other samples in the same batch, which has a certain regularization effect.  
The zero-mean also makes the input in the saturation region of the activation function, accelerating the convergence speed.

## 9 Summary

Tuning has scientific and artistic elements. In actual usage, you may want to try the tips above. Some tips may be suitable for your model and task, helping your model perform better.

