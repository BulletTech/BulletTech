---
template: overrides/blogs.html
---

# 理解Python闭包

!!! info
    作者：袁子弹起飞，发布于2021-09-21，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484557&idx=1&sn=bd624bdb21757e391d01c5ced51cb5f8&chksm=eb90f7f9dce77eef2a8c67bc0d3637e9d90708ffd061ce4773916fa3c58d137e4b859adf1c40&token=1570026209&lang=zh_CN#rd)

## 1 前言

在使用Python的日常工作中，你或许碰到过类似于这样的代码：

```Python
def make_counter():
    # 外层闭包函数
    count = 0
    def counter():
      # 嵌套函数

        nonlocal count
        count += 1
        return count

    return counter
```

一个函数里还有一个函数，并且外层函数的返回值是内层的函数，为什么要这样定义函数呢？这样有什么好处，这篇文章我们来揭开它神秘的面纱 - 闭包（Closure）。

## 2 闭包的要点

闭包指延伸了作用域的函数，它会引用一个不在函数定义中的非全局变量(如上述例子中的count)，nonlocal的加入能把变量标记为自由变量(Python 3才加入nonlocal关键字)，让内层嵌套函数可以修改作用域外的不可变变量。

调用make_counter时，返回一个counter函数对象，每次调用counter时，它会更新count，示例如下：

```Python
# 运行闭包函数
counter = make_counter()
print(counter())
print(counter())
```

输出为：

```python
1
2
```

在这个例子中，有一点需要展开说的是count的历史值的存储位置，count是make_counter函数的局部变量，初始化的时候count的值为0，但调用counter的时候，make_counter函数已经返回了，本地作用域理应不复存在。

在counter函数中，count是自由变量，counter函数实现了对变量count的绑定。可以通过Python中的__code__属性（表示编译后的函数定义体）查看保存的局部变量和自由变量的名称，如下所示：

```Python
# 查看自由变量
counter.__code__.co_freevars
```

输出为：
```
('count',)
```

count的绑定在返回的counter函数的__closure__属性里，其中__closure__的各个元素对应于`counter.__code__.co_freevars`中的一个名称。这些元素是cell对象，可以通过cell_contents属性访问其存储的值，示例如下：

```python
counter.__closure__[0].cell_contents
```

输出为：

```
2
```

闭包能够非常简洁、直观地解决轻量级的问题，如果上述功能用`类`来实现的话，会长成这样：

```Python
# 用类定义一个计数器，从0开始计数
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())
print(counter())
```

输出为：

```Python
1
2
```

## 3 总结

闭包是一种函数，它保留了定义函数时存在的自由变量的绑定，因此，即便是函数返回后作用域不存在了，那些绑定仍然能够被使用。闭包可以很容易地实现一些简单的类的功能，同时基于此还有很多Python的魔法能够实现，比如装饰器，待下回分解！

希望这次的分享对你有帮助，欢迎在评论区讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
