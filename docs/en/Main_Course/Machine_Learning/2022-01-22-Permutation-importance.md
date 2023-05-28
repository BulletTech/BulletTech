---
template: overrides/blogs.html
tags:
  - machine learning
---

# Permutation Importance for Feature Selection

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-06-06, Reading time: about 6 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485194&idx=1&sn=60a358eeed0c7fa7b2ebb362cce92a9b&chksm=eb90f47edce77d68bc54cd35d12a5530c9639250b19b469269f2e0559eeb81c5b2d0052e74a4&token=120973643&lang=zh_CN#rd)

## 1 Introduction

In previous articles, some common feature selection techniques have been introduced. In this article, we will continue to focus on this topic and explain a new method for assessing feature importance: Permutation Importance. Before continuing reading, it is recommended to review relevant previous knowledge:

- [Decision Tree Learning Notes](https://mp.weixin.qq.com/s/waV7HG3KWs-Qx574aUHj3Q)
- [How to Do Feature Selection](https://mp.weixin.qq.com/s/Cuw1ugpxm-5lF_rUkAu56Q)

## 2 Algorithm Deconstruction

Permutation Importance is suitable for tabular data, and its assessment of feature importance depends on the extent to which the model performance score decreases when the feature is randomly rearranged. Its mathematical expression can be represented as:

- Input: model m after training, training set (or validation set, or test set) D
- Performance score s of model m on dataset D
- For each feature j of dataset D
  - For each iteration k of K repeated experiments, randomly permute feature j to construct a contaminated dataset $Dc_{k,j}$
  - Calculate the performance score $s_{k,j}$ of model m on dataset $Dc_{k,j}$
  - Feature j's importance score $i_{j}$ can be expressed as

$$ i_{j} = s - \frac{1}{K}\sum_{k=1}^{K}s_{k,j} $$

## 3 Example Code

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.inspection import permutation_importance
diabetes = load_diabetes()
X_train, X_val, y_train, y_val = train_test_split(
    diabetes.data, diabetes.target, random_state=0)

model = Ridge(alpha=1e-2).fit(X_train, y_train)
model.score(X_val, y_val)


scoring = ['r2', 'neg_mean_absolute_percentage_error', 'neg_mean_squared_error']
# The scoring parameter can include multiple calculation indicators at the same time. This is more efficient than using permutation_importance repeatedly, because the predicted value can be used to calculate different indicators.
r_multi = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0, scoring=scoring)

for metric in r_multi:
    print(f"{metric}")
    r = r_multi[metric]
    for i in r.importances_mean.argsort()[::-1]:
        if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
            print(f"    {diabetes.feature_names[i]:<8}"
                  f"{r.importances_mean[i]:.3f}"
                  f" +/- {r.importances_std[i]:.3f}")

```

The output is:

```python
r2
  s5      0.204 +/- 0.050
  bmi     0.176 +/- 0.048
  bp      0.088 +/- 0.033
  sex     0.056 +/- 0.023
neg_mean_absolute_percentage_error
  s5      0.081 +/- 0.020
  bmi     0.064 +/- 0.015
  bp      0.029 +/- 0.010
neg_mean_squared_error
  s5      1013.903 +/- 246.460
  bmi     872.694 +/- 240.296
  bp      438.681 +/- 163.025
  sex     277.382 +/- 115.126
```

## 4 Conclusion

Compared with tree models, feature importance is usually judged based on the decrease in impurity, which is usually based on the `training set`. When the model is overfitting, the importance of features is misleading. In this case, seemingly important features may not have satisfactory predictive power for new data encountered by the model online.

At the same time, feature importance based on reduction in impurity is easily affected by high-cardinality features, so numerical variables often rank higher. In contrast, Permutation Importance has no bias towards model features and is not limited to specific model types, so it has a wide range of applications. Please note that if the features have strong multicollinearity, it is recommended to take only one important feature. The method can be viewed in this [example](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-multicollinear-py 'Permutation Importance with Multicollinear or Correlated Features').

At the same time, `Scikit Learn` also provides an intuitive [example](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py 'Permutation Importance vs Random Forest Feature Importance (MDI)') to demonstrate the difference between feature importance based on impurity reduction and Permutation Importance.

Hope this sharing is helpful to you, and welcome to leave comments for discussion!