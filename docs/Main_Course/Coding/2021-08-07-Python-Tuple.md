---
template: overrides/blogs.html
---

# Python元组常用操作小技巧

!!! info
    作者：袁子弹起飞，发布于2021-08-07，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/p_Cva92Md_N7k6ohXzc-fA)

## 1 前言

Python作为当下数据科学、人工智能领域炙手可热的编程语言受到了非常多的关注，有很多人都在学习。但是在追求卓越的路上，一点不要忽视了基础，比如常用数据结构、语法规范、编程思维的最佳实践，对这些最基础的事情了如指掌，在这基础之上的工作也会游刃有余。

所以这篇文章，我们先来回顾和总结Python数据结构里常用操作。Python中常见的数据结构可以统称为容器（container）。序列（如列表和元组）、映射（如字典）以及集合（set）是三类主要的容器。而扁平序列如str、bytes、bytearray、memoryview 和 array.array等不在这篇文章的讨论范围内。

在此，我们先从元组开始说起。

## 2 元组不仅是不可变的列表

### 2.2 元组的记录作用

元组区别与列表的显著特征之一就是它不能被修改，但其另外一个作用就是[用于没有字段名的记录](https://book.douban.com/subject/27028517/)。因为后者经常被忽略，我们先来看看元组作为记录的作用。

使用括号就可以定义一个元组。元组中的每个元素都存放了记录中一个字段 的数据，外加这个字段的位置。正是这个位置信息给数据赋予了意义。下面的例子中，元组就被当作记录加以利用

```Python
# 洛杉矶国际机场的经纬度，用元组记录
lax_coordinates = (33.9425, -118.408056)

# 东京市的一些信息：市名、年份、人口（单位：百万）、人口变化 （单位：百分比）和面积（单位：平方千米），用元组记录
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

#一个元组列表，元组的形式为 (country_code, passport_number)。
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

#在迭代的过程中，passport 变量被绑定到每个元组上。% 格式运算符能被匹配到对应的元组元素上。
for passport in sorted(traveler_ids):
  print('%s/%s' % passport)
```

输出为：

```
BRA/CE342567
ESP/XDA205856
USA/31195855
```

### 2.3 元组的拆包

上述for循环中的操作提取了元组中的元素，也叫作拆包（unpacking）。平行赋值是对元组拆包很好的应用，示例如下：

```Python
# 洛杉矶国际机场的经纬度，用元组记录
lax_coordinates = (33.9425, -118.408056)
# 拆包元组，将元组中的元素分别赋值给对应的变量
latitude, longitude = lax_coordinates
```

还有一个经典而优雅的应用是交换变量的值：

```Python
a, b = b, a
```

### 2.4 元组作为函数参数

用 * 运算符把一个可迭代对象拆开作为函数的参数，例如Python的内置函数divmod接收两个数字类型的参数，返回商和余数。以下范例将使用 * 将元组传入函数。

```Python
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)
```
输出为：

```
2 4
```

### 2.5 元组作为函数返回值

有些函数有多个返回值，将其付给一个变量时，变量类型即是元组.

```Python
import numpy as np
arr = np.random.randint(10, size=8)

def count_sum(arr):
   count = len(arr)
   sum = arr.sum()
   return count, sum

result = count_sum(arr)
print(result)
```

输出为：

```
(8, 40)
```

### 2.6 zip函数

zip是Python的内置函数，能够接收两个或多个序列，并组成一个元组列表，在Python3中会返回一个迭代器，如下所示：

```Python
list_a = [1,2,3]
list_b = ['a','b','c']

for i in zip(list_a, list_b):
    print(i)
```

输出为：

```
(1, 'a')
(2, 'b')
(3, 'c')
```

### 2.7 其他常规操作

元组当然也支持一些常规操作，如对于元组`a = (1, 'y', 5, 5, 'x')`：

- 索引，如`a.index('x')`
- 切片，如`a[1:4]`
- 计数，如`a.count(5)`
- 排序，如`a.sort()`
- 合并元组，如`c = a + a`

## 3 总结

上述内容不仅涵盖了元组的基本操作，同时也结合了其他的函数、运算符等。在回顾这些知识时主要参考了两本经典的Python编程书籍：《流畅的Python》和《像计算机科学家一样思考Python》，有兴趣的朋友可以深入阅读！

希望这篇文章对你有帮助，下回将总结Python列表的技巧。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
