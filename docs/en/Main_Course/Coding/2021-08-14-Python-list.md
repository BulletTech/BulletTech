---
template: overrides/blogs.html
tags:
  - python
---

# Tips for Common Operations on Python Lists

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-08-14, Reading Time: about 6 minutes, Wechat Official Account Article Link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484437&idx=1&sn=6d58dbd242157e216cb0e573678686d9&chksm=eb90f761dce77e7711ad25f26be3ff212d80db386a74d5902af1247e027e1108c84ec8d0fb7c&token=891223383&lang=zh_CN#rd)

## 1. Preface

In the previous article, we reviewed the [common operations on Python tuples](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&tempkey=MTEyNl96d1NDWlZlNm1CSWJxKzEyeTlkcTIybWVyQmlFcFJWZncyZGFqZndNUFl1dHA2R1Jzb09STmVLYzZNeGNFUk5nUDJsanZSOUMzMFpLbUlmTUhzOWVUeDZVUjM5MnJtVlc3MkpTRWc0a1haaDBGdmFJUDVLLVFUR29QYlhteDhaN3RTRmpNZFRJTVBJTGs5cmpCcHdtMnAzQjhTbjl2aXBxRzl1S1p3fn4%3D&chksm=6b90f0865ce77990c57a2be4493364667bb91c1a0f0d2f70498bc6f318395c9abbcc5f9cd376#rd), in this article, let's talk about another common data type in Python: lists.

Like tuples, lists are also sequences created by square brackets `[]`. The values in the list are commonly referred to as elements, and the data type of the elements can be different. For example, `test_list = [0,1,1,'a','b']` can successfully create a list.

Unlike tuples, lists are mutable sequences, so the operations available for sequences will be more flexible. Next, we will review the most commonly used operations on lists.

## 2. Common operations on lists

### 2.1 Traversal

Taking the list `people = ['Adam','Nick','Tony']` as an example, we can use a for loop to traverse:

```python
for i in people:
  print(i)
```

When updating the list, using an index to traverse will be more convenient:

```python
for i in range(len(people)):
  people[i] += '_suffix'
```

### 2.2 Slicing

Like tuples, you can get the elements of a list by slicing (the index in Python starts from 0):

```python
print(people[:2])
```

Output:

```
['Adam','Nick']
```

### 2.3 Deleting Elements

a. The `pop` method can return the value to be deleted, and you can use an index to delete or delete the last element: `a = people.pop(2)` or `a = people.pop()`, the value of `a` will be `'Tony'`, and the original list will delete the corresponding element.

b. If you don't need the deleted value, `del` is a good method: `del people[0]`, then the list `people` will become `['Nick','Tony']`.

c. The `remove` method will delete the first required element in the list. For example, after the `test_list.remove(1)` operation, the list will become `test_list = [0,1,'a','b']`. Note that the `remove` method does not return any value.

### 2.4 Interaction between Lists and Strings

Lists and strings can be flexibly converted. For example, convert a string to a list:

```python
# Convert string to list
name = 'Adam is very cool'
name_list_1 = list(name)
print(name_list_1)

# The split method can split the string using a delimiter
name_list_2 = name.split()
print(name_list_2)
```

Output:

```
['A', 'd', 'a', 'm', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 'c', 'o', 'o', 'l']

['Adam', 'is', 'very', 'cool']
```

Sometimes you need to merge a list into a string, the `join` method is very useful:

```Python
# Join the elements in the list with spaces into a new string
print(' '.join(['Adam', 'is', 'very', 'cool']))
```

Output:

```
'Adam is very cool'
```

### 2.5 Aliases of Lists

This is a point that is easy to make a mistake. In the following code, two variables are exactly the same, changing one will also change the value of the other:

```Python
# alias is an alias for the list name
name = ['Adam', 'is', 'very', 'cool']
alias = name
alias.pop()
print(name)
```

Output:

```Python
['Adam', 'is', 'very']
```

Therefore, when you want to use two independent lists, try to use separate assignment statements or shallow copies:

```Python
name = ['Adam', 'is', 'very', 'cool']

# Create a list with the same values
name_2 = ['Adam', 'is', 'very', 'cool']
# Shallow copy
name_3 = name[:]
```

### 2.6 List Arguments

Tuples can be passed into functions as parameters using the `*` operator, and lists can also be passed as parameters to functions. At this time, the function will get a reference to the list, which means that if the function modifies the list, the original list will also be modified. The following example demonstrates this:

```Python
# Define a function to delete the first element of a list
def del_head(t):
  del t[0]

name = ['Adam', 'is', 'very', 'cool']
del_head(name)
print(name)
```

Output:

```
['is', 'very', 'cool']
```

Parameter `t` and the variable `name` refer to the same list, so when `t` changes, `name` also changes. This knowledge point is very important. When writing functions, be very careful about whether the operation will create a new list or make changes to the original list.

### 2.7 Mapping and List Comprehensions

If you want to operate on a list with a function, mapping and list comprehensions are good choices. The built-in function map provided by Python takes two parameters - a mapping function and an iterable object, and returns an iterable object. The following example demonstrates this:

```Python
# Return the square of the element
def square(n):
    return n*n

test_list = [1,2,4,5]
result = map(square, test_list)
print(result)
print(list(result))
```

Output:

```
<map object at 0x1101b9400>
[1, 4, 16, 25]
```

You can also use list comprehensions to perform the same operation:

```Python
test_list = [1,2,4,5]
result = [i*i for i in test_list]
print(result)
```

Output:

```
[1, 4, 16, 25]
```

## 3. Summary

The above knowledge basically summarizes the common operations on lists. Here are some brief experiences:

- Most list methods modify the parameter