---
template: overrides/blogs.html
---

# 教你成功在Win10系统中运行docker

!!! info 
    作者：Tina，发布于2021-11-13，阅读时间：约5分钟，微信公众号文章链接：[:fontawesome-solid-link:]()
    
## 1 前言
在上文[Docker初体验](https://mp.weixin.qq.com/s/gfO5BiK9fqRtWf8rjP8mPA)中我们介绍了Docker的一些基本概念和常用命令，但因为Docker是在Linux系统下创建的资源分离机制，所以它无法在Windows系统下直接运行。这次我们将用3分钟的时间介绍一下如何在Win10系统下运行Docker。

## 2 下载Docker
用户可以根据自己的系统在Docker官网选择[Mac](https://docs.docker.com/desktop/mac/install/ 'Install docker in Mac')或[Windows](https://docs.docker.com/desktop/windows/install/#install-docker-desktop-on-windows 'Install docker in Windows')，因为Docker可以在Mac系统中安装后可以直接运行，这里就不再赘述。

安装完Docker，并注册个人账号，再双击启动它，你会发现并不像你想的那么顺利。错误信息如下图所示：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/failed.jpg" width="500" />
  <figcaption> Docker启动失败 </figcaption>
</figure>

这是因为Docker无法在Windows系统中直接运行，而需要创建一个Wins系统中的Linux虚拟机（VM）为Docker的正常运行搭建好底层依赖。虽然[官方文档](https://docs.docker.com/desktop/windows/install/#wsl-2-backend 'WSL2的安装')提供了hyper-V和WSL2两种解决方案，但是WSL2是基于hpyer-v在WSL1的升级版，其功能，安装方式也简单方便，因此作者就选择了WSL2的后端方式来运行Docker。

## 3 安装WSL2
WSL，Windows Subsystem for Linux，含义就是在Windows系统下Linux的子系统。只需要三步就可以在系统中为docker安装WSL2了，请注意目前WSL2支持在Windows10 2004以上的版本。

### 3.1 开启WSL2功能
首先，打开`Powershell`命令提示符，运行命令先查看网上所有的子系统， 再选择你想要选择的系统，这里我们将选择Ubuntu来进行安装。

```shell
## 查看list
wsl --list --online
## 安装Linux distribution
wsl --install -d Ubuntu
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/terminal-1.jpg" width="500" />
  <figcaption> 查看WSL列表 </figcaption>
</figure>

安装成功后，结果返回会让你创建UNIX的用户名和密码：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/create-account.jpg" width="500" />
  <figcaption> 创建用户名和密码 </figcaption>
</figure>

细心的你会发现命令提示符左上方的logo已经变成了Ubuntu的了。

### 3.2 安装更新包
安装成功后，还需要下载Linux安装更新包，具体操作需要参考[Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package 'Install update package')官方文档根据你自己系统的版本选择合适的更新包。

### 3.3 设置默认版本
打开命令提示符，设置WSL2为Linux distribution的默认版本：

```shell
wsl --set-default-version 2
```


## 4 检查docker设置
成功安装好Linux distribution后，还需要在docker desktop中设置一下关于WSL2的基本参数才能确保docker的成功运行。

首先，需要在通用设置下，勾选使用WSL2基础的引擎，如图所示：
<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/docker-1.png" width="500" />
  <figcaption> 基于WSL2引擎</figcaption>
</figure>

其次，需要在资源中设置WSL整合，此操作是帮助你在拥有多个WSL时可以整合组成部分的。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/docker-2.png" width="500" />
  <figcaption> 设置WSL整合资源 </figcaption>
</figure>

最后，重启docker desktop，你会看到成功启动的界面。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/success.jpg" width="500" />
  <figcaption> 成功界面 </figcaption>
</figure>

## 总结
有些软件在电脑中的成功运行会因为系统的不兼容，需要一些先决条件。不管是参考具体的官方文档还是搜索一些避雷的经验贴，安装成功并使用后，你会发现这些环境的搭建是一劳永逸的，快尝试在你的Windows系统中运行docker吧！之后我们还会持续分享docker的学习经验，敬请期待。

希望这次的分享能对你有所帮助，欢迎留言讨论。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>


