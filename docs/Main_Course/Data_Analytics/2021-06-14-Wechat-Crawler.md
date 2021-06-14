---
template: overrides/blogs.html
---

# 微信小程序爬虫

!!! info 
    作者：Void，发布于2021年6月8日，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/du-t9DyeC2INQsXg1m1xOQ)

# 1


Charles是著名的抓包工具，可以抓取移动端与pc端网络访问的所有数据。我们可以去官网下载适用于自己系统的[Charles](https://www.charlesproxy.com/download/)

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

至此，Charles就可以抓取pc端网络访问的所有数据了。  

Charles常用的工具有工具栏下面扫帚状按钮(清除当前session的数据)和摄像头状按钮(开始以及停止抓取数据)。  
我们在pc端登录微信，打开我们想爬取的小程序，可以看到Charles已经为我们抓取了所有的访问数据。 

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623654447258-vx7.png" width="600" />
  <figcaption>访问数据</figcaption>
</figure>

我们点开目标小程序(https://user.jusssportsvenue.com)  
