---
template: overrides/blogs.html
tags:
  - time series
  - machine learning
---

# 时间序列异常检测

!!! info
    作者：Void，发布于2021-07-20，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/XwtXpa1hOKrN6fIC-zpyKw)

## 1 引言

事情的起因是有朋友告诉我最近有KDD Cup 2021的比赛。为了凑个热闹，也为了刷点经验，我们准备合伙参加(当个炮灰)。  
有三道赛题，时间序列异常检测、图相关的和智慧城市。看上去最正常的[时间序列异常检测](https://compete.hexagon-ml.com/practice/competition/39/)当仁不让的成为了我们的选择。

## 2 题目要求

竞赛要求我们检测时间序列中的异常点。每个时间序列有且仅有一个异常点。题目给出了异常点所在的区间，要求我们给出异常点所在的位置。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-18/1626574899890-3.png" width="500" />
  <figcaption>Example</figcaption>
</figure>

评估时会考察我们给出的位置前后100个点的范围内是否包含真正的异常点。序列长度从几千到几十万个观测点不等。数据的来源可能有心电图、传感器数据等具有明显周期性的数据。目的是想让我们找到有效的算法，自动化地监测大规模的此类数据。  

竞赛分为两期，第一期(PhaseI)有25个时间序列，用于调试算法。第二期(PhaseII)有250个序列，用于评估比赛成绩。

## 3 数据分析

我们选取一个时间序列瞧一瞧。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-18/1626574877652-1.png" width="500" />
  <figcaption>timeseries</figcaption>
</figure>

可以看到这个序列具有很强的周期性。同时，题目告诉我们，异常点位于第2500个点之后。  
通过人工智能(肉眼)识别，我们可以发现第5500个点附近的数据似乎有些古怪。那么，我们怎么通过算法将它识别出来呢？

## 4 初步尝试

可能大部分人都知道，可以通过均值+-几倍标准差来识别极值。但是这个方法有几个缺陷：
- 可以识别出一堆极值，无法确定哪个是异常值
- 极值不一定是异常值，请看：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-18/1626574877658-2.png" width="500" />
  <figcaption>outliers</figcaption>
</figure>

通过肉眼，我们可以发现异常值在第6000个观测值附近。然而那一块并没有出现极值。因此，可以说对于这种周期性较强的时间序列，极值可能也是周期的一部分。我们需要识别的是某个与其他周期不同的小区间。

## 5 Matrixprofile算法

那么，如何识别出周期层面的异常区间呢？我们可能会想，我们先确定一个区间，然后看看这个区间和其他同样长度的区间长得是否不同。  
题目好心地提示我们有这样一个包：matrixprofile。

[matrixprofile](https://towardsdatascience.com/introduction-to-matrix-profiles-5568f3375d90)算法由加州大学河滨分校的研究者于2016年提出。它的想法比较简单直白，即给定窗口长度，计算这个子序列与其他同样长度的子序列的距离，其中，与最相似序列(距离最小的序列)的距离为这个子序列的mp值。通过滑动窗口，我们可以计算出整个序列的mp值。其中，较大的mp值可以认为，此处的子序列与和它最相似的序列距离都比较大，因此该子序列有更大的可能是异常值。  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-18/1626574877648-1.gif" width="500" />
  <figcaption>Demo</figcaption>
</figure>

matrixprofile这个包更多的是在计算效率上做了优化，如在距离的计算上，将子序列标准化后只需要计算点积，避免了欧式距离的计算等等。  

## 6 小试牛刀

matrixprofile的使用非常方便

```python
import matrixprofile as mp
profile= mp.compute(data,windows=window_size,n_jobs=8) #window_size为子序列长度
discords=mp.discover.discords(profile,k=1) #k=1表示找到最大的那一个mp
start_index=discords['discords'][0] #此时，这个子序列的起始点为start_index
```

我们用刚开始瞧一瞧的时间序列为例。通过人眼识别，我们发现异常值在第5500个观测值附近，我们看看用matrixprofile将会表现如何？

首先，我们需要确定窗口(子序列)长度。我们通过傅里叶变换得到周期(频域中，振幅最大的点)。通过计算，matrixprofile告诉我们mp值最大的子序列的起始点为5500，整个序列的mp值序列如下图所示：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-18/1626576279441-4.png" width="500" />
  <figcaption>mp series</figcaption>
</figure>

可以看到，这个子序列相较别的序列，在距离上有明显的不同。我们成功找到了和人眼识别完全相同的异常序列，我们可以简单地认为异常值在这个子序列的中点。  
下面需要做的就是遍历所有时间序列，找出异常值，并提交即可。通过matrixprofile这一简单直白的算法，我们成功的跻身排行榜88%的分位(第一是100%)。

## 7 小结

对于这类周期性较强的时间序列，异常检测的目标是找出差异较大的子序列。可以看到，matrixprofile已经能够达到不错的效果。当然，还有更多复杂、fancy的算法，如频谱相关的算法等，有待进一步发掘。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
