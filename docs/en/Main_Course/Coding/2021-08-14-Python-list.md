---
template: overrides/blogs.html
tags:
  - python
---

# Python列表常用操作小技巧

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-08-14，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484437&idx=1&sn=6d58dbd242157e216cb0e573678686d9&chksm=eb90f761dce77e7711ad25f26be3ff212d80db386a74d5902af1247e027e1108c84ec8d0fb7c&token=891223383&lang=zh_CN#rd)

## 1 Introduction


In the previous article, we reviewed
[Common operation of the python element group] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3ngxoq=&TEMPKEY=mteynl96dwlzlnmwjxkzeyqmlFCFJWZNCY ZGFQZNDNUFL1JZB09stmvlyzznegnfuk5NudjsoumzMFPLMTUHZUEDZUJM5MNJTVLC3MK3MK3MK3MK3MK3MK3MK3MK3MK3MNJT RTRMPNZFRJTVBJTGS5CMPCCCHDTMNAZQJHTBJL2AXBXRZL1S1P3FN4%3d & CHKSM = 6b90F0865CE77A2BE44933666670D2F070498BC6183999318399 5C9ABBCC5F9CD376#RD)
We continue to talk about another commonly used data type -list (list) in Python.


Like the Yuan group, the list is also a sequence, which can be created through square brackets `[` and `].The values in the list are often called elements, and the data types of the element can be different.


Different from the tuples, the list is a variable sequence, so the operation of the sequence can be more flexible. Next, let's review the most commonly used operations of the list.


## 2 List commonly used operation


### 2.1 travers


Taking the list `people = ['adam', 'nick', 'tony']` as an example, you can use the for loop to traverse:


```python
for i in people:
print(i)
```


When you need to update the list, it will be more convenient to use the bidding traversal:


```python
for i in range(len(people)):
people[i] += '_suffix'
```


### 2.2 Slice


Like the Yuan group, you can obtain the element of the list by slicing (the bid in Python starts from 0):


```python
print(people[:2])
```


The output is:
```
['Adam','Nick']
```


### 2.3 Delete elements


a. POP method can return the value to be deleted, you can use the bidding to delete, or delete the last element: `A = People.pop (2)` or `a = peple.pop ()`, `a` of the value of` a`, `a`They will be `tony'`, and the original list will delete the corresponding elements.


b. If you do n’t need to use the deleted value, Del is a good way: `Del people [0]`, then the list of the `people will become` ['nick', 'tony'] `.


c. Remove method will delete the first element to delete in the list, such as `test_list.remove (1)` operation, the list will become `test_list = [0,1, 'a', 'b']`, Note that the Remove method will not return any value.




### 2.4 list and string


List and string can be converted flexibly, such as converting the string into a list:


```python
# Convert the string into a list
name = 'Adam is very cool'
name_list_1 = list(name)
print(name_list_1)


# SPLIT method can use a separatist scholarship strings
name_list_2 = name.split()
print(name_list_2)
```


The output is:


```
['A', 'd', 'a', 'm', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 'c', 'o', 'o', 'l']


['Adam', 'is', 'very', 'cool']
```


And sometimes it is necessary to merge the list into a string. The method is very easy to use:


```Python
# Use the element to connect the list with a space to form a new string
print(' '.join(['Adam', 'is', 'very', 'cool']))
```


The output is:


```
'Adam is very cool'
```


### 2.5 list alias


This is a point that is easy to make errors. In the following code, the two variables are exactly the same, change one, and the other value will be changed:


```Python
# alias is the alias of list name
name = ['Adam', 'is', 'very', 'cool']
alias = name
alias.pop()
print(name)
```


The output is:


```Python
['Adam', 'is', 'very']
```


Therefore, when you want to use two independent lists, try to use a separate assignment statement or shallow replication:


```Python
name = ['Adam', 'is', 'very', 'cool']


# Create the same list list
name_2 = ['Adam', 'is', 'very', 'cool']
#
name_3 = name[:]
```


### 2.6 list parameter


The tuple can be passed into the function through the `*` operator as a parameter, and the list can also be output into the function as a parameter. At this time, the function will get a quotation of the list, which means that if the list is modified in the function, the original list of the original list willIt will also be modified, the example is as follows:


```Python
#Define a function, delete the first element of the list
def del_head(t):
of T [0]


name = ['Adam', 'is', 'very', 'cool']
del_head(name)
print(name)
```


The output is:


```
['is', 'very', 'cool']
```


Parameter T and variable name point to the same list, so when T changes, name also changes.This knowledge point is very important. When writing functions, pay attention to whether the operation will create a new list or change on the original list.


### 2.7 mapping and list derivative


If you want to operate the list by a function, mapping (MAP) and list derivation are a good choice.The built -in function Map provided by Python receives two parameters -mapping functions and iteration objects, and returns an iteration object. The example is as follows:


```Python
# Return to the square of element
def square(n):
return n*n


test_list = [1,2,4,5]
result = map(square, test_list)
print(result)
print(list(result))
```


The output is:


```
<map object at 0x1101b9400>
[1, 4, 16, 25]
```


You can also complete the above operation with the list derivative:


```Python
test_list = [1,2,4,5]
result = [i*i for i in test_list]
print(result)
```


The output is:


```
[1, 4, 16, 25]
```


## 3 Summary


The above knowledge basically summarizes the common operations of the list, and simply summarize the experience:


-Dyn list method is to modify the parameters and return NONE. Be sure to choose the right method to ensure the safety of the variable.
-It has many ways to achieve the same operation. Sometimes the errors are not reported in the wrong method, but the result may be wrong. Make sure that the appropriate method is selected after understanding the difference.
-The aliases of the list of caution, in fact, more than the list, other data types will also have aliases mechanisms.


I hope these knowledge points will be helpful to you. Come on the LeetCode algorithm to consolidate the list of knowledge. Welcome to leave your answer in the comment area!Next time we will talk about the dictionary.


Title: Rotate array


Given an array and move the element in the array to the right position, where K is not negative.Example:


```
Enter: nums = [1,2,3,4,5,6,7], K = 3
Output: [5,6,7,1,2,3,4]
explain:
Step to the right: [7,1,2,3,4,5,6]
Step to the right: [6,7,1,2,3,4,5]
Rotate 3 steps to the right: [5,6,7,1,2,3,4]


Author: LEETCODE
Link: https://letcode-cn.com/leetbook/read/top-nterview-qiestions-easy/x2skh7///
Source: LEETCODE
Copyright belongs to the author.Please contact the author for business reprints. Please indicate the source for non -business reprints.
```


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>