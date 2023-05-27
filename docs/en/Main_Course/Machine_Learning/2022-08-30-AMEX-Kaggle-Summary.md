# AMEX - Default Prediction Kaggle Competition Summary

!!! info
    Author: Yuanzidanqiflying, Published on 2021-06-06, Reading Time: About 6 Minutes, WeChat Official Account Article Link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485350&idx=1&sn=630219a13b43b343585b69c048f5f640&chksm=eb90f4d2dce77dc40ed6a88d7e174b6de9a0211e02588b686f76e6840af72fdb72afb8b61876&token=1184541802&lang=zh_CN#rd)

## 1 Overview

The American financial services company American Express (AMEX) held a [data science competition](https://www.kaggle.com/competitions/amex-default-prediction) on Kaggle, requiring the participants to predict whether the cardholder will be overdue in the future based on credit card billing data. All features have been desensitized, and AMEX provides an explanation of the feature prefix:

```
D_* = Variables related to overdue.
S_* = Variables related to consumption.
P_* = Repayment information.
B_* = Debt information.
R_* = Variables related to risk.
```

The data in the competition is a demonstration (values are fictitious, for reference only):

| customer_ID | S_2 | P_2 | ... | B_2 | D_41 | target |
|---|---|---|---|