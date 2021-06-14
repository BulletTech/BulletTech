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
点击安装证书  
点击下一步  
点击**将所有证书都放入下列存储**，点击浏览，选择**受信任的根证书颁发机构**  
最后完成证书导入向导，提示成功。   

我们重新进入Help -> SSL Proxying -> Install Charles Root Certificate，查看证书结果，点击**证书路径**，显示如图所示即可。  
至此，Charles就可以抓取pc端网络访问的所有数据了。  

Charles常用的工具有工具栏下面扫帚状按钮(清除当前session的数据)和摄像头状按钮(开始以及停止抓取数据)。  
我们在pc端登录微信，打开我们想爬取的小程序，可以看到Charles已经为我们抓取了所有的访问数据。  
我们点开目标小程序(https://user.jusssportsvenue.com)  
