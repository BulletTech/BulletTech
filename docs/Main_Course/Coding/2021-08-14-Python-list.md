---
template: overrides/blogs.html
---

# Python列表常用操作小技巧

!!! info
    作者：袁子弹起飞，发布于2021-08-14，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484437&idx=1&sn=6d58dbd242157e216cb0e573678686d9&chksm=eb90f761dce77e7711ad25f26be3ff212d80db386a74d5902af1247e027e1108c84ec8d0fb7c&token=891223383&lang=zh_CN#rd)

 ## 1 前言

 在上一篇文章中，我们回顾了[Python元组的常用操作](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&tempkey=MTEyNl96d1NDWlZlNm1CSWJxKzEyeTlkcTIybWVyQmlFcFJWZncyZGFqZndNUFl1dHA2R1Jzb09STmVLYzZNeGNFUk5nUDJsanZSOUMzMFpLbUlmTUhzOWVUeDZVUjM5MnJtVlc3MkpTRWc0a1haaDBGdmFJUDVLLVFUR29QYlhteDhaN3RTRmpNZFRJTVBJTGs5cmpCcHdtMnAzQjhTbjl2aXBxRzl1S1p3fn4%3D&chksm=6b90f0865ce77990c57a2be4493364667bb91c1a0f0d2f70498bc6f318395c9abbcc5f9cd376#rd)，这篇文章我们继续聊聊Python里另一种常用的数据类型 - 列表（List）。

和元组一样，列表也是一种序列，通过方括号`[`和`]`即可创建。列表中的值常被称为元素，元素的数据类型可以不同，如`test_list = [0,1,1,'a','b']`就能成功创建一个列表。

不同于元组，列表是可变序列，因此序列可用的操作会更加灵活，接下来我们来回顾列表最常用的操作。

## 2 列表常用操作

### 2.1 遍历

以列表`people = ['Adam','Nick','Tony']`为例，可以使用for循环进行遍历：

```python
for i in people:
  print(i)
```

当需要更新列表时，使用下标遍历会更加方便：

```python
for i in range(len(people)):
  people[i] += '_suffix'
```

### 2.2 切片

和元组一样，可以通过切片来获取列表的元素（Python里下标从0开始计数）：

```python
print(people[:2])
```

输出为：
```
['Adam','Nick']
```

### 2.3 删除元素

a. pop方法可以返回要删除的值，可以使用下标进行删除，或者删除最后一个元素：`a = people.pop(2)`或者`a = people.pop()`，`a`的值都将是`'Tony'`，而原列表将会删除对应的元素。

b. 如果你不需要使用删除的值，del是一个好办法：`del people[0]`，则`people`列表将变为`['Nick','Tony']`。

c. remove方法将删除列表中第一个所需删除的元素，如进行`test_list.remove(1)`操作后，列表将变为`test_list = [0,1,'a','b']`，注意，remove方法不返回任何值。


### 2.4 列表和字符串

列表和字符串能够灵活地进行转换，比如将字符串转化为列表：

```python
# 将字符串转化为列表
name = 'Adam is very cool'
name_list_1 = list(name)
print(name_list_1)

# Split 方法能使用分隔符分割字符串
name_list_2 = name.split()
print(name_list_2)
```

输出为：

```
['A', 'd', 'a', 'm', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 'c', 'o', 'o', 'l']

['Adam', 'is', 'very', 'cool']
```

而有时需要将列表合并成一个字符串，`join`方法非常好用：

```Python
# 用空格连接列表的元素，组成一个新的字符串
print(' '.join(['Adam', 'is', 'very', 'cool']))
```

输出为：

```
'Adam is very cool'
```

### 2.5 列表的别名

这是一个容易出错的点，下列代码中，两个变量是完全一样的，改变一个，另一个的值也会跟着改变：

```Python
# alias是列表name的别名
name = ['Adam', 'is', 'very', 'cool']
alias = name
alias.pop()
print(name)
```

输出为：

```Python
['Adam', 'is', 'very']
```

因此，希望使用两个独立的列表时，尽量使用单独的赋值语句或者浅复制：

```Python
name = ['Adam', 'is', 'very', 'cool']

# 创建值一样的列表
name_2 = ['Adam', 'is', 'very', 'cool']
# 浅复制
name_3 = name[:]
```

### 2.6 列表参数

元组可以通过`*`运算符作为参数传入函数中，列表也可以作为参数输出到函数中，此时函数会得到列表的一个引用，意味着如果函数中对列表进行了修改，那么原列表也将被修改，示例如下：

```Python
#定义一个函数，删除列表的第一个元素
def del_head(t):
  del t[0]

name = ['Adam', 'is', 'very', 'cool']
del_head(name)
print(name)
```

输出为：

```
['is', 'very', 'cool']
```

参数t和变量name指向同一个列表，因此当t变化时，name也变化了。这个知识点十分重要，在编写函数时，要非常注意操作是否会创建一个新的列表，还是在原有列表上作变化。

### 2.7 映射和列表推导式

如果想通过一个函数对列表进行操作，映射（map）和列表推导式是很好的选择。Python提供的内置函数map接收两个参数 - 映射函数和迭代对象，返回一个迭代对象，示例如下：

```Python
# 返回元素的平方
def square(n):
    return n*n

test_list = [1,2,4,5]
result = map(square, test_list)
print(result)
print(list(result))
```

输出为：

```
<map object at 0x1101b9400>
[1, 4, 16, 25]
```

使用列表推导式也可以完成上述操作：

```Python
test_list = [1,2,4,5]
result = [i*i for i in test_list]
print(result)
```

输出为：

```
[1, 4, 16, 25]
```

## 3 总结

上述知识基本概括了列表的常见操作，简单总结一下经验：

- 大部分列表方法都是修改参数并返回None，一定要注意选择合适的方法，确保变量的安全性。
- 实现同一种操作有很多种办法，有时用错误的方法不会报错，但结果有可能不对，确保理解了个中差异后再选择合适的方法。
- 谨慎使用列表的别名，其实不止列表，其他的数据类型也会有别名的机制。

希望这些知识点对你有帮助，来一道leetcode算法题巩固一下列表知识吧，欢迎在评论区留下你的答案！下次我们将聊聊字典（Dict）。

题目：旋转数组

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。示例：

```
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
