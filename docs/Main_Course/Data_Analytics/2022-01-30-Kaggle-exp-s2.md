---
template: overrides/blogs.html
---

# Kaggle量化竞赛Top方案

!!! info 
    作者：Void，发布于2022-01-30，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/oaT49hLhGiL_ajz1dIlGcQ)

## 1 引言

最近，Kaggle上量化相关的竞赛层出不穷。  
前有Jane Street主办的给出交易信号最大化收益的比赛，刚结束的Optiver主办的预测已实现波动率的比赛。在进行中的，G-Research主办的预测数字货币收益率的比赛以及国内量化私募——九坤主办的预测收益率的比赛。  
可能是这些机构真的从Kaggle中获得了不少insight，赚到了真金白银，才使它们如此热衷地举办此类竞赛。  
不同于之前在比赛进行中解读的开源方案：

- [想体验量化交易吗](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484518&idx=1&sn=1110c1bc0a927d0a43446e2ac538fee1&scene=19#wechat_redirect)
- [抄作业啦](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484478&idx=1&sn=87de555f9ccfb00fc4d9ec6934bc61fa&scene=19#wechat_redirect)

本文将解读已结束的Jane Street Market Prediction以及Optiver Realized Volatility Prediction的Top 1的解决方案。
虽然金融市场难以预测，但是神奇的是高分团队可以一直保持在排行榜顶端。

## 2 竞赛介绍

简单回顾下两个竞赛的赛题：
- Jane Street要求我们给出是否交易的信号以最大化收益。
- Optiver要求我们预测高频金融数据(股票)的波动率。


## 3 具体代码

同样，我们一起来看一下开源的高分代码。

### 3.1 import packages

第一部分照例是导入一堆包。值得一提的是，由于本次数据量较大。代码使用了datatable进行数据读取。datatable据称是一个性能碾压pandas的高效多线程数据处理工具

```python
import datatable as dtable
train = dtable.fread('/kaggle/input/jane-street-market-prediction/train.csv').to_pandas()
```

### 3.2 特征工程

由于本次提供的特征仍然是一些不知道含义的匿名特征。代码根据每个特征的分布人为地划分为了4种特征：Linear，Noisy，Negative和Hybrid。  
最后的特征即为所有原始特征，加上每类特征的均值构造的特征。

```python
train['f_Linear']=train[f_Linear].mean(axis=1)
train['f_Noisy']=train[f_Noisy].mean(axis=1)
train['f_Negative']=train[f_Negative].mean(axis=1)
train['f_Hybrid']=train[f_Hybrid].mean(axis=1)
```

### 3.3 确定label

训练集并没有直接给我们label，即是否action。它提供的是5种不同时间窗口的收益率(return)。代码构造label的方式是判断若有大于3个收益为正，即执行交易(action=1)。

```python

resp_cols = ['resp', 'resp_1', 'resp_2', 'resp_3', 'resp_4']
y = np.stack([(train[c] > 0).astype('int') for c in resp_cols]).T

train['action'] = (y.mean(axis=1) > 0.5).astype('int')
```

### 3.4 模型训练

关于模型部分，方案使用了一个XGBoost模型，并用HyperOpt进行了参数优化。  
关于cv的使用，它使用了适合于此类时间序列问题的PurgedGroupTimeSeriesSplit，从下图中可以很直观的看到。验证集永远在训练集后面，并且中间隔了一小段时间。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-9-5/1630827782227-purged_cv.png" width="500" />
</figure>

## 4 小结

可以看到本次开源方案并不复杂，也仍有很多空间可以提升，如分析特征含义，使用神经网络模型，优化题目给出的评价指标等等。但是，在信噪比较低的金融世界中，这些方法是否有用仍是一个问号。  


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
