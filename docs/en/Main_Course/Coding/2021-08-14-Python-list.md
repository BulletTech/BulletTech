---
template: overrides/blogs.html
tags:
  -Python
---

# Python list commonly used tips for operation

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-08-14, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-solid-Link:] (https:: https:: https:: https:: https:: https://mp.weixin.qqqpom/s ?__biz=mzi4mjk3nzgxoq===2247484437IDX=1&Sn=6d58dbd24216cb0e573686d90f761dce7777711 AD25F26BE3FF212DB386A74D5902AF1247E027E1108C84EC8D0FB7C & Token = 891223383 & Lang = zh_cn#RD)

 ## 1 Introduction

 In the previous article, we reviewed the [common operation of the python group] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq==&TEMPKEY=MTeynl96D1CSWJXKZETLKTIYBWV YQMLFCFJWZNCFQZNDNUFL1DHA2R1JZB09STMVLYZZNEGNFUK5NUDJSOUMZMFPLMTUHZUHZUEDZUJM5MNJTVLC3MK3MKDMFJUDVLLLLVFU R29qylhtedhan3RMPNZFRJTVBJTGS5CMPCCHDTMNAZQJHTBJL2AXBXRZL1S1P3FN4%3D & CHKSM = 6B90F0865CE777A2BE449336666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666667B9C1A0D2F7F0D2F0D2F0 0498BC6F318395C9ABBCC5F9CD376#RD), thisWe continue to talk about another commonly used data type-list (list) in Python.

Like the Yuan group, the list is also a sequence, which can be created through square brackets `[` and `].The values in the list are often called elements, and the data types of the element can be different.

Different from the tuples, the list is a variable sequence, so the operation of the sequence can be more flexible. Next, let's review the most commonly used operations of the list.

## 2 List commonly used operation

### 2.1 travers

Taking the list `people = ['adam', 'nick', 'tony']` as an example, you can use the for loop to traverse:

`` `python
for I in people:
  Print (i)
`` `

When you need to update the list, it will be more convenient to use the bidding traversal:

`` `python
for I in Range (Len (PEOPLE)):
  people [i] += '_suffix'
`` `

### 2.2 Slice

Like the Yuan group, you can obtain the element of the list by slicing (the bid in Python starts from 0):

`` `python
Print (PeOPLE [: 2])
`` `

The output is:
`` `
['Adam', 'nick']
`` `

### 2.3 Delete elements

a. POP method can return the value to be deleted, you can use the bidding to delete, or delete the last element: `A = People.pop (2)` or `a = peple.pop ()`, `a` of the value of` a`, `a`They will be `tony'`, and the original list will delete the corresponding elements.

b. If you do n’t need to use the deleted value, Del is a good way: `Del people [0]`, then the list of the `people will become` ['nick', 'tony'] `.

c. Remove method will delete the first element to delete in the list, such as `test_list.remove (1)` operation, the list will become `test_list = [0,1, 'a', 'b']`, Note that the Remove method will not return any value.


### 2.4 list and string

List and string can be converted flexibly, such as converting the string into a list:

`` `python
# Convert the string into a list
name = 'adam is very cool'
name_list_1 = list (name)
Print (name_list_1)

# SPLIT method can use a separatist scholarship strings
name_list_2 = name.split ()
Print (name_list_2)
`` `

The output is:

`` `
['A', 'd', 'a', 'm', '', 'I', 's',' ',' v ',' e ',' r's'c', 'o', 'o', 'l']

['Adam', 'is', 'very', 'cool']
`` `

And sometimes it is necessary to merge the list into a string. The method is very easy to use:

`` `Python
# Use the element to connect the list with a space to form a new string
Print ('' .join (['adam', 'is', 'very', 'cool']))
`` `

The output is:

`` `
'Adam is very cool'
`` `

### 2.5 list alias

This is a point that is easy to make errors. In the following code, the two variables are exactly the same, change one, and the other value will be changed:

`` `Python
# alias is the alias of list name
name = ['adam', 'is', 'very', 'cool']
alias = name
alias.pop ()
Print (name)
`` `

The output is:

`` `Python
['Adam', 'is', 'very']
`` `

Therefore, when you want to use two independent lists, try to use a separate assignment statement or shallow replication:

`` `Python
name = ['adam', 'is', 'very', 'cool']

# Create the same list list
name_2 = ['adam', 'is', 'very', 'cool']
#
name_3 = name [:]
`` `

### 2.6 list parameter

The tuple can be passed into the function through the `*` operator as a parameter, and the list can also be output into the function as a parameter. At this time, the function will get a quotation of the list, which means that if the list is modified in the function, the original list of the original list willIt will also be modified, the example is as follows:

`` `Python
#Define a function, delete the first element of the list
DEF DEL_HEAD (T):
  Del T [0]

name = ['adam', 'is', 'very', 'cool']
del_head (name)
Print (name)
`` `

The output is:

`` `
['is', 'very', 'cool']
`` `

Parameter T and variable name point to the same list, so when T changes, name also changes.This knowledge point is very important. When writing functions, pay attention to whether the operation will create a new list or change on the original list.

### 2.7 mapping and list derivative

If you want to operate the list by a function, mapping (MAP) and list derivation are a good choice.The built -in function Map provided by Python receives two parameters -mapping functions and iteration objects, and returns an iteration object. The example is as follows:

`` `Python
# Return to the square of element
DEF SQUARE (N):
    Return n*n

test_list = [1,2,4,5]
result = map (square, test_list)
Print (Result)
Print (List (Result))
`` `

The output is:

`` `
<MAP Object at 0x1101B9400>
[1, 4, 16, 25]
`` `

You can also complete the above operation with the list derivative:

`` `Python
test_list = [1,2,4,5]
result = [i*I for I in test_list]
Print (Result)
`` `

The output is:

`` `
[1, 4, 16, 25]
`` `

## 3 Summary

The above knowledge basically summarizes the common operations of the list, and simply summarize the experience:

-Dyn list method is to modify the parameters and return NONE. Be sure to choose the right method to ensure the safety of the variable.
-It has many ways to achieve the same operation. Sometimes the errors are not reported in the wrong method, but the result may be wrong. Make sure that the appropriate method is selected after understanding the difference.
-The aliases of the list of caution, in fact, more than the list, other data types will also have aliases mechanisms.

I hope these knowledge points will be helpful to you. Come on the LeetCode algorithm to consolidate the list of knowledge. Welcome to leave your answer in the comment area!Next time we will talk about the dictionary.

Title: Rotate array

Given an array and move the element in the array to the right position, where K is not negative.Example:

`` `
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
`` `

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>