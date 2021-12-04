---
template: overrides/blogs.html
---

# 获取租房房源数据

!!! info
    作者：Echo，发布于2021-12-04，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/NHgnYaelpcDKYWnAqL6vSw)

## 1 前言

租房/有房要出租的小伙伴们看过来~ 
衣食住行是生活的基本需求。衣和食好解决，不喜欢的衣服可以买新的，不好吃的食物可以换一家吃。可是在住宿上，买房和租房的置换成本都相对较高，因此房源选择尤为慎重。作为目前买不起房的自然人，我们一般是通过中介来实现租房的需求，比如自如，贝壳找房和链家。看来宇宙的尽头是铁岭，租房的尽头是链家……  
链家占据了租赁市场的主导地位，且提供的信息相对公允。但每当我刷超过十个房源，我就会记不起来每一个的信息，也无法可视化去比较很多个房源。那么让我们开始动手，用万能的Python来让链家变成你家，获取链家网上的你想要的信息吧。（真的不是广告）


## 2 获取房源数据

此次侧重XPath的使用和反爬虫小技巧。XPath是用路径表达式在XML文档中选取节点，这里也同样适用于HTML文档的搜索。

### 2.1 确定URL

打开上海链家网的租房页面，选择筛选条件，示例如下。确认后地址栏的URL会根据筛选条件而发生变化。（当然如果没有想好想要住的区域，地铁线，租金，面积，朝向，户型也没有关系，可以直接爬取全部的上海房源数据。）

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/SH_rent.PNG" width="500"/>
</figure>

共计28页房源信息，点击切换下一页，观察URL会发现链家网是静态的网页，页面切换通过在URL中加入pg{i}参数实现。因此我们只要能爬取一页的信息，就可以通过参数循环来爬取所有页面。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/SH_rent05.PNG" width="500"/>
</figure>

### 2.2 解析页面
按F12打开开发者工具，在页面中选择一个元素以进行检查。可以看到右侧的房源列表模块和左边的房源信息是一一对应的。左侧的每一条房源信息都等价于右侧的class属性为content__list--item的一个div图层。因此我们只需要观察了解第一个房源信息即可。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/SH_rent01.PNG" width="500"/>
</figure>

继续展开这个div图层，会发现我们需要的信息基本都被包含在属性为content__list--item--main的子div图层中，尤其是其中几个class为title，description，price的元素里。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/SH_rent03.PNG" width="500"/>
</figure>

以属性为content__list--item--title的paragraph为例，其中包含了租赁方式，街区，房屋朝向等信息。我们可以用XPath来匹配和定位到这个段落，取出里面的文本。常用的匹配规则为 / 代表选取直接子节点，// 代表选择所有子孙节点，. 代表选取当前节点，.. 代表选取当前节点的父节点，@ 则是加了属性的限定，选取匹配属性的特定节点。下面是租赁方式（整租/合租）的匹配方式。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/SH_rent04.PNG" width="500"/> 
</figure>

```python
LeaseMethod = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a/text()')[0].strip().split(' ')[0].split('·')[0]
```
以此类推，我们可以轻易的取出街区，租赁方式，朝向，每月租金，行政区，板块，房屋面积，格局和发布时长等信息。

### 2.3 反爬虫解决措施
网站的反爬措施有很多，比如检测访问请求头。且如果一个header短期频繁发送请求，也很容易被识别。这种情况下可以通过添加多个请求头，每次随机选取一个header，伪装成浏览器访问；且设置time sleep，每次发送请求随机间隔一段时间来防止出现error403/404。还有一些方法如添加Referer，host，代理IP等，这里不做过多阐述，感兴趣的小伙伴欢迎自行探索。

完整代码和最终结果如下。可以看到第一步在链家主页搜索时显示的828条记录已经全部获取到数据框中。可以进行下一步的分析啦！


```python
import requests
from lxml import etree
import random
import time
import pandas as pd

#伪装请求头
user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

def getHeaders():
    user_agent = user_agents[random.randint(0, len(user_agents)-1)] 
    headers = {
        'User-Agent': user_agent
    }
    return headers


#对一个URL发送请求，解析结果，获取所需数据
def get_data(url):
    #反爬虫策略1：随机取headers
    response = requests.get(url, headers=getHeaders(), stream=True)
    tree = etree.HTML(response.text)
    # 定位到content__list
    li_list = tree.xpath('//div[@class="content w1150"]/div[@class="content__article"]/div[@class="content__list"]/div')
    # all_house_list = []
    for li in li_list:
        #下面是两种定位方式，都可
        # Nbhood = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a[@class="twoline"]/text()')[0].strip().split(' ')[0].split('·')[1]
        Nbhood = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a/text()')[0].strip().split(' ')[0].split('·')[1]
        LeaseMethod = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a/text()')[0].strip().split(' ')[0].split('·')[0]
        HouseOrientation = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a/text()')[0].strip().split(' ')[2]
        Rent = li.xpath('.//div[@class="content__list--item--main"]/span[@class="content__list--item-price"]/em/text()')[0]
        District = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--des"]/a/text()')[0]
        Location = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--des"]/a/text()')[1]
        Size = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--des"]/text()')[4].strip()
        HouseType = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--des"]/text()')[6].strip()
        releaseTime = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--brand oneline"]/span[@class="content__list--item--time oneline"]/text()')[0]
        Link = li.xpath('.//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a[@class="twoline"]//@href')[0]
        all_house_list.append((Nbhood,LeaseMethod,HouseOrientation,Rent,District,Location,Size,HouseType,releaseTime))
        
    return all_house_list

#循环爬取所需租房信息
pages = ['https://sh.lianjia.com/ditiezufang/li143685063/pg{}rt200600000001l1l0ra1ra2ra0rp5rp6/'.format(x) for x in range(1,29)]
all_house_list = []
count = 0
for page in pages:
    a = get_data(page)
    #反爬虫策略2：每次爬取随机间隔3-10s
    time.sleep(random.randint(3,10))
    count=count+1
    print ('the '+str(count)+' page is sucessful')

name = ["街区", "租赁方式", "朝向", "每月租金", "行政区","板块","房屋面积","格局","发布时长"]
page_data = pd.DataFrame( columns= name,data=all_house_list)
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/SH_rent02.PNG" width="500" />
</figure>


## 3 总结

一句话总结，爬取数据的本质就是观察和找规律。那么祝大家找到满意的房子！有时间的话下次写写基于获取的房源信息做的分析，当然，如果鸽了的话当我没说~

