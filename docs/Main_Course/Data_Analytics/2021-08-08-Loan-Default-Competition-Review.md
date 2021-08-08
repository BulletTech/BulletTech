---
template: overrides/blogs.html
---

# 天池零基础金融风控比赛小结

!!! info 
    作者：Jeremy，发布于2021-08-08，阅读时间：约12分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 背景

去年九月份参加了天池举办的零基础入门金融风控-贷款违约预测比赛，赛题以金融风控中的个人信贷为背景，要求选手根据贷款申请人的数据信息预测其是否有违约的可能，以此判断是否通过此项贷款，是一个典型的分类问题。

## 2 数据

赛题数据来源于某信贷平台的贷款记录，总数据量为120W，训练集，测试集A，测试集B数据量各位80W，20W，20W。原数据中包含47列变量信息，其中15列为匿名变量。主要包括的信息有：贷款信息(金额，利率，贷款等级等)，贷款人信息(就业信息，收入信息，债务比，FICO，贷款记录等)，贷款人行为计数特征信息（匿名）。查询完整的字段表可以访问赛题官网(https://tianchi.aliyun.com/competition/entrance/531830/information)，或点击**阅读原文**查看我们Blog上的文章。

赛题需要参赛者输出每个测试样本为1（违约）的概率，以AUC为指标评估模型。

## 3 思路和方法

### 3.1 EDA+数据清洗

该部分主要为了了解数据类型，各种特征的数据分布和缺失值情况，并了解特征间的相关关系以及特征和目标值之前的相关关系。为接下来对数据进行简单清洗做准备。

![特征箱线图](https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-8/1628434776302-%E7%AE%B1%E7%BA%BF%E5%9B%BE.png)

整体而言赛题数据相对干净，通过箱线图发现有一些数值特征中存在明显的异常值,决定使用箱型图+3-Sigma进行去除。对于缺失值，选择先构造特征记录缺失特征数量，再用纵向填充的方法尝试处理。此外通过计算Pearson相关系数可以看出有几对相关度很高的变量，例如匿名变n2-n3-n9和ficoRangeLow-ficoRangeHigh等，每对保留一个变量即可。

![特征相关性热图](https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-8/1628434676311-feature_corr.png)

### 3.2 特征工程

经过EDA可以发现特征中有较多离散型变量，如贷款等级，工作职称，贷款目的，邮编等等，这些变量需要通过一定的编码方法进行变换。常见的one-hot encoding对于较低维度的变量（unique values < 100）效果不错，但是如果应用在高维变量上（如邮编，职称等），会产生过于稀疏的矩阵，导致每个类别里可以学习的数据过少。所以对于高维变量，一种比较有效的编码方式是target encoding，即用类别对应的标签的期望来代替原始的类别，这样相当于将高维的离散变量转换成了在0-1之间的数字变量。比较常用的定义方式为：

![](https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-7/1628306237775-image.png)

其中p为全部标签的均值，alpha为系数，用于控制该变量对依赖变量的拟合程度。


特征交互方面，简单构造了一些可能有实际意义的交互特征，这一部分的业务经验不多，有经验的小伙伴欢迎在评论区分享一下特征构造的思路。

``` python 
data['interestRateOLoanAmnt'] = data['interestRate']/data['loanAmnt']
data['annualIncomeOLoanAmnt'] = data['annualIncome']/data['loanAmnt']
data['annualIncomeOImploymentLength'] = data['annualIncome']/data['employmentLength']
data['annualIncomeMImploymentLength'] = data['interestRate']*data['loanAmnt']
data['openAccOTotalAcc'] = data['openAcc']/data['totalAcc']
data['openAccOEarliestCreditLine'] = data['openAcc']/data['earliesCreditLine']
data['pubRecOissueDate'] = data['pubRec']/data['issueDate']
```

最后根据EDA中的相关系数计算，去除了三个和其他变量有高相关性的变量，加上离散特征一共保留了约150个特征。

### 3.3 模型训练

模型训练部分的思路是尝试构造几个表现较强的单模型，再进行模型融合。一共尝试了 XGBoost, Light-GBM, Catboost以及MLP(4 layers) 4种模型，CatBoost 模型本身就可以很好地处理离散特征，并且碰巧它也是使用基于target encoding衍生的方法处理高维离散特征，所以使用CatBoost时省略了对离散特征进行预处理的步骤。此外对MLP模型处理之前，额外尝试了使用自动编码器进行变量交互，但是效果明显不如Boosting模型。

为了冲刺竞赛排名，模型融合也比较关键。我选择了表现较强的的三个Boosting模型，用简单加权平均的方法进行Stacking，让AUC成绩由单模型的0.7342提高到最终的0.7397。

4个单模型和融合模型的训练表现如下:


|  模型  | Training AUC | Validation AUC | Test AUC * |
|  ----  | ----  | ----  |  ----  | 
| XGBoost(baseline)  | **0.7845** | 0.7367 | - | 
| Light-GBM | 0.7407 | 0.7351 | - |
| CatBoost  | 0.7446 | **0.7434** | 0.7342 |
| MLP | 0.7263 | 0.7247 | - |

* 获取test AUC数据需要上传预测值到天池平台，每天只有一次测试机会，所以只收集了效果最好的CatBoost模型的AUC结果。

从模型对比来看，XGBoost的过拟合现象较为严重，LightGBM 比较均衡，CatBoost泛化能力很好并且表现出众，主要得益于对类别变量的优秀处理能力。MLP模型表现一般，可能是数据规模还没有足够大到让它能够完全发挥挖掘非线性特征的能力。

### 3.4 特征重要性

![CatBoost模型特征的SHAP值- Top20](https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-8/1628434578524-SHAP2png.png)

三个Boosting模型对特征重要性的评估略有区别，比较明显的区别是CatBoost模型中，离散数据的重要性普遍较高。以CatBoost的SHAP值为例，最重要的特征有点出乎意料地是**申请人职称**，此外，**贷款期数，贷款子级，地区邮编，债务收入比**等也有较高的SHAP值。对于数值型特征而言，三个模型的排序基本相似。在特征工程中构造的少数几个变量如**审批时间，有效账户/总账户比**也有幸被选进重要度前20。

## 4 总结

这次的赛题是一个经典的机器学习分类预测问题，Boosting模型实乃这种数据量的比赛中的大杀器，其中CatBoost又尤为适合挖掘离散型变量。再利用模型融合，最终在正赛阶段排名榜的Top30。但是由于业务经验有限，在特征工程方面给模型表现带来的提升不多，这应该是后期模型表现优化的主要方向。

## 5 参考

1. 天池竞赛 零基础入门金融风控-贷款违约预测: https://tianchi.aliyun.com/competition/entrance/531830/information
2. Target Encoding 参考文献:  A Preprocessing Scheme for High-Cardinality Categorical Attributes in Classification and Prediction Problems
3. CatBoost库: https://CatBoost.ai/