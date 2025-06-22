---
template: overrides/blogs.html
tags:
  - machine learning
  - python
---

# AMEX - Default Prediction Kaggle Competition Summary

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-06-06, Reading time: approx. 6 minutes, WeChat article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485350&idx=1&sn=630219a13b43b343585b69c048f5f640&chksm=eb90f4d2dce77dc40ed6a88d7e174b6de9a0211e02588b686f76e6840af72fdb72afb8b61876&token=1184541802&lang=zh_CN#rd)

## 1 Overview

American Express (AMEX), a well-known financial services company, hosted a [data science competition](https://www.kaggle.com/competitions/amex-default-prediction) on Kaggle. Participants were tasked with predicting whether a credit cardholder would default in the future based on anonymized credit card billing data. AMEX provided explanations for feature prefixes:

```
D_* = Delinquency-related variables
S_* = Spending-related variables
P_* = Payment information
B_* = Balance information
R_* = Risk-related variables
```

The table below provides a sample of the competition data (values are fictional and for reference only):

| customer_ID | S_2 | P_2 | ... | B_2 | D_41 | target |
|---|---|---|---|---|---|---|
| 000002399d6bd597023 | 2017-04-07 | 0.9366 | ... | 0.1243 | 0.2824 | 1 |
| 0000099d6bd597052ca | 2017-03-32 | 0.3466 | ... | 0.5155 | 0.0087 | 0 |

Certain features such as `'B_30', 'B_38', 'D_114', 'D_116', 'D_117', 'D_120', 'D_126', 'D_63', 'D_64', 'D_66', 'D_68'` are categorical. The objective is to predict the probability of default (`target = 1` or `target = 0`) for each `customer_ID`. Negative samples were undersampled at a rate of 5%. The competition has ended, and this article summarizes publicly available solutions and discussions to share insights from the community.

## 2 Preparation Work

Due to the large dataset, memory optimization was crucial. Some efforts included converting floating-point data to integers and storing data in `parquet format`, as seen in [AMEX data - integer dtypes - parquet format](https://www.kaggle.com/datasets/raddar/amex-data-integer-dtypes-parquet-format). Another compression method was [AMEX-Feather-Dataset](https://www.kaggle.com/datasets/munumbutt/amexfeather).

```
60M sample_submission.csv
32G test_data.csv
16G train_data.csv
30M  train_labels.csv
```

The competition used a custom evaluation metric combining `top 4% capture` and `gini`. Many solutions referred to [Amex Competition Metric (Python)](https://www.kaggle.com/code/inversion/amex-competition-metric-python) and [Metric without DF](https://www.kaggle.com/competitions/amex-default-prediction/discussion/327534) for performance evaluation.

## 3 Exploratory Data Analysis (EDA)

Understanding the dataset thoroughly before modeling is essential. In this competition, key EDA tasks included:

- Checking missing values
- Identifying duplicate records
- Examining label distribution
- Analyzing credit card statement counts per customer
- Investigating categorical and numerical feature distributions
- Detecting anomalies and feature correlations
- Identifying artificial noise
- Comparing feature distributions between training and test sets

Notable high-score notebooks for EDA:

- [Time Series EDA](https://www.kaggle.com/code/cdeotte/time-series-eda#Load-Train-Data)
- [AMEX EDA which makes sense](https://www.kaggle.com/code/ambrosm/amex-eda-which-makes-sense)
- [American Express EDA](https://www.kaggle.com/code/datark1/american-express-eda)
- [Understanding NA values in AMEX competition](https://www.kaggle.com/code/raddar/understanding-na-values-in-amex-competition)

## 4 Feature Engineering & Modeling

### 4.1 Feature Engineering

As each customer has multiple statements, aggregating them was a focus of many solutions:

- For continuous variables: calculating mean, standard deviation, min, max, last statement value, and differences/ratios between last and first statement.
- For categorical variables: counting occurrences, tracking last statement value, converting frequencies into numerical features, and encoding accordingly.

High-score notebooks for feature engineering:

- [Amex Agg Data How It Created](https://www.kaggle.com/code/huseyincot/amex-agg-data-how-it-created/notebook)
- [Lag Features Are All You Need](https://www.kaggle.com/code/thedevastator/lag-features-are-all-you-need)
- [Amex Features: The best of both worlds](https://www.kaggle.com/code/thedevastator/amex-features-the-best-of-both-worlds)

### 4.2 Model Design, Training & Inference

Top solutions used XGBoost, LightGBM, CatBoost, Transformer, TabNet, or ensembles of these models. Chris Deotte, a Kaggle Grandmaster at Nvidia, contributed foundational solutions such as [XGBoost Starter](https://www.kaggle.com/code/cdeotte/xgboost-starter-0-793), [TensorFlow GRU](https://www.kaggle.com/code/cdeotte/tensorflow-gru-starter-0-790), and [TensorFlow Transformer](https://www.kaggle.com/code/cdeotte/tensorflow-transformer-0-790). His final 15th place solution used Transformer with LightGBM knowledge distillation ([15th Place Gold](https://www.kaggle.com/competitions/amex-default-prediction/discussion/347641)).

The second-place team ([2nd place solution - team JuneHomes](https://www.kaggle.com/competitions/amex-default-prediction/discussion/347637)) highlighted best practices, including team collaboration using AWS, thorough version control, and model selection strategies.

The first-place solution ([1st solution](https://www.kaggle.com/competitions/amex-default-prediction/discussion/348111)) was highly complex but not detailed by the author.

## 5 Conclusion

Many useful insights emerged from the competition's Discussion section:

- [Speed Up XGB, CatBoost, and LGBM by 20x](https://www.kaggle.com/competitions/amex-default-prediction/discussion/328606)
- [Which is the right feature importance?](https://www.kaggle.com/competitions/amex-default-prediction/discussion/331131)
- [11th Place Solution (LightGBM with meta features)](https://www.kaggle.com/competitions/amex-default-prediction/discussion/347786)

Notable notebooks include:

- [AMEX TabNetClassifier + Feature Eng [0.791]](https://www.kaggle.com/code/medali1992/amex-tabnetclassifier-feature-eng-0-791)
- [KerasTuner - Find the MLP for you!](https://www.kaggle.com/code/illidan7/kerastuner-find-the-mlp-for-you)
- [AmEx lgbm+optuna baseline](https://www.kaggle.com/code/anuragiitr1823/amex-lgbm-optuna-baseline/notebook)

This competition showcased impressive ML techniques and strategies, offering valuable learning experiences for the community.



