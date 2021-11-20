---
template: overrides/blogs.html
---

# 使用GitHub Action自动构建和推送Docker镜像

!!! info
    作者：袁子弹起飞，发布于2021-11-20，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

我们之前介绍了很多GitHub的酷炫功能，为了方便理解这篇文章的内容，建议阅读之前的文章回顾基本的GitHub操作知识，特别是GitHub Action：

- [一行代码都不写，教你使用GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)
- [Git常用命令一览](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)
- [玩转GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)
- [用GitHub做一份精美的在线简历](https://mp.weixin.qq.com/s/Ns0YXYQBEZbUJEJyX21L0w)
- [GitHub Action概览](https://mp.weixin.qq.com/s/aGPIfrXA3rHsg0ioFcGsBQ)

同时，如果需要理解Docker的知识，可以查看Tina老师的佳作：

- [教你成功在Win10系统中运行docker](https://mp.weixin.qq.com/s/8B9ye55zpWCCVTA4g4fLQQ)
- [Docker 初体验](https://mp.weixin.qq.com/s/gfO5BiK9fqRtWf8rjP8mPA)

在这篇文章里，我们将介绍如何使用GitHub Action自动推送Docker镜像到镜像仓库，大大简化构建镜像、推送镜像的繁琐步骤！

## 2 配置镜像仓库

这里以阿里云的镜像容器服务为例做演示，其他的镜像仓库原理类似，可以触类旁通。登录[阿里云镜像容器服务](https://cr.console.aliyun.com/cn-shanghai/instance/repositories '阿里云镜像容器服务')，进行如下操作：

- 创建命名空间（namespace），作为镜像仓库的合计，可以以公司或组织命名，如我们使用`bullettech_services`。
- 创建镜像仓库（registry），作为镜像的合集，可以存储不同版本的镜像到仓库中。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/registry.png"  />
  <figcaption>镜像仓库</figcaption>
</figure>

## 3 配置GitHub Action

### 3.1 配置密码

在GitHub仓库里设置密码，用于登录镜像容器服务。可以在仓库设置里找到密码，然后将镜像容器服务的账号和密码存储起来。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/secrets.png"  />
  <figcaption>存储镜像容器服务的账号和密码</figcaption>
</figure>

### 3.2 创建工作流

首先在`.github/workflows`目录下创建一个工作流，例如`ci.yml`，然后根据注释理解命令，并根据项目情况修改。

```yml
name: actions

on: [push, pull_request] # 触发事件

jobs:
  bt-product-release:
    if: ${{ github.ref == 'refs/heads/main' }}  # 检测main分支是否有更新
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2 # pull代码到运行服务器上
    - name: Login to Aliyun Container Registry (ACR)
      uses: aliyun/acr-login@v1 # 使用阿里云镜像服务action
      with:
        login-server: registry.cn-shanghai.aliyuncs.com # 填写镜像容器服务的登录地址
        region-id: cn-shanghai # 3
        username: "${{ secrets.REGISTRY_USERNAME }}" # 引用GitHub repo设置的镜像容器服务用户名
        password: "${{ secrets.REGISTRY_PASSWORD }}" # 引用GitHub repo设置的镜像容器服务密码
    - name: Build and Push Docker Image
      env:
        IMAGE_TAG: ${{ github.sha }} # 用于标记容器版本号
      run: |
        docker build -t registry.cn-shanghai.aliyuncs.com/bullettech_services/app:$IMAGE_TAG .
        docker push registry.cn-shanghai.aliyuncs.com/bullettech_services/app:$IMAGE_TAG
```

这样每次在main分支更新时，GitHub会基于本次更新的代码构建镜像、并将镜像推送到指定的镜像仓库（注意版本）：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/images.png"  />
  <figcaption>镜像</figcaption>
</figure>

## 4 总结

这套高效的工作流节约了许多时间，而且避免了许多手动操作时易发生的错误，GitHub Action真香啊！

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
