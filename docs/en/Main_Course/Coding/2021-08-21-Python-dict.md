---
template: overrides/blogs.html
tags:
  - python
---

# Tips for Common Operations on Python Dictionaries

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan)，Published on 2021-08-21, Reading time: about 6 minutes，WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484449&idx=1&sn=227c9fd7dfa3baacbfeb877570450a52&chksm=eb90f755dce77e4305d6b352e8d4d828edc10456edd92e5d77010ba316582ce9fdd8f2e715af&token=874200166&lang=zh_CN#rd)

## 1 Introduction

In the previous article, we reviewed [common operations on Python lists](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484437&idx=1&sn=6d58dbd242157e216cb0e573678686d9&chksm=eb90f761dce77e7711ad25f26be3ff212d80db386a74d5902af1247e027e1108c84ec8d0fb7c&token=379425388&lang=zh_CN#rd). As a commonly used data type, lists play a very important role in daily work. In this article, we will continue to talk about another commonly used data type in Python - dictionaries (Dict).

Dictionaries can be defined using the `dict()` method or using curly braces, such as `name2code = {'Tony':1, 'Kevin':2, 'Luis':3}`. If you want to add elements, you can use the key-value assignment pattern: `name2code['Nick'] = 0`. It is easy to see that, unlike lists, dictionaries do not use integers as subscripts. Let's take a look at the commonly used methods of dictionaries.

## 2 Common Dictionary Methods

### 2.1 Indexing

Since dictionaries are in the form of key-value pairs, you can use the key to index the value you need. For example:

```python
print(name2code['Nick'] )
```

Output:

```python
0
```

Similarly to lists, you can use the `in` operator to check whether the dictionary contains the key you want to find. It is worth noting that the implementation of the `in` operator in lists and dictionaries is different. Lists use a search algorithm, so when the list becomes longer, the search time will also become longer. But dictionaries use a hash table algorithm, so regardless of how many key-value pairs there are in the dictionary, the `in` operator takes almost the same amount of time.

```python
print('Nick' in name2code)
```

Output:

```python
True
```

If you want to see whether a value is in the dictionary, you can use the `values()` method to extract the values from the dictionary and use the `in` operator to check:

```python
values = name2code.values()
print(0 in values)
```

Output:

```python
True
```

### 2.2 Deleting Elements

The method for deleting elements from a dictionary is similar to that for a list:

- To clear a dictionary: `name2code.clear()`, note that the `clear()` method has no return value
- Remove the key-value pair associated with the key k and return the corresponding value: `name2code.pop(k, [default])`
- Return the last key-value pair added and remove it: `name2code.popitem()`

### 2.3 Looping

You can use a for loop to iterate through the keys of a dictionary. Please note that because the keys are hashable, their appearance does not follow a specific order. The following code may have a different output order on your computer (Note: Python 3.6 and later versions retain the order in which the key-value pairs were added, so the result is determined):

```python
for i in name2code:
    print(i, name2code[i])
```

Output:

```python
Tony 1
Kevin 2
Luis 3
Nick 0
```

If you want to iterate through both the key and value, you can use the `items()` method:

```python
for k,v in name2code.items():
    print(k,v)
```

Output:

```python
Tony 1
Kevin 2
Luis 3
Nick 0
```

### 2.4 Reverse Lookup

For a dictionary, the operation of using a key to find a value has been introduced above. If you want to use a value to find its associated key, then you need to perform a reverse lookup. Note that a `raise` statement is used here to throw an exception, which is used to display the value of the parameter being searched.

```python
def reversed_lookup(d, v):
    for i in d:
        if d[i] == v:
            return i
    raise ValueError("The value being searched for is not in the dictionary")

reversed_lookup(name2code,5)
```

Output:

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-33-832e824fe6b4> in <module>
----> 1 reversed_lookup(name2code,5)

<ipython-input-32-be75152f6e58> in reversed_lookup(d, v)
      4             return i
      5
----> 6     raise ValueError("The value being searched for is not in the dictionary")

ValueError: The value being searched for is not in the dictionary
```

### 2.5 Dictionary Comprehension

Starting from Python 2.7, list comprehension and generator expressions have also been ported to dictionaries. For example:

```python
code2name = {code:name for name,code in name2code.items() if code < 2}
print(code2name)
```

Output:

```python
{1: 'Tony', 0: 'Nick'}
```

## 3 Variants of Dictionaries

In addition to `dict`, there are several other mapping types in the `collections` module of the Python standard library:

- `collections.OrderedDict`: This type keeps the order of keys when they are added, so the iteration order of keys remains consistent. Please note that if you define an ordered dictionary and do not insert any data after that, the original key-value pairs are still unordered, just like a regular dictionary.
- `collections.ChainMap`: This type can hold multiple different mapping objects. When a key lookup operation is performed, these objects are searched one by one until the corresponding key is found. This is commonly used for managing dictionaries that represent different scopes and contexts.
- `collections.Counter`: As the name suggests, this is a counter. When a key is updated, the counter is also updated. It is commonly used to count elements in a hash table or as a multiset (a set where elements occur multiple times).
- `colllections.UserDict`: This class is mainly used for inheritance by users. Inheriting from this class is more convenient than inheriting from `dict` because the methods of built-in types like `dict` usually ignore user-overridden methods, causing unexpected troubles, as detailed in Chapter 12 of [Fluent Python](https://book.douban.com/subject/27028517/).

## 4 Summary

The above knowledge points are very useful in daily work. The following content also covers the summaries of many years of practical experience of Python programmers. Let's review:

- The keys of a dict must be hashable, which means that its hash value cannot change during its lifetime and the object must implement the `__hash__` method to support testing for equality using the `__eq__` method.
- Dictionaries consume a lot of memory. Because dictionaries use hash tables, and hash tables must be sparse, the space utilization rate is low. If the amount of data is huge, it is recommended to use tuples or lists instead.
- Key lookup in dictionary is very efficient. As long as the dictionary can fit into memory, the key lookup speed does not slow down with the increase of data volume, but the fast speed comes at the cost of greater space usage.
- Adding a new key to a dict may change the order of existing keys. The specific reason depends on the implementation of the dict. It is recommended not to iterate and modify the dict at the same time, but to split it into two steps: iterate to find the content that needs to be modified and record it, and