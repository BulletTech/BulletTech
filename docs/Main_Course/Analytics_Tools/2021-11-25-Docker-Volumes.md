---
template: overrides/blogs.html
---

# Docker之数据可持续化

!!! info
    作者：Tina，发布于2021-11-25，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言
在[Docker初体验](https://mp.weixin.qq.com/s/gfO5BiK9fqRtWf8rjP8mPA)一文中我们介绍了Docker的基本概念，之后我们又分享了如何[教你成功在Win10系统中运行docker](https://mp.weixin.qq.com/s/8B9ye55zpWCCVTA4g4fLQQ)和[使用GitHub Action自动构建和推送Docker镜像](https://mp.weixin.qq.com/s/BCzu346DvNga84vEUXUbTQ)，尝试过的朋友应该可以在Docker中为自己的程序代码创建镜像，运行容器，或是在`github action`中使用Docker等基本操作。今天，我们将说说如何Docker中持续化管理数据--数据卷(Volumes)的使用。

## 2 管理数据的必要性
初次体验Docker的人可能会发现，每当我们重启容器时，之前的数据都会丢失，又或是感觉数据很难转移。这些都是因为Docker的默认设置会将所有的文件都创建在一个容器中的某些可读容器层。换句话说，一个容器的数据是独立不能共享的，为了实现数据共享和数据迁移，就需要我们使用一些方法可持续化地管理数据。

## 3 关于Volumes
### 3.1 优势
Volumes是一种由Docker创建并维护的数据管理机制。如下图所示，它最大的特点是将文件存放在Docker主机内，是不允许其他程序的访问，在不同容器间共享数据时具有较高的安全性；且可直接用Docker命令进行数据备份和数据迁移。除此之外，Volumes在Docker Desktop的表现性能比其他方式更加出色，这也是官方最推荐的方式。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/difference_ploy.png"  />
  <figcaption>来自：Docker官方文档</figcaption>
</figure>

### 3.2 Volumes常见操作
这里参考[官方文档](https://docs.docker.com/storage/volumes/ 'Docker Volumes')，我们介绍几种不同情况下对Volumes的使用。

1.我们可通过以下基本命令创建及管理Volumes:
```shell
# 创建volumes并命名 my-vol
docker volume create my-vol

# Volumes列表
docker volume ls

# 查看Volumes特性
docker volume inspect my-vol

# 移除Volumes
docker volume rm my-vol

# 移除所有Volumes
docker volume prune
```


2.可在启动容器时指定Volumes:

```shell
## 运行devtest容器
## 并将容器myvol2挂在/app目录中
 docker run -d \
  --name devtest \
  -v myvol2:/app \
  nginx:latest
```


3.当建立多容器服务的时候，开发者往往会选择`docker compose`这一多容器管理的工具，并编写好`docker-compose.yml`文件。一方面，此文件可以帮助我们将所有容器的配置参数融合在一个file里面统一管理，另外一方面它可以帮助多容器的服务快速启动或终止，这里我们不详细介绍`yml`文件的每个参数，而着重说一下如何在此文件中定义Volumes。

```shell
version: "3.9"
services:
  frontend:
    image: node:lts
    volumes:
      - myapp:/home/node/app
volumes:
  myapp:
    external: true
```
这里的两个volumes设定，第一个是设置services的volumes，名为`myapp`,路径是储存在`/home/node/app`下，第二个顶级volumes中的设置是为了实现多个容器的共享，比如这里就是设置`myapp`可以被所有容器共享。


4.使用已存在的容器数据为新的容器创建Volumes。这里新容器名为`nginxtest`，新Volumes命名为`nignx-vol`，其数据来源的路径是`/usr/share/nginx/html`。

```shell
 docker run -d \
  --name=nginxtest \
  -v nginx-vol:/usr/share/nginx/html \
  nginx:latest
```

在此基础上，你也可以通过添加`ro`来设置只读权限，这样可以防止其他人在共享容器数据时的误删或其他失误。

```shell
 docker run -d \
  --name=nginxtest \
  -v nginx-vol:/usr/share/nginx/html:ro \
  nginx:latest
```


5.Volumes还可以运用在数据备份，数据迁移的场景中。

首先，我们创建一个名`dbstore`的容器且带有Volumes`dbdata`：
```shell
docker run -v /dbdata --name dbstore ubuntu /bin/bash
```

接下来，为这个容器的Volumes进行备份，利用`--volumes-from`指定容器的来源，指定将`dbdata`备份到路径`/backup`下的`backup.tar`文件中：
```shell
docker run --rm --volumes-from dbstore -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /dbdata
```

接下来，迁移上一步已经备份好的容器数据, 需要创建一个新的容器`dbstore2`：

```shell
docker run -v /dbdata --name dbstore2 ubuntu /bin/bash
```

再从`backup.tar`文件中迁移到新的容器中：
```shell
 docker run --rm --volumes-from dbstore2 -v $(pwd):/backup ubuntu bash -c "cd /dbdata && tar xvf /backup/backup.tar --strip 1"
```

## 4 总结
当部署服务时，功能的开发是一方面，数据的可持续化管理也是必不可少的一个部分。希望这篇文章可以帮助你在Docker学习过程中对Volumes有更深的理解并选择合适的命令管理容器中的数据。

欢迎各位小伙伴留言讨论。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>

