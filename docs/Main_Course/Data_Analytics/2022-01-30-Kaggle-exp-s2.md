---
template: overrides/blogs.html
---

# Kaggle量化竞赛Top方案

!!! info 
    作者：Void，发布于2022-01-30，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/oaT49hLhGiL_ajz1dIlGcQ)

## 1 引言

最近，Kaggle上量化相关的竞赛层出不穷。  
前有Jane Street主办的给出交易信号，最大化收益的比赛，刚结束的Optiver主办的预测已实现波动率的比赛。在进行中的，G-Research主办的预测数字货币收益率的比赛以及国内量化私募——九坤主办的预测收益率的比赛。  
可能是这些机构真的从Kaggle中获得了不少insight，赚到了真金白银，才使它们如此热衷地举办此类竞赛。  
不同于之前解读在比赛进行中开源的方案：

- [想体验量化交易吗](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484518&idx=1&sn=1110c1bc0a927d0a43446e2ac538fee1&scene=19#wechat_redirect)
- [抄作业啦](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484478&idx=1&sn=87de555f9ccfb00fc4d9ec6934bc61fa&scene=19#wechat_redirect)

本文将解读已结束的Jane Street Market Prediction以及Optiver Realized Volatility Prediction最终排名第一的解决方案。


## 2 竞赛介绍

简单回顾下两个竞赛的赛题：
- Jane Street要求我们给出是否交易的信号以最大化收益。
- Optiver要求我们预测高频金融数据(股票)的波动率。

这两个比赛在私榜(Private Leaderboard)阶段都会定期的用实际的金融数据更新方案排名。虽然金融市场难以预测，但是神奇的是高分团队可以一直保持在排行榜顶端，让人不得不信服他们方案的有效性。下面我们就来一起看看他们的获胜方案吧。

## 3 方案解读

### 3.1 Jane Street Top 1 solution from Cats Trading...

获胜方案采用了一个XGBoost和一个有监督的自编码器的神经网络(Supervised Autoencoder with MLP)集成，其中后者单模型也能保持第一。

### 3.2 Optiver Top 1 solution from nyanp

之前的文章中我们提到过，竞赛给出的数据主要是交易相关的(价格、成交量等)以及订单簿数据(买一价、卖一价等)这两大类。有一定领域相关知识的选手可以构造出不少有用的特征。在开源的Code或是Discussion中也有大佬给出了这些特征。大家用的特征都差不多，因此特征这块并不是获胜的关键。  

在模型ensemble方面，最终的模型是一个CNN(权重0.4)，一个GBDT(权重0.4)，一个TabNet(权重0.1)以及一个MLP(权重0.1)的集成。从单模型角度，一个GBDT最终即可获得第一，其他单模型也都在金牌区。可见他的单模型都表现很好，最终模型集成的提升并没有特别大。  

获胜的关键是nyanp采用了7种不同的最近邻的方式来获得聚合特征。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>

可以看到聚合的维度主要是时间和股票两种，衡量的指标有价格、波动率、交易量，采用的最近邻算法是sklearn中的NearestNeighbors算法，并采用了不同的衡量距离的方式。  
NearestNeighbors是无监督的最近邻算法，包括了brute force以及通过KD树等优化距离计算的一些算法。  

其实在比赛中开源的方案也提到了通过Kmeans获得聚合特征。nyanp做的较好的地方是采用了不同方式，使获得的特征更加稳健。加上此类聚合特征后，方案的排名有了大幅度的提升。



## 4 小结

可以看到本次开源方案并不复杂，也仍有很多空间可以提升，如分析特征含义，使用神经网络模型，优化题目给出的评价指标等等。但是，在信噪比较低的金融世界中，这些方法是否有用仍是一个问号。  


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
