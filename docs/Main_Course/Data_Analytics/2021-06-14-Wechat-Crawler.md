---
template: overrides/blogs.html
---

# 微信小程序爬虫

!!! info 
    作者：Void，发布于2021年6月8日，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/du-t9DyeC2INQsXg1m1xOQ)

# 1


Charles是著名的抓包工具，可以抓取移动端与pc端网络访问的所有数据。我们可以去官网下载适用于自己系统的[Charles安装包](https://www.charlesproxy.com/download/)

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
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447252-vx12.png" width="600" />
  <figcaption>查看证书结果</figcaption>
</figure>

至此，Charles就可以抓取pc端网络访问的所有数据了。  

Charles常用的工具有工具栏下面扫帚状按钮(清除当前session的数据)和摄像头状按钮(开始以及停止抓取数据)。  
我们在pc端登录微信，打开我们想爬取的小程序，可以看到Charles已经为我们抓取了所有的访问数据。 

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447258-vx7.png" width="600" />
  <figcaption>访问数据</figcaption>
</figure>

我们点开目标小程序：久事体育场馆(https://user.jusssportsvenue.com) 的文件夹，探索一下Charles为我们抓取了什么。  
我们点击api - common - advertising?type=1。可以看到右侧显示了这个请求的Overview。我们继续点击右上侧的Contents，可以看到底下已经呈现了这个请求所返回的内容。  

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623661217674-vx8.png" width="600" />
  <figcaption>返回内容示例</figcaption>
</figure>

对应于小程序的正是首页的广告内容“小小体育家”。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623661222648-vx9.png" width="600" />
  <figcaption>小小体育家</figcaption>
</figure>

Charles成功为我们获取了微信小程序的内容。下一步，我们将模拟整个订网球场的流程，观察这些请求以及返回的内容，以便我们之后用程序实现整个订场的流程。  
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

以及我们最需要关注的u文件夹。u文件夹由block、order两个子文件夹以及info组成。info存储了用户的信息，从右侧Contents可以看到自己的用户名、手机号码等等。block初始化了这笔订单，并没有太多别的信息。order文件夹下包括cancel文件夹以及下订单的各种请求。其中createkBlock这个post请求对应于我们在小程序上所做的**确认订单**。我们点击其Contents，可以看到请求成功后会返回一个tradeId。blockPay代表了**立即支付**操作


