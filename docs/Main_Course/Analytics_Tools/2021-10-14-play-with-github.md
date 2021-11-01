---
template: overrides/blogs.html
---

# 玩转GitHub

!!! info
    作者：Void，发布于2021-10-14，阅读时间：约5分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)

## 1 引言

GitHub的主要功能是进行代码的版本管理与协作。我们在《一行代码都不写，教你使用GitHub》这篇文章中，详细地介绍了GitHub能做什么以及如何使用GitHub。  
其实GitHub也可以很有趣，本文将从不一样的视角，聊聊GitHub有哪些好玩的功能。

## 2 Action

GitHub Action提供了一套自动化执行脚本命令的服务。我们团队使用GitHub Pages来建立我们的博客。当我们在GitHub上更新我们的文章时，很自然的，我们想让这一改动自动地更新到博客当中。  
如果没有GitHub Action这一自动化部署服务，我们可能需要每次手动地跑一些脚本将文章部署到博客上面。  
现在，我们只需要在这一路径下(BulletTech/.github/workflows)，创建ci.yml文件，将我们需要的命令写入其中。当有改动push到main分支时，GitHub Action就可以自动地帮我们跑设定好的脚本。  

```yml
name: ci
on:
  push:
    branches:
      - master
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
      - run: pip install --upgrade mkdocs-material
      - run: pip install mkdocs-redirects
      - run: pip install mkdocs-minify-plugin
      - run: pip install mkdocs-macros-plugin
      - run: pip install mkdocs-git-revision-date-localized-plugin
      - run: git pull
      - run: mkdocs gh-deploy --force
```

除了自己创建的工作流(workflow)，GitHub还有很丰富的workflow社区，你可以选择不同的workflow，实现你的各种需求。

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github4.png" width="500" />
</figure>

## 3 Projects

GitHub自带了项目管理的功能。  
首先，我们点击项目看板(Projects)，可以看到我们创建的项目。

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github1.png" width="500" />
</figure>

点击项目，可以看到看板状的结构，有To do，In progress，Done等多个Column，当然也可以自己新建Column。

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github2.png" width="500" />
</figure>

我们可以通过点击Column中的加号创建note。在图示中，我们可以看到在To do这一Column中的note是一个issue。那么，这是怎么实现的呢？    
我们在创建issue过程中，可以注意到右边栏有Projects这一项。如果我们选择对应的Column，就可以把这个issue作为card插入这一Column。  

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github3.png" width="500" />
</figure>

我们也可以在看板中，通过add card将issue直接加入。  
有了项目看板功能，我们可以更方便地进行项目管理与团队协作。

## 4 Wiki

GitHub的Wiki允许我们以markdown文本的方式构建属于这个repo的Wiki，让用户不止于README文档，更好地了解repo内容。优秀的示例如Pytorch的[Wiki](https://github.com/pytorch/pytorch/wiki)

## 5 Security

GitHub Security提供了关于代码安全方面的工具。  

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github5.png" width="500" />
</figure>

如我们可以通过创建Security.md向用户提示代码中的某些潜在问题，优秀的案例可以参考Tensorflow Repo中的[Security文件](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md)。  
我们还可以通过GitHub Action设定代码安全扫描的工作流。它可以自动地扫描分支和pull request中代码的语法错误、不安全的输入(显示的用户输入)等等。  

## 6 Insights

GitHub的Insights以直观的图表的形式给出了repo整体的以及代码贡献者个人的commit，pull request等行为的信息。

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github6.png" width="500" />
</figure>

## 7 小结

GitHub也可以很有趣，除了提供的常规功能之外，GitHub提供了很多有趣、实用的功能。它们不仅极大地提高了生产力，也丰富了GitHub的内容。


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
