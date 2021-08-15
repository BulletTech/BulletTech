---
template: overrides/blogs.html
---

# Python列表常用操作小技巧

!!! info
    作者：袁子弹起飞，发布于2021-08-14，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/GmZ1Du4qJRai7D7oXKh75w)
    
 ## 前言
 
 在上一篇文章中，我們回顾了Python元组的常用操作，这篇文章我们继续聊聊Python里另一种常用的数据类型 - 列表（List）。

和元组一样，列表也是一种序列，通过方括号`[`和`]`即可创建。列表中的值常被称为元素，元素的数据类型可以不同，如`test_list = [0,1,'a','b']`就能成功创建一个列表。

不同于元组，列表是可变序列，因此序列可用的操作会更加灵活，接下来我们来回顾对序列最常用的操作。

