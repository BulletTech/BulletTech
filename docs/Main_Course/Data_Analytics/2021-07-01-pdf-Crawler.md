---
template: overrides/blogs.html
---

# 爬取并下载url不变的pdf文件

!!! info 
    作者：Void，发布于2021-07-02，阅读时间：约4分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/cmSw_rvSm2gYbenI02NQ7Q)

## 1 引言

为了更好的卖保险(导师要求)，需要下载[保险业协会官网](http://icid.iachina.cn/?columnid_url=201510010005#)-信息披露中保险公司披露的pdf文件。保险公司很多，每家又有不少年度披露的pdf。同时，神奇的是，无论怎么点击页面，网页的url都没有发生变化。为了拒绝当人肉爬虫，我们再次尝试使用Python帮助我们高效、自动地下载这些pdf文件。  

## 2 具体步骤

我们打开保险业协会网站，点击不同的科目，如保险公司年度信息披露，我们发现页面的url并没有发生变化。这时，请不要怀疑自己的眼睛或是砸烂电脑，我们应该合理地怀疑页面采取了某些异步请求(Ajax)的方式。  
此时，我们需要找到发送真实请求的页面。我们打开开发者工具，在Network中勾选ALL，清空后重新点击我们要选取的科目，如关联交易合并披露。神奇的事情出现了，红框中标示出来了一个新的url，那么这个url是不是我们真正要找的OnePiece呢？

```html
http://icid.iachina.cn/ICID/front/leafColComType.do?columnid=2016072012158397
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-1/1625140634123-1.jpg" width="500" />
  <figcaption>Real url</figcaption>
</figure>
        
我们进入此url。完蛋，这只是一个和上一页面神似但是长得更丑的网址。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-1/1625140619323-2.jpg" width="500" />
  <figcaption>Enter url</figcaption>
</figure>

我们破罐子破摔，点击第一家保险公司：中国人寿资产管理有限公司，同样我们发现url并没有发生变化。我们“自暴自弃”的按同样的操作观察它的XHR，发现url又变了：

```html
http://icid.iachina.cn/ICID/front/getCompanyInfos.do?columnid=2016072012158397&comCode=GSZC&attr=01
```

这下，事情似乎有转机了。我们发现似乎只需要在comCode这边赋值所有的保险公司简称即可。  
下一步就是获取所有的保险公司的简称，我们在上一页面，即

```html
http://icid.iachina.cn/ICID/front/leafColComType.do?columnid=2016072012158397
```

中，使用select an element去审查每家保险公司的名字，发现其简称都存储在控件a的id中。因此，我们可以通过遍历的方式得到所有保险公司的简称，并带入到comCode中。
以国寿资产(GSZC)为例，我们进入新的网址：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-1/1625140619330-3.jpg" width="500" />
  <figcaption>Example</figcaption>
</figure>

其中每一个pdf就是我们最终想得到的结果了，我们点击一个公告，同样查看它的XHR。

```html
http://icid.iachina.cn/front/infoDetail.do?informationno=2020012109398975
```

接下来就是要获取informationno，它在这个页面控件为a的id处。我们进入这个url。  

那么最后一步就是获取国寿资产这一年度公告的pdf了。点开公告，我们可以看到url为

```html
http://icid.iachina.cn/ICID/files/piluxinxi/pdf/viewer.html?file=8f993c5a-1c1c-4f91-a8a5-7fad85a14616.PDF
```

file名恰好也存在上一页面控件为a的id中。需要注意的是，这边是viewer方式，我们只需要原始的pdf，因此改为以下url即可。

```html
http://icid.iachina.cn/ICID/files/piluxinxi/pdf/8f993c5a-1c1c-4f91-a8a5-7fad85a14616.PDF
```

我们如同拆开套娃一般，成功拿到了最终的pdf。下面就是使用Python把它下载下来了。只需要写几个简单的循环，点击运行程序，再打开Dota2，一把dota的时间，Python已经帮我们下载完成了近1个G的pdf文件。

## 3 总结

我们往往会碰到一些需要机械、重复操作完成的请求。这时，用程序实现往往是高效、省力的选择。在这个例子中，我们使用Python成功下载了所需要的大量pdf文件。由于不同网站的构造不同，保险业协会的网站采用了异步加载的方式，导致页面的url一直保持不变。我们通过开发者工具，成功找到了发送的真实请求。


## 4 代码

最终code整理如下：

```python
from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm
import os
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}

url="http://icid.iachina.cn/front/leafColComType.do?columnid=2016072012158397"
response=requests.get(url,headers=header)
response.encoding='GBK'
soup=BeautifulSoup(response.text,'lxml')
data=soup.select('a')
n=[]
for i in data:
    try:
        n.append(i.attrs['id'])
    except:
        continue
for z in tqdm(n):

    url="http://icid.iachina.cn/front/getCompanyInfos.do?columnid=2016072012158397&comCode={}&attr=01#".format(z)
    response=requests.get(url,headers=header)
    response.encoding='GBK'
    soup=BeautifulSoup(response.text,'lxml')
    data=soup.select('a')
    l=[]
    name=[]
    for i in data:
        try:
            l.append(i.attrs['id'])
            name.append(i.text)
        except:
            continue
    l=l[:-1]
    name=name[:-1]
    for j in range(len(l)):
        url="http://icid.iachina.cn/front/infoDetail.do?informationno={}".format(l[j])
        response=requests.get(url,headers=header)
        response.encoding='GBK'
        soup=BeautifulSoup(response.text,'lxml')
        data=soup.select('a')
        link=data[1].attrs['id']

        url="http://icid.iachina.cn/files/piluxinxi/pdf/{}".format(link)
        response=requests.get(url,headers=header)
        pdf = response.content
        #写入pdf
        c=0
        with open(r"C:\Users\admin\Desktop\关联\auto\{}.pdf".format(name[j]),'wb') as f:
            f.write(pdf)
        while os.path.getsize(r'C:\Users\admin\Desktop\关联\auto\{}.pdf'.format(name[j]))==0:
            time.sleep(3)
            url="http://icid.iachina.cn/files/piluxinxi/pdf/{}".format(link)
            response=requests.get(url,headers=header)
            pdf = response.content
            with open(r"C:\Users\admin\Desktop\关联\auto\{}.pdf".format(name[j]),'wb') as f:
                f.write(pdf)  
            c+=1
            if c>=5:
                break
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
