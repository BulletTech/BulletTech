---
template: overrides/blogs.html
tags:
  - machine learning
---

# Kaggle Tips

!!! info
    Author: Void, Published on 2021-07-20, Reading time: about 10 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/LVw3rcDCOk0R3oZ_MEDAEQ)

## 1 Introduction

As the most famous data science competition platform (no doubt about it), Kaggle provides various high-quality competitions and has formed a friendly and open-source community atmosphere. Many experts generously share their knowledge and experience. This article summarizes some useful tips seen in the Kaggle treasure trove.

## 2 Tips

[Chris Deotte](https://www.kaggle.com/cdeotte) is an active expert in the Kaggle community and a Grandmaster in Competitions, Datasets, Notebooks, and Discussion. He is ranked #1 in the world in the Discussion section (ranked by the number of medals earned in discussion threads). From his discussion threads, we can always gain many experience and knowledge.

He has an article about feature engineering:

- Label encoding should be done with the training set and the test set together. This is mainly to prevent new categories from appearing in the test set. It should be noted that if label processing is involved, such as WOE, the training set should be processed first, and the validation set should use the dictionary to find the corresponding values to prevent data leakage.
- Handling missing values. For tree models, samples with missing values are divided into left and right subtrees based on gain. One way to handle missing values is to fill them with -999, which allows these samples to participate in node splitting. Whether this approach can improve model performance needs to be confirmed by validation results.
- Since Kaggle competition questions often encounter the problem of data size being too large, we need to reduce the memory occupancy of data. There is a classic memory_reduce function on Kaggle that can reduce data size well.
- For categorical variables in tree models, they can be treated as categories or numbers after label encoding. Which method is better still needs to be confirmed by validation results.
- Splitting one feature into multiple features. For example, splitting the amount into integer and decimal parts. Not sure if it's useful.
- Feature combination. Combining categorical variables or performing addition, subtraction, multiplication, and division on numerical variables.
- Frequency Encoding (and various encodings).
- Some statistical measures after Group by.
- Normalization. Generally, normalization is not a big problem (it is necessary for neural networks, and trends in data can also be removed).
- Eliminating the influence of extreme values.

In the IEEE-CIS Fraud Detection competition, Chris also won first place. His experience sharing about this competition includes:

- The key to the competition is to identify the client's UID. However, ID variables such as UID cannot be directly used as features because many new UIDs appear in the test set.
- CatBoost models perform well in tree models.
- Temporal consistency of variables: Chris used the data in the first month to train a model for each variable and then looked at the performance of the model in the last month. If the performance is poor, it means that this variable may only work in the past, and these variables should be discarded.
- Numerical variables with low variance are often useless. Sklearn.feature_selection has VarianceThreshold to perform feature selection.

Chris also participated in some image and NLP-related competitions, which are not summarized here as they are not closely related to his main business.

[CPMP](https://www.kaggle.com/cpmpml) is also a Grandmaster in Discussion and has an article on tips to avoid overfitting.

- The more the validation set is used, the easier it is to overfit to the validation set, such as the public LB (leaderboard) and fixed k-fold CV in competitions. A good method is to use random k-fold CV.
- He recommends a [paper](https://arxiv.org/abs/1811.12808) on model validation and model selection.

## 3 Conclusion

Although some of these knowledge and experiences are targeted at competition tricks, they still have certain guiding significance for daily modeling and are worth our thinking and trying. 

Thanks to the spirit of these experts who are willing to share, it is truly fortunate to be able to absorb knowledge and nutrition from the Kaggle community. 

