---
template: overrides/blogs.html
tags:
  - machine learning
---

# Reflections on "Rules of Machine Learning" (Part 2)

!!! info
    Author: Void, published on 2021-07-22, time to read: about 10 minutes, link to WeChat public account article: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/eZqfAIiE9wP2M8x-7CE9-w)

## 1 Introduction

This is the second part of the reflection on "Rules of Machine Learning" by Martin Zinkevich, which mainly covers specific modeling aspects, including feature engineering, analysis, and optimization.

## 2 Feature Engineering

After the initial system is set up in stage one, the second stage is to add as many effective features as possible. At this point, improving the model performance is relatively easy.

```
Rule #16: Plan to launch and iterate.
```

Prepare well for continuous iteration.

```
Rule #17: Start with directly observed and reported features as opposed to learned features.
```

Start with simple and intuitive features. The so-called learned features can be scores from other models. Adding such features will increase dependency. If one day some model retires, this feature will not be available anymore. However, this does not mean that such features cannot be used at all.

```
Rule #18: Explore with features of content that generalize across contexts.
```

Use cross-scenario features. For example, customer data on Product A can be beneficial for modeling Product B. At the same time, this can also solve the cold start problem.

```
Rule #19: Use very specific features when you can.
```

If the data volume is large enough, use as many simple features as possible instead of a few complex features. Do not be afraid of using sparse ID features.

```
Rule #20: Combine and modify existing features to create new features in human-understandable ways.
```

Feature engineering should have a certain meaning. Discretizing continuous features or the interaction of categorical features should have some business meaning instead of being mixed up randomly. Feature combination can be tried with Shap. Shap can give the impact of feature interaction on label to guide feature combination.

```
Rule #21: The number of feature weights you can learn in a linear model is roughly proportional to the amount of data you have.
```

The number of features should be matched with the sample quantity (supported by statistical theory).

- Thousands of data correspond to dozens of features
- Tens of millions of data correspond to hundreds of thousands of features

It seems that it is off by two orders of magnitude.

```
Rule #22: Clean up features you are no longer using.
```

Remove unused features. If unnecessary, do not add entities. This also conforms to the principle of Occam's Razor. Removing such features can not only make the model more clean but also improve the model performance. In addition, features with too low coverage may not be unusable. If a feature has a coverage rate of only 1%, but all of them are positive samples, it can still be a very effective feature.

## 3 Human Analysis of Machine Learning Systems

```
Rule #23: You are not a typical end user.
```

As a model developer, you are not a truly objective end user. Let real end users or other colleagues check the model performance.

```
Rule #24: Measure the delta between models.
```

Compare the performance of new and old models. Generally speaking, we expect the performance of the new model to be better than that of the old model. Checking performance differences can give you insights into what has changed in the model.

```
Rule #25: When choosing models, utilitarian performance trumps predictive power.
```

When choosing models, the performance of utility metrics is more important than predictive power. For example, when we use the model score cutoff to reject bad transactions, the accuracy of sorting is more important than the predicted value itself. Often these two are consistent. But we can also adjust the model based on our specific needs, such as giving higher weights to samples with higher scores (higher ranking).

```
Rule #26: Look for patterns in the measured errors, and create new features.
```

Construct new features through case studies. Multi-similar features can be constructed, and then the model can select effective features.

```
Rule #27: Try to quantify observed undesirable behavior.
```

Quantify observed negative phenomena. For example, if you think that the sorting accuracy of the model is not enough, how to define the sorting accuracy? Only by providing clear quantitative indicators can further optimization be made.

```
Rule #28: Be aware that identical short-term behavior does not imply identical long-term behavior.
```

The effect of model test does not mean long-term generalization ability. It is a headache whether the model has really learned patterns or just overfitting the samples.

## 4 Differences Between Training and Online Launch

There are often differences between training and online launch, and the best or rare way is to monitor.

```
Rule #29: The best way to make sure that you train like you serve is to save the set of features used at serving time, and then pipe those features to a log to use them at training time.
```

The best method is to log real online data as training data. This can greatly reduce the differences between the two.

```
Rule