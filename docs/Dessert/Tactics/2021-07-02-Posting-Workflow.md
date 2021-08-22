---
template: overrides/blogs.html
---

# 如何以最快的速度写出一篇优美的文章

!!! info
    作者：袁子弹起飞，发布于2021-07-02，阅读时间：约4分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484231&idx=1&sn=27085e9af4a05db567d7004aa97cd78b&chksm=eb90f033dce77925a389375a1e39b7c83a85d55e9c4df1a857650ce5c8096293881047f2ef07&token=97683576&lang=zh_CN#rd)

## 1 前言

对于一个需要在多平台快速发布文字内容的团队来说，提高写字、排版的效率至关重要。我们为了找到效率最高的办法，查阅了很多资料，测试了很多工具，最终组建了一套行之有效、省时省力的办法，这篇文章将会详细介绍BulletTech发布文章的工作流，帮助大家理解如何以最快的速度写出一篇优美的文章，并同步到各个平台。

## 2 工作流

简而言之，有如下几步：

- 构思主题，完成写作任务排期
- 创建不包含任何格式的Markdown文本
- 渲染Markdown文本，发布文章
- 跟踪阅读数据，逐步调优

### 2.1 构思主题，完成写作任务排期

目前BulletTech所有的文章全部是原创，所以每周团队成员需要开会讨论写作主题，团队成员根据频道定位、各自的知识储备和用户阅读反馈来确定写作主题，然后使用Notion进行写作任务排期。关于Notion的使用技巧，请参考Void老师佳作：[功能强大，颜值在线的个人笔记应用 - Notion](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247483944&idx=1&sn=fe72700771845764d33fa8e92bff4bef&chksm=eb90f15cdce7784a67240f7202025582734689e09f96049836b5daedd35f76db079ad70ee7bb&token=150554771&lang=zh_CN#rd)。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-2/1625209039771-Notion%E6%8E%92%E6%9C%9F.png" width="600" />
  <figcaption>使用Notion进行写作任务的排期</figcaption>
</figure>

### 2.1 创建不包含任何格式的Markdown文本

各个平台格式不尽相同，所以最简单的办法是一开始创建纯文本，然后使用“格式刷”把文本刷成优美的样式。因此Markdown成为了不二之选，Markdown可以使用特定的标识符标记样式，这些样式能非常容易地转化为优美的HTML，在移动设备和电脑上供用户观看。例如，输入小标题的写法是：

```
- 标题-1
- 标题-2
```

经过渲染后它会转化为非常易于观看的样式：

- 标题-1
- 标题-2

因此，在进行文章写作的时候，完全不用担心格式混乱。当文字写完后，也非常容易将预先设定好的样式套用在Markdown文件上。

### 2.3 渲染Markdown文本，发布文章

推荐使用免费的mdnice网页客户端进行文章样式的渲染，只需要将写好的Markdown文本粘贴到mdnice编辑器，选择合适的主题就可以完成样式的渲染了，你可以通过调整CSS样式来构建自己专属的样式。mdnice支持[配置GitHub图床](https://product.mdnice.com/article/developer/github-image-hosting/)，上传的图片会生成一个通用的链接，各个平台都能通过该链接正确访问图片，无需反复上传。

同时，mdnice支持微信和知乎文章样式的导出，实测发现导出效果很棒，只需要轻微调整就可达到发布的状态。使用微信导出样式在头条和CSDN上也能很好的适配。多平台发布效率极高。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-2/1625210341851-mdnice.png" width="600" />
  <figcaption>mdnice网页编辑器</figcaption>
</figure>

### 2.4 跟踪阅读数据，逐步调优

由于微信公众号是主战场，所以我们主要根据公众号文章阅读数据来进行优化，阅读量、分享量、阅读后关注人数、阅读渠道等指标评价文章效果。每个频道都有所不同，不再赘述。推荐使用微信推出的订阅号助手，该App能够很方便地管理公众号：添加内容、回复评论、查阅数据等，通过使用这个工具能随时随地和用户保持紧密的联系。

## 3 总结

以上就是BulleTech工作流的简介，这样一套效率极高的方法能够帮助我们很快地将想法转化为文章分享给大家，希望这篇文章能帮助到你，欢迎在评论区分享你的反馈！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
