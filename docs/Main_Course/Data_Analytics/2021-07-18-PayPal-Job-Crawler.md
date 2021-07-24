---
template: overrides/blogs.html
---

# Python爬虫应用 - 职位抓取

!!! info
    作者：袁子弹起飞，发布于2021-07-18，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

金三银四刚过去没多久，秋招又即将到来，在忙碌又卷的季节，笔者曾经幻想着能一键抓取心仪公司所有的职位，然后根据自己的强项和求职意愿逐个击破，收货一篮子offer。其实，借助Python就能轻易完成这个目标的第一步，这篇文章将以著名金融科技公司PayPal官网为例，展示Python自动批量抓取职位的小技巧，帮你在求职路上快人一步!

注：本文用于学习研究Python编程技巧，如果侵权，将立即删除。

## 2 准备工作

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-19/1626696168541-PayPal%20job.png" width="700" />
  <figcaption>PayPal招聘官网</figcaption>
</figure>

首先，查看PayPal求职官网的结构，所发布的职位以列表的形式展示，点击列表里的职位，就可以跳转到对应的详情页。同时，某些国家和地区的职位比较多，分成了多页显示，则URL会以相应的页面编号来区分，例如`https://jobsearch.paypal-corp.com/en-US/search?facetcitystate=san%20jose,ca&pagenumber=2`。所以可以判断大致需要如下几步即可抓取到每个职位的详情：

- 定位职位列表，找到每个职位对应的URL
- 遍历所有页面，重复完成上述操作，存储所有职位URL
- 通过职位的URL，访问职位描述，定位详情所在的位置，并保存职位描述

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-19/1626698254470-JD.png" width="700" />
  <figcaption>PayPal职位描述</figcaption>
</figure>

## 3 用代码构建爬虫

Python环境的配置请参考之前的文章：[两分钟打造淘宝抢单机器人](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484044&idx=1&sn=ed68ae67ea2f1360053e4ecae0be3ba7&chksm=eb90f1f8dce778eeba987ea0b2f37341999418fd9541c4c7a7b1c256dbada1185e6f4c2aae87&token=261686941&lang=zh_CN#rd)

## 3.1 导入依赖的包

```Python
# 解析网页
import requests
from bs4 import BeautifulSoup

# 表格操作
import numpy as np
import pandas as pd

# 通用
import re
import os
import unicodedata
```

## 3.2 访问职位列表

```Python
# 访问URL，并取回返回结果
def url_request(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}
    r = requests.get(url, headers=header)
    print("Connection status:", r.status_code, '\n')
    return r.text
```

## 3.3 解析职位类别

```Python
# 找到页面中需要的元素，存储职位列表信息
def job_parser(html):
    header,desc,link = [[] for i in range(3)]
    soup = BeautifulSoup(html, "html.parser")
    # 右键通过打开留言器检查器，在元素tab中查看网页源码，可看到职位名称的类别名字为primary-text-color job-result-title，并且是一个a标签
    job_header = soup.find_all('a', attrs={'class': 'primary-text-color job-result-title'})
    # 元素查找方法同上
    job_link = soup.find_all('a', attrs={'class': 'primary-text-color job-result-title'}, href=True)

    header = [i.contents[0] for i in job_header]
    link = ["https://jobsearch.paypal-corp.com/"+i['href'] for i in job_link]

    # 将结果存起来
    return pd.DataFrame({'Title':header, 'Link':link})
```

## 3.4 遍历所有页面

```Python
# 创建一个存储结果的dataframe
df = pd.DataFrame(columns=['Title','Link'])
# 创建URL的模板，添加不同的页码就可匹配不同的页面
job_url_header = 'https://jobsearch.paypal-corp.com/en-US/search?facetcountry=cn&facetcity=shanghai&pagenumber='

# 遍历所有页面，并存储结果
for i in range(2):
  job_url = job_url_header + str(i+1)
  print('URL: {}'.format(job_url))
  job_html = url_request(job_url)
  # 将每个页面的结果存起来
  df = df.append(job_parser(job_html))
```

### 3.5 抓取职位详情

```Python
def get_jd(url):
  jd_html = url_request(url)
  soup = BeautifulSoup(jd_html, "html.parser")
  jd_desc = soup.find('div', attrs={'class': 'jdp-job-description-card content-card'})
  # JD格式不一，此处仅做演示
  if jd_desc:
    if jd_desc.findAll('ul')[:]:
      desc = [i.text + '\n{}'.format(j.text) for i,j in zip(jd_desc.findAll('p')[:], jd_desc.findAll('ul')[:])]
    else:
      desc = [i.text  for i in jd_desc.findAll('p')[:]]

    return unicodedata.normalize("NFKD", '\n'.join(i for i in desc))

# 对之前存储的内容使用详情抓取函数，将详情保存下来。
df['JD'] = df['Link'].apply(get_jd)

# 打印结果
df.tail(2)
```

| Title                              | Link                                                                                               | JD                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Manager, APAC Portfolio Management | https://jobsearch.paypal-corp.com//en-US/job/manager-apac-portfolio-management/J3N1SM76FQPVMX4VFZG | As the Shanghai Team Manager of PayPal APAC Portfolio Management team in GSR Enterprise Seller Risk Ops, you will manage a team of underwriters, and drive a risk management strategy and framework leveraging your strong business and financial acumen, logical reasoning and communication skills. This role will be covering the markets such as Hong Kong, Taiwan, Korea and Japan, based out of Shanghai. |
| FBO Accountant                      | https://jobsearch.paypal-corp.com//en-US/job/fbo-accoutant/J3W8C0677G8FLJQQZDL                     | Responsibilities    Timely and effective reconciliation of all assigned General Ledger accounts, including timely and accurate clearing of reconciling items in accordance with Company Policy.   Ensure accurate posting of general ledger...                                                                                                                                                                |

可以看到已经成功地抓取到了职位的信息（内容有截取）。网页上还有其他信息，你也可以根据自己的需求再继续添加信息，如果有疑问，可以添加BulletTech微信客服详细讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
