---
template: overrides/blogs.html
---

# American Express - Default Prediction 竞赛精华总结

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()


## 1 概述

美国著名金融服务公司American Express在Kaggle上举办了一个数据科学竞赛，要求参赛者针对信用卡账单数据预测持卡人是否在未来会逾期。其中，各个特征都做了脱敏处理，AMEX提供了特征前缀的解释:

```
D_* = 逾期相关的变量
S_* = 消费相关的变量
P_* = 还款信息
B_* = 欠款信息
R_* = 风险相关的变量
```

其中'B_30', 'B_38', 'D_114', 'D_116', 'D_117', 'D_120', 'D_126', 'D_63', 'D_64', 'D_66', 'D_68'特征为类别型的数据，目标是对于每一个customer_ID，预测其在未来逾期（target = 1）的可能性。其中负样本已经做了欠采样（采样率为5%）。近日比赛已经结束，本文将选取目前已经公开代码的方案进行总结和浅析，和大家一起学习社区中优秀的思路和具体实现。

## 2 准备工作

由于数据量相对于Kaggle提供的实验环境很大，因此有一些工作是围绕内存的优化展开的，比如[AMEX data - integer dtypes - parquet format](https://www.kaggle.com/datasets/raddar/amex-data-integer-dtypes-parquet-format 'AMEX data - integer dtypes - parquet format')将浮点型的数据转化为了整型，并将数据以`parquet format`格式存储，有效地减少了内存的开销。类似的数据压缩方案还有[AMEX-Feather-Dataset](https://www.kaggle.com/datasets/munumbutt/amexfeather, 'AMEX-Feather-Dataset')。

```
60M sample_submission.csv
32G test_data.csv
16G train_data.csv
30M  train_labels.csv
```

同时，本次竞赛的评价指标是客制化的，融合了`top 4% capture`和`gini`，许多方案都参考了[Amex Competition Metric (Python)](https://www.kaggle.com/code/inversion/amex-competition-metric-python, 'Amex Competition Metric (Python)')和[Metric without DF](https://www.kaggle.com/competitions/amex-default-prediction/discussion/327534 'Metric without DF')的代码进行模型性能的评价。

下表为竞赛的数据示意（值为虚构，仅做参考）

| customer_ID | S_2 | P_2 | ... | B_2 | D_41 | target |
|---|---|---|---|---|---|---|
| 000002399d6bd597023 | 2017-04-07 | 0.9366 | ... | 0.1243 | 0.2824 | 1 |
| 0000099d6bd597052ca | 2017-03-32 | 0.3466 | ... | 0.5155 | 0.0087 | 0 |

## 3 探索性数据分析

在对数据建模前，透彻地了解它非常关键，探索性数据分析（Exploratory Data Analysis）成为了许多后续工作的基础。在AMEX的竞赛中，社区在这一阶段的工作关注点有：

- 检查数据中的缺失值
- 检查重复的记录
- 标签的分布
- 每位客户信用卡账单数量及账单日分布
- 类别型变量及数值型变量的分布，是否有异常值
- 特征之间的相关性
- 人为噪音
- 训练集和测试集中特征分布对比

针对这些分析，高分笔记本有如下：

- [Time Series EDA](https://www.kaggle.com/code/cdeotte/time-series-eda#Load-Train-Data, 'Time Series EDA')
- [AMEX EDA which makes sense](https://www.kaggle.com/code/ambrosm/amex-eda-which-makes-sense)
- [American Express EDA](https://www.kaggle.com/code/datark1/american-express-eda, 'American Express EDA')

## 4 特征工程 & 建模




希望这次的分享对你有帮助，欢迎在评论区留言讨论！



<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
