---
template: overrides/blogs.html
---

# SnowFlake 运行机制浅谈

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

SnowFLake作为近年来十分火爆的数据仓库应用获得了许多用户和投资人的青睐，本人日常工作中也经常使用SnowFLake做分析，所以对其背后的运行机制做了一些研究，今天和大家聊聊SnowFLake的主要架构和工作原理。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-31/1627739241720-Home.png"  />
  <figcaption>SnowFlake股价</figcaption>
</figure>

## 2 SnowFlake主要特性

- 安全性和数据保护：SnowFlake支持多种验证方式，如Multi-Factor Authentication (MFA), federal authentication，Single Sign-on (SSO)和OAuth。客户端和服务器之间的通信都由[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security "Transport Layer Security")保护.
- 支持标准的SQL和许多扩展SQL的特性，其对绝大多数SQL的数据定义语言（Data Definition Language）和数据操作语言（Data Manipulation Language）都支持，因此做数据分析时基本不用担心找不到对应的操作。
- SnowFlake支持软件客户端进行连接，同时也为多种编程语言提供了接口如Python connector, Spark connector, Node.js driver, .NET driver等。
- 便捷的分享功能，用户可以很容易地分享数据和查询语句给其他的用户。

## 3 SnowFlake架构

SnowFlake的架构融合了[Shared-Disk](https://en.wikipedia.org/wiki/Shared_disk_architecture "Shared-Disk Architecture")和[Shared-Nothing](https://en.wikipedia.org/wiki/Shared-nothing_architecture "Shared-nothing Architecture")架构以综合两者的优势，下面是这两种架构的示意：

### 3.1 Shared-Disk架构示意

常用于传统的数据库中，它拥有一个集群里所有节点都能访问的存储层，集群中的计算节点没有自己的存储，它们都通过访问中央存储层来获取数据并进行处理。通过集群控制软件来监控和管理数据的处理，数据的增删改查都在同一份数据上完成，因此所有节点获取的数据都相同。两个及以上的节点同时更新一份数据是绝对禁止的。

这种架构不利于性能的发挥，并且缺乏扩展性。经常需要做数据更新的应用不太适用于这类架构，因为Shared-Disk的锁机制会对其掣肘。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-31/1627739241720-Home.png"  />
  <figcaption>Shared-Disk架构</figcaption>
</figure>


### 3.2 Shared-Nothing架构示意

顾名思义，Shared-Nothing架构里，集群的节点都有自己单独的计算资源和存储空间，其优势是数据可以分区存储在各个节点中。当需要处理用户请求时，路由会将请求分配到合适的节点上进行计算，当有结算发生错误时，处理的进程能被其他的节点接管，保证用户请求能被稳定、正确地处理。这种架构很适合于数据读取量很大的应用，比如数据仓库。

### 3.3 SnowFlake的选择

SnowFlake则采用了3个不同的层来构建应用：`存储层`、`计算层`和`云服务层`，其示意图如下：

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-31/1627739241720-Home.png"  />
  <figcaption>Shared-Nothing架构</figcaption>
</figure>

`存储层`负责将数据优化、压损并存在多个微小的片区中。数据以行列的格式存储，并且以类似于Shared-Disk的方式进行管理。计算节点通过连接存储层来获取数据进行查询计算，存储层独立于其他资源，并且SnowFlake部署在云上，因此其超大型的分布式存储系统能保证高性能、稳定性、可用性、容量和可扩展性。

`计算层`使用虚拟仓库（Virtual Warehouse，依托于虚拟机）运行查询语句，而计算层和存储层在设计上是分离的，在这之间，SnowFlake实施了智能的缓存机制保证资源的最优化和减少计算层和存储层不必要的交互。虚拟仓库有大小之分，可以创建多个用于处理不同性能需求的请求，并且虚拟仓库是各自独立的，因此计算资源并不共享。这样设计的优点有：

- 可以随时创建或者删除虚拟仓库，也可以很方便地在不影响查询语句计算的前提下扩展虚拟仓库的计算资源。
- 虚拟仓库可被方便地停用或者启用，适用于长时间没有查询或者停用一段时间后需重新参与查询
- 可以非常方便地自动更改虚拟仓库的集群大小，例如设置虚拟仓库适用集群在1-3个之间，SnowFlake则可以根据工作量来自动创建合适的虚拟仓库

`云服务层`负责用户信息验证、集群管理、安全与加密、数据的元数据管理、查询语句优化等工作，这些工作都由计算节点完成。常见的处理内容示例包括：

- 用户登录
- 查询语句提交后，首先会经过云服务层的优化器，然后再传入计算层进行处理
- 优化查询、过滤数据所需的元数据也存储在这一层

SnowFlake的三层架构都能够独立地进行扩展，但SnowFlake只对存储层和计算层进行收费，因为服务层在计算节点中进行处理。单独扩展的优势显而易见，需要更多数据即单独扩展存储层，需要更强的计算性能，则单独扩展计算层。详见SnowFlake的[架构导览](https://docs.snowflake.com/en/user-guide/intro-key-concepts.html "SnowFlake的架构")。

## 3 总结

了解了SnowFlake架构之后，相信你能更好地理解为什么如此多的用户选择SnowFlake，其依托于云的易扩展、按需收费的特性为很多企业提供了高效、安全、稳定、划算的解决方案。作为数据分析师，亲身体验下来发现SnowFlake也的确比许多传统的数据仓库更好用。关于实操经验，请查看往期的SQL小贴士：[数据仓库N兄弟](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484458&idx=1&sn=b103c9b9d205e0d6a4589b68687e9c95&chksm=eb90f75edce77e480d76a140289f4217c8f8de8cb6b5da80c89b4cf09b1b07d87ef5f256831e&token=969028810&lang=zh_CN#rd) 和[SQL不完全实践指南](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484506&idx=1&sn=c46e7bf80719bd004a63d7fa668f4c7e&chksm=eb90f72edce77e38c38fdfe685b1ff86590ed22aea65b8c19f07fb7ce44b5b981929796873cc&token=969028810&lang=zh_CN#rd)。

希望这次的分享对你有帮助！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
