# Summary of Feature Engineering in Financial Risk Control

!!! info
    Author: Jeremy, published on September 25, 2021, reading time: about 8 minutes, WeChat public account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484564&idx=1&sn=e13190de19bb84676db3902527685159&chksm=eb90f7e0dce77ef69155a7f19a4181f04b35c01e1297b2355389667e8b178ff5f7c373bd9479&token=1727747278&lang=zh_CN#rd)

## 1 Introduction

Recently, I summarized the data processing and modeling process of a credit default risk prediction competition I participated in, and found that my understanding of business feature engineering is still shallow. Incidentally, there was also a financial risk control competition on Kaggle, namely the Home Credit Default Risk Competition, in which many experts shared their feature engineering methods, and there were many places worth learning and referring to upon careful study.

## 2 Problem and Data Introduction

This competition is also a classic supervised binary classification problem in which we need to predict the probability of loan default by the applicant based on their application information, bureau credit records of the applicant (Bureau), and their credit history with the institution. Since the task is to predict before lending, the main focus of features to be mined is whether the customer is fraudulent or not, and for non-fraudulent customers, whether they have the ability to repay.

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/3a541655-3d6a-457f-a195-5ef56d8046d5.png"  />
  <figcaption>Data table relationship diagram</figcaption>
</figure>

The data of the competition is distributed in several tables, and we need to do appropriate table join operations:

* Application table: loan application information, main table, one row represents one loan application ID.
* Bureau balance table: Bureau credit records, each row is monthly data of an applicant, with up to 96 months of records for one ID.
* Application history table: Historical loan application information of the same user, including credit line, term, interest rate, approval status, etc.
* Repayment table: Historical repayment behavior records of the same user.
* Credit card balance record table: credit card consumption behavior record data of users with credit cards.

## 3 Feature Engineering

The main idea of feature engineering is to construct as many features as possible, and then reduce the number of features using feature selection indicators or models.

For the automatic data engineering step, some contestants almost completely rely on automatic feature engineering, such as constructing polynomial features, while others use open-source data engineering packages such as Featuretools.

### 3.1 Recent Features

Sometimes the time information in the data is in timestamp format, which can be manually converted into numerical information, such as calculating the time of the last credit card usage, the last contact time, and the last overdue time.

### 3.2 Statistical Features

One loan application ID corresponds to Bureau credit records and credit card usage data of the applicant, with multiple rows of records in other tables corresponding to one ID. For these variables, statistical features such as mean, maximum/minimum value, total value, and frequency are often considered.

``` python
def agg_numeric(df, group_var, df_name):
    """
    Aggregates the numeric values in a dataframe. This can
    be used to create features for each instance of the grouping variable.
    """
    # Remove id variables other than grouping variable
    for col in df:
        if col != group_var and 'SK_ID' in col:
            df = df.drop(columns = col)

    group_ids = df[group_var]
    numeric_df = df.select_dtypes('number')
    numeric_df[group_var] = group_ids

    # Group by the specified variable and calculate the statistics
    agg = numeric_df.groupby(group_var).agg(['count', 'mean', 'max', 'min', 'sum']).reset_index()

    # Need to create new column names
    columns = [group_var]

    # Iterate through the variables names
    for var in agg.columns.levels[0]:
        # Skip the grouping variable
        if var != group_var:
            # Iterate through the stat names
            for stat in agg.columns.levels[1][:-1]:
                # Make a new column name for the variable and stat
                columns.append('%s_%s_%s' % (df_name, var, stat))

    agg.columns = columns
    return agg
```

### 3.3 Time Series Features

Calculating time series features in different time windows can help identify abnormal user consumption behavior. Common time series features include:

* Maximum value - minimum value
* Current value/N-month average value
* Continuous increase/decrease within N months
* Maximum consecutive increase/decrease in the number of months

For example, if a user's current monthly consumption amount is much higher than the monthly average consumption amount in the past 12 months, it may indicate that the customer has deliberately overdrawn their credit limit or engaged in credit card fraud, and the user's risk should be increased.

### 3.4 Feature Selection

According to the form of feature selection, it can be divided into three categories:

* Filter: Evaluating each feature according to its divergence or correlation, setting a threshold or selecting a number of features to be screened, common indicators include Pearson correlation coefficient, chi-square test, mutual information, etc.
* Wrapper: Based on the target function (often a prediction performance score), select or exclude a certain number of features each time, common methods include recursive feature elimination.
* Embedded: First train some machine learning models (usually tree models), obtain the weight coefficients of each feature, and select features based on the coefficients in descending order (similar to filter, but the coefficients are obtained through training).

To ensure the interpretability of the model, feature dimensionality reduction methods such as PCA for transforming features are generally not used in risk control modeling. Most feature selection methods first remove collinear features using filter methods, and then use embedded methods to calculate feature importance to sort them.

In [Introduction to Feature Selection](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection), the author finally selected 342 variables from 1465 variables and put them into the LightGBM model. The AUC of the testing set only decreased from 0.783 to 0.782, while the baseline LightGBM model without feature engineering was 0.735.

## 4 Conclusion

The biggest feeling after studying the feature engineering ideas of the Kaggle experts is that the amount of work is huge. Some companies choose to directly merge the feature expansion step in the ETL of the data warehouse, thereby reducing the cycle and cost of modeling. For individuals, understanding the ETL process in the data warehouse may be one of the means to improve business understanding.