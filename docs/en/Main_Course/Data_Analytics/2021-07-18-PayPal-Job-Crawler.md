---
template: overrides/blogs.html
tags:
  - python
  - automation
---

# Python爬虫应用 - PayPal职位抓取

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-07-18，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484353&idx=1&sn=fa3c49192bd8ba303b2d796364a6a088&chksm=eb90f0b5dce779a31d0d8eae377ab8d453f65c7b046b5fc973303d6f14a340670601420321af&token=447292391&lang=zh_CN#rd)

## 1 Introduction


It wasn't long before Jin Sanyin Si had just passed, and the autumn recruitment was coming again. In the busy and rolled season, I once imagined that I could grasp all the positions of the company's company with one click, and then broke according to my strength and the willingness to apply for job application.Basket offer.In fact, with the help of python, you can easily complete this goal. This article will take the official website of the famous fintech company Paypal as an example to display the tips for automatic batch of positioning of Python to help you one step on the job search road!




!!! warning
Note: This article is only used to learn Python programming skills. If infringement, it will be deleted immediately.


## 2 Preparation


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-19/1626696168541-PayPal%20job.png" width="700" />

<figcaption> PayPal Recruitment </figcaption>
</figure>


First of all, check the structure of the official website of PayPal.At the same time, there are many positions in some countries and regions. When it is divided into multiple pages, URL will distinguish it with the corresponding page number, such as `https://jobsearch.paypal-corp.com/en-search?FacetCityState= san%20Jose, CA & Pagenumber = 2 `.Therefore, the details of judgment need to be taken as follows to grasp the details of each position:


-Preate the position list and find the URL corresponding to each position
-The through all pages, repeatedly complete the above operations, and store all positions URL
-In the URL of the position, visit the position description, locate the location of the details, and save the position description


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-19/1626698254470-JD.png" width="700" />

<figcaption> PayPal Position Description </figcaption>
</figure>


## 3 Use code to build crawlers


For the configuration of the Python environment, please refer to the previous article:
[Two minutes to build Taobao single robot] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq==&mid=22474844 enfilledx=1&ED67EA2F1360053be3ba7&CH KSM = EB90F1F8DCE778EEBA987EA0B2F37341999418FD9541C4C7A7B1C256DBADA1185E6F4C2AE87 & Token = 261686941 & LANG = zh_cn#RD)


### 3.1 Import dependent bags


```Python
# Analysis webpage
import requests
from bs4 import BeautifulSoup


# 表 表
import numpy as np
import pandas as pd


# # 通
import re
Import us
import unicodedata
```


### 3.2 Visit position list


```Python
# URL, and retrieve the return result
def url_request(url):
header = {
'User-Agent': 'Mozilla / 5.0 (Windows NT 6.1) Applewebkit / 537.3,159.159.1599.101 / 537.36'}
r = requests.get(url, headers=header)
print('Connection status:', r.status_code, '\n')
return r.text
```


### 3.3 Analysis job category


```Python
# Find the required elements in the page, storage position list information
def job_parser(html):
header,desc,link = [[] for i in range(3)]
soup = BeautifulSoup(html, 'html.parser')
# Right-click by turning on the browser checker, check the web source code in the element TAB, you can see that the category name of the position name is Primary-Text-COLOR job-result-title, and it is an A tag
job_header = soup.find_all('a', attrs={'class': 'primary-text-color job-result-title'})
# Element search method is the same as above
job_link = soup.find_all('a', attrs={'class': 'primary-text-color job-result-title'}, href=True)


header = [i.contents[0] for i in job_header]
link = ['https://jobsearch.paypal-corp.com/'+i['href'] for i in job_link]


# Move the result up
return pd.DataFrame({'Title':header, 'Link':link})
```


### 3.4 to pass all pages


```Python
# Create a dataframe of the storage result
df = pd.DataFrame(columns=['Title','Link'])
# Create a template for URL, add different page numbers to match different pages
job_url_header = 'https://jobsearch.paypal-corp.com/en-US/search?facetcountry=cn&facetcity=shanghai&pagenumber='


#Prink through all pages and store results
for i in range(2):
job_url = job_url_header + str(i+1)
print('URL: {}'.format(job_url))
job_html = url_request(job_url)
# Save the results of each page
df = df.append(job_parser(job_html))
```


### 3.5 Grabbing position details


```Python
def get_jd(url):
jd_html = url_request(url)
soup = BeautifulSoup(jd_html, 'html.parser')
jd_desc = soup.find('div', attrs={'class': 'jdp-job-description-card content-card'})
# Jd formats are different, only a demonstration here
if jd_desc:
if jd_desc.findAll('ul')[:]:
desc = [i.text + '\n{}'.format(j.text) for i,j in zip(jd_desc.findAll('p')[:], jd_desc.findAll('ul')[:])]
else:
desc = [i.text  for i in jd_desc.findAll('p')[:]]


return unicodedata.normalize('NFKD', '\n'.join(i for i in desc))


#At the details of the previously stored content to capture the function and save the details.
df['JD'] = df['Link'].apply(get_jd)


# Print results
df.tail(2)
```


| Title                              | Link                                                                                               | JD                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Manager, APAC Portfolio Management | https://jobsearch.paypal-corp.com//en-US/job/manager-apac-portfolio-management/J3N1SM76FQPVMX4VFZG | As the Shanghai Team Manager of PayPal APAC Portfolio Management team in GSR Enterprise Seller Risk Ops, you will manage a team of underwriters, and drive a risk management strategy and framework leveraging your strong business and financial acumen, logical reasoning and communication skills. This role will be covering the markets such as Hong Kong, Taiwan, Korea and Japan, based out of Shanghai. |
| FBO Accountant                      | https://jobsearch.paypal-corp.com//en-US/job/fbo-accoutant/J3W8C0677G8FLJQQZDL                     | Responsibilities    Timely and effective reconciliation of all assigned General Ledger accounts, including timely and accurate clearing of reconciling items in accordance with Company Policy.   Ensure accurate posting of general ledger...                                                                                                                                                                |


You can see the information that has been successfully grasped (interception).There are other information on the webpage. You can also continue to add information according to your needs. If you have any questions, you can add Bullettech WeChat customer service to discuss in detail!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>