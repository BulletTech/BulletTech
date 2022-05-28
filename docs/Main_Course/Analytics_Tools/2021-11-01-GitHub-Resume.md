---
template: overrides/blogs.html
tags:
  - git
---

# 用GitHub做一份精美的在线简历

!!! info
    作者：袁子弹起飞，发布于2021-11-01，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/Ns0YXYQBEZbUJEJyX21L0w)

## 1 前言

我们之前介绍了很多GitHub的酷炫功能，为了方便理解这篇文章的内容，建议阅读之前的文章回顾基本的GitHub操作知识：

- [一行代码都不写，教你使用GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)
- [Git常用命令一览](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)
- [玩转GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)

在这篇文章里，我们将介绍如何使用GitHub制作在线简历、打造一个所有人都能访问的网站展示自己。

## 2 制作在线简历

### 2.1 下载示例代码

本示例采用Bootstrap的模板，请前往BulletTech的官方GitHub账号里找到[Resume仓库](https://github.com/BulletTech2021/Resume 'BulletTech的Resume示例代码')下载示例代码。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Resume仓库.png"  />
  <figcaption>BulletTech的Resume仓库</figcaption>
</figure>

需要修改的代码存在`/home/index.html`里:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/home源代码.png"  />
  <figcaption>主页源代码</figcaption>
</figure>


### 2.2 修改示例代码

下载了源码之后，可以在本地双击`index.html`进行实时预览，对照着网页内容使用`ctrl/command + F`查找然后修改对应的元素，网页刷新后则会显示最新的内容，也可以修改CSS（`home/css/styles.css`）和其他部件进行深度定制。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Resume.png"  />
  <figcaption>本地预览简历</figcaption>
</figure>

### 2.3 上线简历

创建一个自己的GitHub仓库，并将改完后的代码提交到自己的仓库中。在网页上查看确保完整的代码被上传。然后激活GitHub Pages功能，默认状态下，选择master/main分支下的root即可，点击对应的URL就可以访问你自己的简历了。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/GitHub_Pages.png"  />
  <figcaption>设置GitHub Pages</figcaption>
</figure>

## 3 总结

GitHub的使用小技巧又增加了一个，欢迎参照上述步骤制作自己的在线简历。BulletTech的[示例简历](https://bullettech2021.github.io/Resume/home/ 'BulletTech示例简历')可以访问`https://bullettech2021.github.io/Resume/home/`进行查看。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
