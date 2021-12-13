---
template: overrides/blogs.html
---

# 初识图数据库

!!! info
    作者：Dragond41，发布于2021-12-13，阅读时间：约2分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言
小伙伴们有听说过"图数据库 - Graph Database" 吗？
<p><strong>是用来存储图片的数据库？还是用图片存储数据？？（误）</strong>
<p>如果有被这两句话忽悠到的话，那赶紧进入今天的文章吧~</p>

## 2 节点和关系

与传统关系型数据库不同，图数据库由节点和关系（节点之间的关系）组成。如下图：


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V1.png"  />
  <figcaption></figcaption>
</figure>



### 2.1 节点
节点代表一个实体。一个节点与关系型数据库中的一条记录类似。
<p>上图中的圆形图案都是节点。其中橙色的节点代表是电影实体，蓝色的节点代表的是具体的人。

### 2.2 关系
两个节点之间的联系就是关系。如上述图中就出现了三种【人-电影】的关系：
- <font size="1">ACTED_IN - 基努·里维斯、劳伦斯·菲什伯恩、凯莉·安摩丝和雨果·维文等参演
- <font size="1">DIRECTED - 沃卓斯基姐妹指导
- <font size="1">PRODUCED - 乔·西佛监制

### 2.3 关系的方向
在Neo4J中，关系是必须有方向的。
对一个节点来说，关系可以有两种方向。<p>指向它的关系，和由它指向其他节点的关系。上图中，所有的关系都是由人指向电影。

### 2.4 标签
标签是节点或者关系的种类（Type)。如上述图中，定义蓝色节点时，他们的Label是Person；定义橙色节点时，他们的Label是Movie。
<p>标签的作用是，当你进行查询时只返回特定某些类型的节点。比如只查询Person节点。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V2.png"  />
  <figcaption></figcaption>
</figure>

### 2.5 属性
节点与关系都能添加属性。属性是以name-value对的形式添加的。比如，返回上述图中所有Person的name和born属性。
<p>属性使图数据库中的信息变的更加丰富，查询时也可以利用到这些属性，如查询在1970年后出生的人。

  <figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V3.png"  />
  <figcaption></figcaption>
</figure>

## 3 Why图数据库
大家看了对图数据库的大体介绍，可能觉得这个技术很酷炫，那在具体的业务中，图数据库能带来哪些关系型数据库不能带来的价值呢？以下两方面可以作为参考。

- <font size="1">高效的查询数据间的关系，尤其是当关系很复杂时
- <font size="1">同时也能较便捷的可视化数据间的关系

当你看到以下这样的查询结果时，是不是很赏心悦目呢？电影与人之间的关系可以一目了然。
当然，这只是一小部分数据查询的结果。

  <figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V4.png"  />
  <figcaption></figcaption>
</figure>
  
当数据变多时，可视化的结果是这样的。。。


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V5.png"  />
  <figcaption></figcaption>
</figure>
  
当然没有人会从这样的可视化结果中获取有价值的信息，那图数据库具体应该如何应用在业务中呢？
<p>请期待之后的图数据库实战系列，绝对能让你对这个又新又潮的技术有更具体的认识！
  
    
## 4 总结
  
学习了本篇文章之后是不是不会被忽悠什么是图数据库了（狗头），而且能在朋友面前吹吹牛呢？
<p>如果想继续收看和图数据相关的文章的话，就点个赞或者在看吧！


<p>希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
