---
template: overrides/blogs.html
---

# 微信小程序爬虫

!!! info 
    作者：Void，发布于2021年6月21日，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/PBHXRCzPUKyRLYSOkkZmLw)

Big brother是我们公司的网球王子，他总是使用某微信小程序预定网球场地。然而，热门时间段的场地总是如同变魔术一般在一瞬间被订满。  

别慌，我们有黑科技。这篇文章将教你使用Python实时监控场地情况，让你在订网球场也内卷的时代占尽先机。

## 1 软件配置

Charles是著名的抓包工具，可以抓取移动端与pc端网络访问的所有数据。我们将使用它抓取我们与小程序交互的所有信息。我们可以去官网下载适用于自己系统的[Charles安装包](https://www.charlesproxy.com/download/)

安装完成后，很重要的一步是关于证书的配置。  
以下适用于使用Windows系统的用户。  
Help -> SSL Proxying -> Install Charles Root Certificate  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654412806-vx1.png" width="600" />
  <figcaption>Install Charles Root Certificate</figcaption>
</figure>

点击安装证书  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447235-vx2.png" width="600" />
  <figcaption>安装证书</figcaption>
</figure>

点击下一步  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654592933-vx3.png" width="600" />
  <figcaption>下一步</figcaption>
</figure>

点击**将所有证书都放入下列存储**，点击浏览，选择**受信任的根证书颁发机构**  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654598065-vx4.png" width="600" />
  <figcaption>存储证书</figcaption>
</figure>

最后完成证书导入向导，提示成功。   

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447250-vx5.png" width="600" />
  <figcaption>完成证书导入</figcaption>
</figure>

我们重新进入Help -> SSL Proxying -> Install Charles Root Certificate，查看证书结果，点击**证书路径**，显示如图所示即可。  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447252-vx6.png" width="600" />
  <figcaption>查看证书结果</figcaption>
</figure>

接着点击Proxy->SSL Proxy Settings。在SSL Proxying中勾选Enable SSL Proxying并点击Add，添加Host和Port都为 * (代表监听所有IP地址的所有端口)。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-20/1624149630714-vx12.png" width="600" />
  <figcaption>Enable SSL Proxying</figcaption>
</figure>

至此，Charles就可以抓取pc端网络访问的所有数据了。  

Charles常用的工具有工具栏下面扫帚状按钮(清除当前session的数据)和摄像头状按钮(开始以及停止抓取数据)。  

## 2 探索数据 

我们在pc端登录微信，打开我们想爬取的小程序，可以看到Charles已经为我们抓取了所有的访问数据。 

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447258-vx7.png" width="600" />
  <figcaption>访问数据</figcaption>
</figure>

我们点开目标小程序：久事体育场馆(https://user.jusssportsvenue.com) 的文件夹，探索一下Charles为我们抓取了什么。  
我们点击api - common - advertising?type=1。可以看到右侧显示了这个请求的Overview。我们继续点击右上侧的Contents，可以看到底下呈现了这个请求所返回的内容。  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623661217674-vx8.png" width="600" />
  <figcaption>返回内容示例</figcaption>
</figure>

对应于小程序的正是首页的广告内容“小小体育家”。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623661222648-vx9.png" width="600" />
  <figcaption>小小体育家</figcaption>
</figure>

Charles成功为我们获取了微信小程序的内容。下一步，我们将模拟整个订网球场的流程，观察这些请求以及返回的内容，以便之后用程序获取我们想要的场地信息。

我们先关闭打开的微信小程序并点击Charles的扫帚状按钮，清除当前session的数据。我们重新打开微信小程序，点击**网球**，选择我们的目标场地：**东方体育中心**。我们选择想订的时间，例如，周二13点的三号场，点击确认提交。  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623661233694-vx10.png" width="600" />
  <figcaption>选择场地</figcaption>
</figure>

为了避免Charles获取其他不相关数据，我们点击摄像头状按钮停止抓取数据。我们重新点开久事体育场馆(https://user.jusssportsvenue.com) 的文件夹并点击api文件夹。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623661238490-wx11.png" width="600" />
  <figcaption>所有数据</figcaption>
</figure>

- common文件夹下存取的是广告与按钮相关的信息。
- venues文件夹下存取的是场地相关的信息，包括小程序上可以看到的仙霞网球中心、东方体育中心等可以预定的场地。
- block文件夹下存取的是已经被预定的场地信息。

以及和下单有关的u文件夹。u文件夹由block、order两个子文件夹以及info组成。info存储了用户的信息，从右侧Contents可以看到自己的用户名、手机号码等等。block初始化了这笔订单，并没有太多别的信息。order文件夹下包括cancel文件夹以及下订单的各种请求。其中createkBlock这个post请求对应于我们在小程序上所做的**确认订单**。blockPay代表了**立即支付**的操作。 

## 3 Python脚本

下面我们将尝试使用Python，自动化的帮我们获取场地信息。我们按照[两分钟打造淘宝抢单机器人](https://mp.weixin.qq.com/s/du-t9DyeC2INQsXg1m1xOQ)文章所述，打开notebook。  

第一步，导入所需要的包。  

```python
import requests
import random
import time
import re
import json
```

第二步，我们在Charles中观察到，block -> ground文件夹下的请求返回了场地的信息。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-20/1624149638885-vx13.png" width="600" />
  <figcaption>所有数据</figcaption>
</figure>

从Overview中我们可以拿到请求的URL。我们获取了未来几天的场地信息的URL。  

```python
urls=[ 'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624204800000&skuId=5'#周一
      ,'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624291200000&skuId=5'#周二
      ,'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624032000000&skuId=5'#周六
      ,'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624118400000&skuId=5'#周日
      ]
```

第三步，用Python提交请求，获取场地信息。

```python
response = requests.get(urls[0],verify=False)
data=response.text
data1=json.loads(data)
orders=data1['data']['modelList']
this_orders=orders[0]
this_block=this_orders['blockModel'][0]
```

我们打印一下获得的场地信息。

```python
print(this_block) 

{'groundId': 41,
 'groundName': '1号场',
 'id': '41-1号场-0',
 'isCheckout': False,
 'isChoosing': False,
 'isNormal': True,
 'orderId': '202106141200125481',
 'price': 30.0,
 'source': 1,
 'sportsType': 11,
 'status': 0,
 'userAvatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/gq1EeEEFPQ9ob3aibUn7s9VpKoCjwmRIc5wKxKPqsdj06TwjHIoeC7icw6ibzJzYMC2lJvwRiay3wvvbXK2hwe2j5Q/132',
 'userId': 4919,
 'userName': 'xxx', #友情打码
 'userPhone': 'xxx' #友情打码}
```

Bingo！我们成功使用Python获取了未来几天的场地的信息，下面我们将把代码整合起来。  
我们融入了一些自己的需求，如只考虑工作日晚上及周末的场地以及如果有空的场地就给自己的邮箱发邮件等。最终的代码如下：  

```python
import requests
import random
import time
import re
import json

user_agent_list = [
    'Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 MicroMessenger/7.0.10.1580(0x27000A5E) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']


header = {
    'Host': 'user.jusssportsvenue.com',
    'Connection': 'keep-alive',
    'accept': 'application/json',
    'charset': 'utf-8',
    'content-type': 'application/x-www-form-urlencoded',
    'User-Agent': random.choice(user_agent_list),
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://servicewechat.com/wx0fa97a8b900cb199/19/page-frame.html'
}


urls=[ 'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624204800000&skuId=5'#周一
      ,'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624291200000&skuId=5'#周二
      ,'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624032000000&skuId=5'#周六
      ,'https://user.jusssportsvenue.com/api/block/ground/list?venuesId=14&sportsType=11&startTime=1624118400000&skuId=5'#周日
      ]

def send_email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart  
    
    _user = "XXX"
    _pwd  = "XXX"
    _to   = "XXX"
    
    msg = MIMEMultipart('related')
    msg = MIMEText('has room')
    msg["Subject"] = "Tennis booking"
    msg["From"]    = _user
    msg["To"]      = _to
    
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print ("Success!")
    except smtplib.SMTPException:
        print ("Falied")
        
id=True
while id:
    for u in range(len(urls)):

        pattern = re.compile('startTime=(.*)&',re.S)
        starttime = int(re.findall(pattern, urls[u])[0])
        response = requests.get(urls[u],headers=header,verify=False)
        data=response.text
        data1=json.loads(data)
        orders=data1['data']['modelList']
        for i in orders:
            if u<2 and i['startTime']/1000<starttime/1000+64800:
                continue
            for j in i['blockModel']:
                if j['status']!=0:
                    send_email()
                    print('has room!') 
                    id=False
                    break
        time.sleep(3)
```

我们只需要运行这段代码，如果有空的场地，Python将自动的给我们的邮箱发送邮件。我们只需要及时下单预定场地即可。


