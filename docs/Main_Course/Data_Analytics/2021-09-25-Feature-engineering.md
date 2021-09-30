---
template: overrides/blogs.html
---

# 金融风控特征工程小结

!!! info 
    作者：Jeremy，发布于2021-09-25，阅读时间：约8分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

前一阵子总结了下自己参加的信贷违约风险预测比赛的数据处理和建模的流程，发现自己对业务上的特征工程认识尚浅，凑巧在Kaggle上曾经也有一个金融风控领域——[房贷违约风控](https://www.kaggle.com/c/home-credit-default-risk/overview)的比赛，里面有许多大神分享了他们的特征工程方法，细看下来有不少值得参考和借鉴的地方。

## 2 赛题和数据简介

这个比赛也是经典的监督学习中的二分类问题，需要我们根据用户的申请信息，征信信息（Bureau）以及用户在该机构的信用历史等信息，预测申请人贷款违约的概率。由于赛题是做贷前预测，所以需要找的特征主要是挖掘客户是否存在欺诈，对于非欺诈用户，他们是否有能力还款、

<figure>
  <img src="https://files.mdnice.com/user/15233/3a541655-3d6a-457f-a195-5ef56d8046d5.png"  />
  <figcaption>数据表关系图</figcaption>
</figure>


赛题的数据分布在几张表里，需要我们做适当的表连接操作：

* 申请表:贷款申请信息，主表，一行代表一个贷款申请id。
* 征信(Bureau)余额表: Bureau信用记录，每行是一个申请用户的月度数据，一个id最多有近96个月的记录
* 申请历史表: 同一用户的历史贷款申请信息，额度，期限，利率，是否审批通过等
* 还款记录表: 同一用户的历史还款行为记录。
* 信用卡余额记录表: 持有信用卡的用户的信用卡消费行为记录数据。

## 3 特征工程

特征工程的主要思路是尽可能多地构造大量特征，再利用特征筛选指标或是模型减少特征数量。

自动化的数据工程这一步，有些选手几乎完全依赖自动特征工程，例如构造polynomial features，有些利用开源的数据工程包如Featuretools。

### 3.1 近期特征

有时数据中的时间信息为时间戳，我们可以手工将其转换成数值信息，如计算最近一次使用信用卡的时间，上一次联系时间，上次逾期时间等。

### 3.2 统计特征 

一个申请id会对应拉取其申请人的征信(Bureau Credit)数据和信用卡使用数据，一个申请id在其他表中对应多行记录。对于这部分变量，往往会考虑构造统计性特征，如均值，最大/最小值，合计值，频次等等。

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

### 3.3 时序特征

在不同的时间窗口计算时序特征往往能帮助识别异常的用户消费行为。常见的时序特征有：

* 最大值-最小值
* 当前值/N月均值
* N月内持续升高/降低
* 最大连续上升/下降月份数

例如如果一个用户在本月消费金额远高于过去12个月内的月均消费金额，可能说明客户在恶意透支信用额度或者盗刷，用户的风险应提高。

### 3.4 特征筛选

根据特征选择的形式，可分为三大类：

* Filter(过滤法)：按照发散性或相关性对各个特征进行评分，设定阈值或者待选择特征的个数进行筛选，常见的指标有pearson相关系数，卡方验证，互信息等。
* Wrapper(包装法)：根据目标函数（往往是预测效果评分），每次选择若干特征，或者排除若干特征，常见如递归特征消除法。
* Embedded(嵌入法)：先使用某些机器学习的模型(常见用树模型)进行训练，得到各个特征的权值系数，根据系数从大到小选择特征（类似于Filter，只不过系数是通过训练得来的）。

为了保证模型的可解释性，例如PCA对特征做变换的特征降维方法一般不用于风控建模中。多数特征筛选方法是先用filter法移除共线特征，然后利用嵌入法计算特征重要性对进行排序。

在 [Introduction to Feature Selection](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection) 中，作者最终从1465个变量中筛选342个变量放入LightGBM模型中，测试集AUC仅从0.783降低到0.782，未经过特征工程的LightGBM模型baseline为0.735。

## 4 小结

Kaggle 大神们的特征工程思路后，最大的感受是工程量很大。一些公司会选择直接将特征扩展的步骤合并在数据仓库的ETL中，从而降低建模的周期和成本。对于个人来说，了解数据仓库中的ETL过程，或许是提高业务认知的手段之一。
