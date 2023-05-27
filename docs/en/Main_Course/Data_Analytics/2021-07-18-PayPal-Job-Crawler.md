---
template: overrides/blogs.html
tags:
  - python
  - automation
---

# Python Web Scraping Application - Scraping PayPal Job Positions

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published: 2021-07-18, Reading Time: About 6 minutes, WeChat public account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484353&idx=1&sn=fa3c49192bd8ba303b2d796364a6a088&chksm=eb90f0b5dce779a31d0d8eae377ab8d453f65c7b046b5fc973303d6f14a340670601420321af&token=447292391&lang=zh_CN#rd)

## 1 Introduction

Not long after the traditional job-hunting season (around March/April in China), the autumn job-hunting season is approaching. In this busy and stressful period of time, I once dreamed of being able to grab all the job positions of my target companies with one click, and then conquer them one by one based on my strengths and job-seeking desires, and get a basketful of offers. In fact, we can easily accomplish the first step of this goal using Python. This article will take the official website of PayPal, a well-known financial technology company, as an example to demonstrate the small technique of automatically scraping job positions with Python, and help you take a faster step on the job-hunting path!

!!! warning
    Note: This article is for learning and researching Python programming techniques only. If any infringement is found, it will be deleted immediately.

## 2 Preparation

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-19/1626696168541-PayPal%20job.png" width="700" />
  <figcaption>PayPal recruitment website</figcaption>
</figure>

First of all, check the structure of the PayPal job search website. The released job positions are displayed in the form of a list, and clicking on a position in the list will take us to its corresponding details page. At the same time, some job positions in certain countries and regions are relatively large in quantity and are displayed on multiple pages, with URLs distinguished by their corresponding page numbers, such as `https://jobsearch.paypal-corp.com/en-US/search?facetcitystate=san%20jose,ca&pagenumber=2`. Therefore, we can roughly crawl the details of each job position by performing the following steps:

- Locate the list of job positions and find the URL corresponding to each job position
- Traverse all pages and repeat the above operation to store all job positions URLs
- Access the job position description through the URL of the job position, locate the position of the details, and save the job position description

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-19/1626698254470-JD.png" width="700" />
  <figcaption>PayPal job position description</figcaption>
</figure>

## 3 Building the Web Scraper with Python Code

Please refer to the previous article [Two-minute Taobao Order Grab Robot](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484044&idx=1&sn=ed68ae67ea2f1360053e4ecae0be3ba7&chksm=eb90f1f8dce778eeba987ea0b2f37341999418fd9541c4c7a7b1c256dbada1185e6f4c2aae87&token=261686941&lang=zh_CN#rd) for Python environment configuration.

### 3.1 Importing Dependent Packages

```Python
# Parsing web pages
import requests
from bs4 import BeautifulSoup

# Table operation
import numpy as np
import pandas as pd

# Common
import re
import os
import unicodedata
```

### 3.2 Accessing the Job Position List

```Python
# Request the URL and get the returned result
def url_request(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}
    r = requests.get(url, headers=header)
    print('Connection status:', r.status_code, '\n')
    return r.text
```

### 3.3 Parsing Job Position Categories

```Python
# Find the elements needed in the page and store the job position list information
def job_parser(html):
    header,desc,link = [[] for i in range(3)]
    soup = BeautifulSoup(html, 'html.parser')
    # Right-click to open the browser inspector, check the page source code, and you can see that the name of the job position category is "primary-text-color job-result-title", which is an a tag
    job_header = soup.find_all('a', attrs={'class': 'primary-text-color job-result-title'})
    # Element lookup method is the same as before
    job_link = soup.find_all('a', attrs={'class': 'primary-text-color job-result-title'}, href=True)

    header = [i.contents[0] for i in job_header]
    link = ['https://jobsearch.paypal-corp.com/'+i['href'] for i in job_link]

    # Save the result
    return pd.DataFrame({'Title':header, 'Link':link})
```

### 3.4 Traverse All Pages

```Python
# Create a dataframe to store the result
df = pd.DataFrame(columns=['Title','Link'])
# Create a URL template and add different page numbers to match different pages
job_url_header = 'https://jobsearch.paypal-corp.com/en-US/search?facetcountry=cn&facetcity=shanghai&pagenumber='

# Traverse all pages and store the results
for i in range(2):
  job_url = job_url_header + str(i+1)
  print('URL: {}'.format(job_url))
  job_html = url_request(job_url)
  # Store the results of each page
  df = df.append(job_parser(job_html))
```

### 3.5 Scraping Job Position Details

```Python
def get_jd(url):
  jd_html = url_request(url)
  soup = BeautifulSoup(jd_html, 'html.parser')
  jd_desc = soup.find('div', attrs={'class': 'jdp-job-description-card content-card'})
  # JD formats are different, here are just demonstrations
  if jd_desc:
    if jd_desc.findAll('ul')[:]:
      desc = [i.text + '\n{}'.format(j.text) for i,j in zip(jd_desc.findAll('p')[:], jd_desc.findAll('ul')[:])]
    else:
      desc = [i.text  for i in jd_desc.findAll('p')[:]]

    return unicodedata.normalize('NFKD', '\n'.join(i for i in desc))

# Use the detail scraping function on previously stored content, and save detail information.
df['JD'] = df['Link'].apply(get_jd)

# Print the result
df.tail(2)
```

| Title                              | Link                                                                                               | JD                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Manager, APAC Portfolio Management | https://jobsearch.paypal-corp.com//en-US/job/manager-apac-portfolio-management/J3N1SM76FQPVMX4VFZG | As the Shanghai Team Manager of PayPal APAC Portfolio Management team in GSR Enterprise Seller Risk Ops, you will manage a team of underwriters, and drive a risk management strategy and framework leveraging your strong business and financial acumen, logical reasoning and communication skills. This role will be covering the markets such as Hong Kong, Taiwan, Korea and Japan, based out of Shanghai. |
| FBO Accountant                      | https://jobsearch.paypal-corp.com//en-US/job/fbo-accoutant/J3W8C0677G8FLJQQZDL                     | Responsibilities    Timely and effective reconciliation of all assigned General Ledger accounts, including timely and accurate clearing of reconciling items in accordance with Company Policy.   Ensure accurate posting of general ledger...                                                                                                                                                                |

We can see that we have successfully scraped job position information (with some text truncated). There is other information on the web page, and you can add more information according to your needs. If you have any questions, feel free to contact us via the BulletTech WeChat customer service! 

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>