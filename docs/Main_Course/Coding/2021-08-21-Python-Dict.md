---
template: overrides/blogs.html
---

# Python列表常用操作小技巧

!!! info
    作者：袁子弹起飞，发布于2021-08-21，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484437&idx=1&sn=6d58dbd242157e216cb0e573678686d9&chksm=eb90f761dce77e7711ad25f26be3ff212d80db386a74d5902af1247e027e1108c84ec8d0fb7c&token=891223383&lang=zh_CN#rd)

## 1 前言

在上一篇文章中，我们回顾了[Python列表的常用操作](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484437&idx=1&sn=6d58dbd242157e216cb0e573678686d9&chksm=eb90f761dce77e7711ad25f26be3ff212d80db386a74d5902af1247e027e1108c84ec8d0fb7c&token=379425388&lang=zh_CN#rd)，列表作为一种常用的数据类型在日常工作中扮演了非常重要的作用，这篇文章我们继续聊聊Python里另一种常用的数据类型 - 字典（Dict）。

定义字典可以使用`dict()`方法，或者使用花括号`name2code = {'Tony':1, 'Kevin':2, 'Luis':3}`，如果想要增加元素，可以使用键值对的赋值模式：`name2code['Nick'] = 0`。很容易看出，不同于列表，字典并不以整数作为下标。接下来我们来看看字典常用的方法。

## 2 字典常用方法

### 2.1 索引

字典以键值对的形式出现，因此可以用键来索引所需要的值，如：

```python
print(name2code['Nick'] )
```

输出为：

```python
0
```

类似于列表，可以使用`in`操作符查看字典中是否含有所要查找的键，值得注意的是，`in`操作符在列表和字典中的实现有所区别，列表使用搜索算法，因此列表变长时，搜索时间也会变长，但是字典使用散列表（hashtable）的算法，因此不论字典中有多少键值对，`in`操作符所花时间都差不多。

```python
print('Nick' in name2code)
```

输出为：

```python
True
```

如果要查看值是否在字典中，可以借助`values`方法取出字典的值，然后用in操作符查看：

```python
values = name2code.values()
print(0 in values)
```

输出为：

```python
True
```

### 2.2 删除元素

字典删除元素的方法与列表类似：

- 清空字典：`name2code.clear()`，注意`clear()`方法没有返回值
- 返回键k对应的值，然后移除该键值对：`name2code.pop(k, [default])`
- 返回最后添加的键值，并移除该键值对：`name2code.popitem()`

### 2.3 循环

使用for循环可以遍历字典的键，请注意，因为键可散列，所以其出现不遵循特定的顺序，以下代码在你的电脑上运行可能会有不同的输出顺序（注：Python 3.6及之后的版本保留了键值对添加的顺序，所以结果是确定的了）：

```python
for i in name2code:
    print(i, name2code[i])
```

输出为：

```python
Tony 1
Kevin 2
Luis 3
Nick 0
```

如果同时想用键和值进行遍历，也可使用`items()`方法：

```python
for k,v in name2code.items():
    print(k,v)
```

输出为：

```python
Tony 1
Kevin 2
Luis 3
Nick 0
```

### 2.4 反向查找

对于一个字典，使用键去找值的操作在上文已做介绍，如果想用值来寻找键，此时应做反向查找的操作，注意这里使用了一个`raise语句`抛出异常，用于显示参数的值有问题。

```python
def reversed_lookup(d,v):
    for i in d:
        if d[i] == v:
            return i
    raise ValueError("所查找的值不在字典中")

reversed_lookup(name2code,5)
```

输出为：

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-33-832e824fe6b4> in <module>
----> 1 reversed_lookup(name2code,5)

<ipython-input-32-be75152f6e58> in reversed_lookup(d, v)
      4             return i
      5 
----> 6     raise ValueError("所查找的值不在字典中")

ValueError: 所查找的值不在字典中
```

### 2.5 字典推导

从Python 2.7开始，列表推导和生成器表达式也被移植到了字典上，示例如下，

```python
code2name = {code:name for name,code in name2code.items() if code < 2}
print(code2name)
```

输出为：

```python
{1: 'Tony', 0: 'Nick'}
```

## 3 字典的变种

除了dict之外，在Python标准库里collections模块中还有若干种不同的映射类型：

- collections.OrderedDict：这个类型再添加键的时候会保持键的顺序，因此键的迭代顺序始终保持一致。但请注意，如果定义完有序字典后没有插入数据的操作，原始的键值对仍然是无序的，和普通字典一样。
- collections.ChainMap：这个类型可以容纳多个不同的映射对象，在进行键查找操作时，这些对象会被逐个查找，直到找到对应的键为止。常用于管理多个代表不同范围和上下文的字典。
- collections.Counter：顾名思义，这是一个计数器，键更新时，计数器也随之更新。常用于为可散列表计数或作为多重集合（集合里元素出现多次。）
- colllections.UserDict：该类主要用于让用户继承，继承这个类会比继承dict要更加方便，主要是因为dict等内置类型的方法通常会忽略用户覆盖的方法，造成意料不到的麻烦，详见[流畅的Python 12章 - 继承的优缺点](https://book.douban.com/subject/27028517/)。

## 4 总结

上述知识点在日常工作中都十分常用，以下内容还涵盖了许多Python程序员多年实践经验的总结，让我们再回顾一下：

- dict的键必须是可散列的。意味着在这个对象的生命周期中散列值不变，并且对象要实现`__hash__`方法，支持通过使用`__eq__`方法验证相等性。
- dict内存耗费巨大。因为字典使用散列表，散列表又必须稀疏，导致空间利用率低下。如果数据量巨大，建议使用元组或者列表。
- 键查询效率很高。只要字典能被装进内存，其键查询速度与不随数据量增大而减缓，但速度快的代价是较大的空间使用。
- 向dict里添加新的键可能会改变已有键的顺序。具体原因与dict实现方式有关，建议不要对dict同时进行迭代和修改，最好分成两步：先迭代找到需要修改的内容并记录下来，迭代之后再对原dict更改。

在回顾这些知识时，自己也有了新的理解和收获，希望这些内容也对你有帮助！
