---
template: overrides/blogs.html
---

# Docker 初体验

!!! info 
    作者：Tina，发布于2021-11-05，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1. 前言

因为作者之前并没有太多产品开发和部署的经验，所以初入团队时，确实花了一段时间学习Docker概念和应用。那么今天就跟大家分享一下如何从零到一地打开Docker的大门吧。

## 2. Docker的基本概念

Docker是一个开放源代码的软件，程序员用Python、Java等面向对象的语言能够设计出产品，为什么还要使用它呢？这是因为我们在开发时需要很多特定的包和配置文件去搭建环境，如果用户想要在不同的系统环境去调用它，是一件很费时费力的事情。那么这个时候Docker就派上用场了。Docker可以帮助打包好我们产品需要的依赖包和环境，用户可以更加直接且轻松地使用我们的产品。

谈到Docker，自然离不开镜像(image)，容器（container），镜像仓库（repository）这三个概念。这里我将用一个贴近现实的比喻，帮助你更形象地理解这三个概念。

试想我们的产品是一辆小汽车，如果有消费者欣赏这款车的车型，没有Docker他可能需要从零件开始复刻这辆车的制作过程。

镜像(image)就好比这个汽车的雏形，是这台车刚生产出来的样子，只有轮胎，发动机，方向盘等基础配件。镜像在这里决定着一款车的汽车型号。

容器，就相当于一款车型在市场中为了迎合不同口味的而设计出的不同版本，如豪华版，简易版等，甚至买家在购买之后根据自己的喜好装饰它。也就是说，容器是基于镜像的运用实例。容器和容器之间是相互独立的，但有可能是来源于同一个镜像。通过命令，我们可以创建，运行，停止和删除容器。

镜像仓库，就像是停车场，存放着各种各样不同的车。这个比较好理解，这个仓库概念很像Github Repo，是存放所有镜像的地方。

构建镜像的最常见的方式之一，是创建Dockerfile。在上面的例子中，就相当于设计汽车的蓝图。Dockerfile需要和程序的主函数同时存放在根路径下面，方便运行时找到所有你需要的文件。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Dockerfile.png" width="500" />
  <figcaption>Dockerfile 存放规则 </figcaption>
</figure>


## 3. Docker的部署流程

### 3.1 创建Dockerfile

简单介绍一下[Dockerfile](https://docs.docker.com/engine/reference/builder/ "Dockerfile")的组成元素：
```Docker
FROM           <code_version>    # 指定基础镜像
MAINTAINER     <name>            # 指明镜像的创建者
# 指定本地路径并添加文件（本地文件的添加,官方更推荐COPY）
COPY           </local/path/filename>  
RUN            <command>         # 创建镜像的命令
#指定路径添加文件 (ADD不仅可以解压本地 tar file，还可以从URL中拷贝文件)
ADD            </path/filename>  
WORKDIR        <absolute path dir>   # 指定镜像的工作目录
EXPOSE         <port>            #指定交互端口    
CMD            <e.g. python run main.py>    # 启动镜像的命令
```

### 3.2 创建镜像

这里介绍三种常用的创建镜像的方式：

```Docker
# 1.基于当前路径的Dockerfile创建
docker build .  

# 2.基于github URL 路径寻找Dockerfile来创建
docker build github.com/creack/docker-firefox 

# 3.基于本地Dockerfile创建
docker build -t /path/to/Dockerfile .
```

### 3.3 运行容器

容器就是运行起来的镜像，通过查看镜像选择你想要运行的镜像就可以启动容器。

- 后台模式运行`-d`：
```Docker
docker run --name mycontainer -d myimage:latest  
```
使用docker镜像myimage:latest以后台模式运行容器并命名为mycontainer。

- 指定端口运行`-p`：
```Docker
docker run -p 127.0.0.1:80:8000/tcp ubuntu bash
```
绑定容器8080端口，并将其映射到本机127.0.0.1的80端口上。tcp代表端口协议，进入ubuntu系统使用bash命令运行容器。

- 分配虚拟终端`-it`:
```Docker
docker run --name mycontainer -it myimage:latest
```
`-it`表示让Docker分配一个虚拟的终端给容器运行。

如果你想要更加详细的了解Docker run，请参考[官方文档](https://docs.docker.com/engine/reference/run/ "Docker run refernce")。

### 3.4 Docker其他常用命令

最后，附上常用的基本操作可以帮助你快速地操作和推送创建好的镜像服务。

```Docker
docker pull <regsitry_path> # 从私有或公共仓库拉取镜像
docker images # 查看镜像
docker ps # 列举当前正在运行的容器
docker ps -a | grep <test> #查看test容器信息
docker stats #查看正在使用的运行资源
docker container logs <container_id> # 查看日志
docker stop <container_id> #停止容器
docker start <container_id> #启动stop的容器
docker rm <container_id> #删除容器
docker push <registry_path>[image_version] #推送镜像到远端仓库
docker image prune  #删除悬空镜像
docker container prune # 清理stopped容器
docker container prune --filter "container id" #不清理特定的容器ID
docker rm -v $(docker ps -aq -f status=exited) #删除已退出的所有容器
```

## 4. 总结

看上去这些概念很抽象，特别是对于从未接触过这方面知识的人而言（比如作者本人）。但当自己反复阅读思考加上实践，发现这套东西并没有多复杂，它只是帮助你部署网页等产品的工具而已。下期我们将展开说说如何在容器中持续化地管理数据。

希望这篇分享可以在你探索Docker之路时有所帮助，欢迎大家留言讨论。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
