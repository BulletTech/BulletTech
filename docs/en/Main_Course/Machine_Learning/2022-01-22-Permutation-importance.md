---
template: overrides/blogs.html
tags:
  -Machine Learning
---

#The feature selection Permutation Importance

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-06-06, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-solid-Link:] (https://mp.weixinin.qqqpom/s/s?_biz=mzi4mjk3nzgxoq===2247485194&IDX=1&Sn=60a358eeed0c7b2ebb362a9b&Chksm=eDce77d68bc 54CD35D12A5530C9639250B19B469269F2E0559EEB81C5B2D0052e74a4 & Token = 120973643 & Lang = zh_cn#RD)


## 1 Introduction

The previous article mentioned some commonly used feature selection techniques. This article continues to study this topic to explain a new method of checking feature importance: Permutation Importance.Before reading, you can read the relevant previous review:

- [Decision Tree Learning Notes] (https://mp.weixin.qq.com/s/wav7hg3kws-qx574auhj3q)
- [How to choose feature selection] (https://mp.weixin.qq.com/s/cuw1ugpxm-5LF_RUKAU56q)

## 2 algorithm deconstruction

Permutation Importation is suitable for table data, and its judgment of feature importance depends on the degree of decline of the model performance score after the characteristics are randomly discharged.Its mathematical expression can be expressed as:

-Enter: Model M after training, training set (or verification set, or test set) D
-The performance score of Model M on Data Set D S
-Ad the features of data set D.
  -S for each iteration of K in the K sub -repeat experiment, randomly arranges characteristic J to construct a contaminated data set $ dc_ {k, j} $
  -Ac calculating model m in the dataset $ DC_ {k, j} $ performance score $ s_ {k, j} $
  -The importance scores of feature J $ i_ {j} $ can be recorded as

$o I_ {j} = s - \ frac {1} {k} \ sum_ {k = 1}^{k} s_ {k, j} $o

## 3 sample code

`` `python
From Sklearn.datases Import Load_diabetes
From Sklearn.model_selection Import Train_Test_Split
From Sklearn.Linear_model Import Ridge
diabetes = load_diabetes ()
X_train, x_val, y_train, y_val = train_test_split (
    Diabetes.data, Diabetes.Target, RANDOM_STATE = 0)

Model = Ridge (alpha = 1E-2) .fit (x_train, y_train)
Model.score (X_VAL, Y_VAL)


scoring = ['r2', 'neg_mean_absolute_percentage_error', 'neg_mean_squared_error']
# Scoring parameters can add multiple calculation indicators at the same time, so that it is more efficient to use Permutation_importance, because the predictable value can be used to calculate different indicators to calculate different indicators
R_multi = Permutation_importance (Model, X_VAL, Y_VAL, N_Repeats = 30, RANDOM_STATE = 0, Scoring = Scoring)

For Metric in R_Multi:
    Print (f "{metric}")
    r = r_multi [metric]
    for I in R.importances_mean.argsort () [::-1]:
        if r.importances_mean [i] - 2 * r.importances_std [i]> 0: 0:
            Print (f "{diabetes.feature_names [i]: <8}"
                  f "{r.importances_mean [i] :. 3F}"
                  f "+/- {r.importances_std [i] :. 3F}")

`` `

The output is:

`` `python
R2
  S5 0.204 +/- 0.050
  BMI 0.176 +/- 0.048
  BP 0.088 +/- 0.033
  SEX 0.056 +/- 0.023
neg_mean_absolute_percentage_error
  S5 0.081 +/- 0.020
  BMI 0.064 +/- 0.015
  BP 0.029 +/- 0.010
neg_mean_squared_error
  S5 1013.903 +/- 246.460
  BMI 872.694 +/- 240.296
  BP 438.681 +/- 163.025
  SEX 277.382 +/-115.126
`` `

## 4 Summary

In contrast, tree models are usually judged by the decline of impureness. The importance is usually based on the `training set. When the model is overfit, the importance of the feature is misleading.In this case, seemingly important features may not have satisfactory prediction capabilities for the new data encountered after the model.

At the same time, the importance importance based on impureness is easily affected by high quantity class properties (High Cardinality), so those numerical variables often rank forward.The Permutation Importance has no prejudice to the model's features, nor is it limited to specific model categories, and the applicability is wide.Please note.If the features have a strong multiple common linearity, it is recommended to take only one important feature. The method can view [Example] (https://scikit-rearn.org/Auto_examples/Inspection/plotation_importance_multicolinear.html.html #SPHX-GLR-Auto-examples-innspect-Plot-Plot-Importance-Multicolinear-Permutance with Multicoliner or Correled Features').

At the same time, `Scikit Learn` also provides an intuitive [Example] (https://scikit-rearn.org/Auto_Examples/inspection/plot_Permutance.html#Sphx-glr- EXA MPLES-inSpection-PLOT-PERMUTATATION-Importance-Permutation Importance Vs Random Forest Feature Importance (MDI)) shows the difference between unnoticed characteristic importance and Permutation Importance.

I hope this sharing will help you, please leave a message in the comment area!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>