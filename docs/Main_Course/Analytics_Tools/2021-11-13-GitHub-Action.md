---
template: overrides/blogs.html
---

# GitHub Action概览

!!! info
    作者：袁子弹起飞，发布于2021-11-13，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/aGPIfrXA3rHsg0ioFcGsBQ)

## 1 前言

我们之前介绍了很多GitHub的酷炫功能，为了方便理解这篇文章的内容，建议阅读之前的文章回顾基本的GitHub操作知识：

- [一行代码都不写，教你使用GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)
- [Git常用命令一览](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)
- [玩转GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)
- [用GitHub做一份精美的在线简历](https://mp.weixin.qq.com/s/Ns0YXYQBEZbUJEJyX21L0w)

在这篇文章里，我们将介绍如何使用GitHub Action，简化重复机械的工作，以大大提高效率、节省时间。

## 2 GitHub Action概览

GitHub Action可以自动执行自定义的脚本完成预先设定的工作。用户需要设置触发条件（事件）及条件满足时的命令，GitHub就可以自动完成预设的操作，例如当有更新合并到master/main分支时，自动执行测试脚本检查错误。下图展示了GitHub Action执行时的组件：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/overview-actions-design.png"  />
  <figcaption>GitHub Action组件，来源：GitHub官网</figcaption>
</figure>

事件发生时，GitHub自动触发工作流。然后程序按步骤执行。

## 3 创建Action

GitHub Action使用[YAML](https://yaml.org/ 'YAML')定义触发的事件、工作和步骤，工作流文件需要存放在代码仓库中的特定位置：`.github/workflows`。

以[BulletTech博客的持续集成工作流](https://github.com/BulletTech/BulletTech/blob/main/.github/workflows/ci.yml 'BulletTech博客的工作流')为例：

```yml
name: ci
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - run: python ./docs/Scripts/Update_reading_time.py
      - run: pip install mkdocs-material
      - run: pip install mkdocs-redirects
      - run: pip install mkdocs-minify-plugin
      - run: pip install mkdocs-macros-plugin
      - run: pip install mkdocs-git-revision-date-localized-plugin
      - run: pip install --upgrade mkdocs-material
      - run: pip install --upgrade mkdocs-redirects
      - run: pip install --upgrade mkdocs-minify-plugin
      - run: pip install --upgrade mkdocs-macros-plugin
      - run: pip install --upgrade mkdocs-git-revision-date-localized-plugin   
      - run: git pull
      - run: mkdocs gh-deploy --force
```

要点如下：

- `name`定义了工作流的名称，此处为持续集成（Continous Integration, CI)。
- `on`为触发工作流的事件，此处定义为更新推送到main分支时需要执行命令。
- `jobs`里定义了工作任务，deploy为工作的名称，在GitHub的Ubuntu Linux虚拟机上运行一系列步骤。
  - `uses`后接[GitHub Action集市](https://github.com/marketplace?type=actions 'GitHub Action集市')里的action。此处使用了action来check out仓库并将代码下载到运行代码的服务器上，同时配置Python运行环境。
  - `run`后接要执行的命令，此处安装了一些博客依赖的Python包并且运行部署命令。

## 4 查看Action运行状态

在GitHub仓库的Actions标签中，可看到action运行状态：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Action_Status.png"  />
  <figcaption>GitHub Action状态</figcaption>
</figure>

可以见到BulletTech使用的ci工作流，点击runs可以查看action每一步的运行状态。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Action_steps.png"  />
  <figcaption>Action运行情况</figcaption>
</figure>


## 5 总结

使用GitHub Action自动化了许多重复机械的劳动，节约出来的时间可用于更有意义的事情，更多的内容可自行查看下列参考资料定制适合自己的工作流。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
