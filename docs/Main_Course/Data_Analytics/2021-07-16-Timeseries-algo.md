---
template: overrides/blogs.html
---

# 时间序列异常检测

!!! info 
    作者：Void，发布于2021-07-16，阅读时间：约5分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/3JlO0eO95SBqhHH4EHPypw)

## 1 引言

事情的起因是有朋友告诉我最近有KDD Cup 2021的比赛。为了凑个热闹，也为了刷点经验，我们准备合伙参加(当个炮灰)。  
有三道赛题，时间序列异常检测、图相关的和智慧城市。看上去最正常的[时间序列异常检测](https://compete.hexagon-ml.com/practice/competition/39/)当仁不让的成为了我们的选择。

## 2 题目要求

竞赛要求我们检测多个时间序列(25+250个)中的异常点。每个时间序列有且仅有一个异常点。题目给出了异常点所在的区间，要求我们给出异常点所在的位置。  
评估时会考察我们给出的位置前后100个点的范围内是否包含真正的异常点。序列长度从几千到几十万不等。



<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
