---
template: overrides/blogs.html
---

# 玩转GitHub

!!! info 
    作者：Void，发布于2021-10-14，阅读时间：约5分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)

## 1 引言

Github的主要功能是进行代码的版本管理与协作。我们在《一行代码都不写，教你使用GitHub》这篇文章中，详细地介绍了Github能做什么以及如何使用Github。  
其实github也可以很有趣，本文将从不一样的视角，聊聊github有哪些好玩的功能。

## 2 Projects

GitHub自带了项目管理的功能。首先，我们点击项目看板(Projects)，可以看到我们创建的项目。点击项目，可以看到看板状的结构，有To do，In progress，Done等多个Column，当然也可以自己新建Column。  
我们可以通过点击Column中的加号创建note。在图示中，我们可以看到在To do这一Column中的note是一个issue。那么，这是怎么实现的呢？  
我们在创建issue过程中，可以注意到右边栏有Projects这一项。如果我们选择对应的Column，就可以把这个issue作为card插入这一Column。我们也可以在看板中，通过add card将issue直接加入。  
有了项目看板功能，我们可以更方便的进行项目管理与团队分工协作。

## 3 Action

Action提供了一套自动化执行脚本命令的服务。我们团队使用Github pages来建立我们的博客。当我们在github上更新我们的文章时，很自然的，我们想让这一改动自动化地更新到博客当中。  
如果没有github Action这一自动化部署服务，我们可能需要每次手动的跑一些脚本将文章部署到博客上面。  
现在，我们只需要在这一路径下(BulletTech/.github/workflows)，创建ci.yml文件，将我们需要的命令写入其中。当有改动push到main分支时，github Action就可以自动地帮我们跑写入的脚本。  

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

除了自己创建的workflow，github还有很丰富的workflow社区，你可以选择不同的workflow，实现你的各种需求。

## 4 Insights

## 5 小结


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
