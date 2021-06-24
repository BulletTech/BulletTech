---
template: overrides/blogs.html
---

# 一行代码都不写，教你使用Github

## 1 Github是什么

在很多人的印象中，GitHub主要是程序员写代码会使用到的工具。事实上，GitHub最主要的特性是版本管理和协同工作，这意味着不仅是程序员，非技术人士也可以使用它更高效地完成很多工作。因此，这篇文章将教大家零基础使用GitHub，帮助大家认识这个强大的效率工具。首先请熟悉GitHub使用过程中的常见术语：

- 仓库（Repository）：可以看作是存代码和文件一个文件夹，当你作为仓库管理者时，可以设置访问权限
- 远程仓库（Remote Repository）：可以看作仓库的副本，通常在此完成修改，日后用于补充到仓库主干上
- 主干（master或main）：当前项目所在的状态
- 分支（Branch）：可以看作主干的副本，可暂时存储修改的状态，常用于
- 提交更新（Push）：将修改提交到仓库中
- 获取更新（Pull）：将仓库上的更新同步到现在的工作状态
- 合并请求（Pull request）：用于将分支上的修改合并到主干上
- 合并（Merged）：分支上的更改被合并到主干上，仓库状态更新


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-23/1624441420407-Github%20%E5%9B%BE%E4%BE%8B.png" width="600" />
  <figcaption>GitHub常见术语图示</figcaption>
</figure>


接下来的介绍中，都会使用GitHub的桌面客户端（在GitHub的官方网站可免费下载），借助这个app，可以使用GitHub绝大多数的核心功能。

## 2 Github能做什么

GitHub在版本管理和协同工作方面是绝佳的工具之一。

### 2.1 版本管理

具体来说，版本管理的功能可以帮助保存文件的修改历史，以便在需要回溯时能很方便地检查和回滚。



<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-23/1624441521157-Github%20%E6%9F%A5%E7%9C%8B%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC.png" width="600" />
  <figcaption>Github Desktop 查看历史版本</figcaption>
</figure>


示例中是BulletTech的仓库，过往的更改历史都被保存了下来，点击更改即可看到更改的文件和对应的更新。

### 2.2 协作

同时，这些更改是由BulletTech的团队成员共同完成的，当多人协作时，建议在不同的分支上工作，当完成更新后，可以通过合并请求（⌘ + R）将你的分支上的更新合并到主干上。此时，软件会自动引导你跳转到网页端创建请求，团队的成员就可以审核更改，如果符合要求，更新就可以被合并到主干上。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-23/1624441553655-Github%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82.png" width="600" />
  <figcaption>合并请求</figcaption>
</figure>

建议设置合并请求的模板，将更新的信息填写清楚会节省很多沟通的时间，日后回看时也有迹可循。可以在我们的[仓库](https://github.com/BulletTech/BulletTech/tree/main/.github)中找到对应的模板，并根据自己的需求更新模板。

### 2.3 

## Github怎么用
