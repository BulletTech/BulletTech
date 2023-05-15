---
template: overrides/blogs.html
tags:
  - python
---

# Python元组常用操作小技巧

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-08-07，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/GmZ1Du4qJRai7D7oXKh75w)

## 1 Introduction


Python has received a lot of attention as the current in the field of data science and artificial intelligence, and many people are learning.However, on the way to pursue excellence, you must not ignore the foundation, such as the best practice of common data structure, grammatical specifications, and programming thinking. The most basic things are fingered, and the work on the basis of this will be ease.


Let's first review and summarize the common operation in the Python data structure: The common data structures in Python can be collectively referred to as container.Sequences (such as lists and metal groups), mapping (such as dictionary) and collection (SET) are three main containers.The flat sequences such as Str, Bytes, bytearray, MemoryView, and Array.array are not within the scope of this article.


Here, let's start with the Yuan Group.


## 2 yuan group is not only an unchanged list


### 2.1 Cost


One of the significant features of the Yuan Group is different from the list is that it cannot be modified, but the other role is
[Used for records without field names] (https://book.douban.com/subject/27028517/)
EssenceBecause the latter is often ignored, let's take a look at the role of the tuple as a record.


A group group can be defined with brackets.Each element in the tuples stores the data of a field in the record, plus the location of this field.It is this location information that gives the data meaning.In the following example, the tuples are used as records:


```Python
#The latitude and longitude of Los Angeles International Airport, recorded with the Yuan Group
lax_coordinates = (33.9425, -118.408056)


# Some information in Tokyo: city name, year, population (unit: millions), population change (unit: percentage) and area (unit: square kilometer)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)


#, The form of the tuples is (country_code, passport_number).
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]


#During the iteration, the Passport variable is bound to each group.The % format operator can be matched on the corresponding meta -group element.
for passport in sorted(traveler_ids):
print('%s/%s' % passport)
```


The output is:


```
BRA/CE342567
ESP/XDA205856
USA/31195855
```


### 2.2 yuan for disassembly bags


The operation in the above For loop extracts the elements in the turtle group, also called unpacking.Parallel assignment is a good application for the tuple disassembly. The example is as follows:


```Python
#The latitude and longitude of Los Angeles International Airport, recorded with the Yuan Group
lax_coordinates = (33.9425, -118.408056)
# Disassembling the Bao Yuan Group, assigning the elements in the turtle group to the corresponding variable
latitude, longitude = lax_coordinates
```


Another classic and elegant application is the value of the exchange variable:


```Python
a, b = b, a
```


### 2.3 yuan group as a function parameter


Use the `*` to disassemble an iterative object as a parameter of the function. For example, the built -in function of Python receives the parameters of the two digital types, and returns the quotient and the remaining numbers.The following example will use the `*` to pass the Yuan group into the function.


```Python
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)
```
The output is:


```
2 4
```


### 2.4 yuan group as a function return value


Some functions have multiple return values. When they are assigned to a variable, the variable type is the tuple:


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


The output is:


```
(8, 40)
```


### 2.5 zip function


ZIP is a built -in function of Python, which can receive two or more sequences and form a list list. A iterator will be returned in Python3, as shown below:


```Python
list_a = [1,2,3]
list_b = ['a','b','c']


for i in zip(list_a, list_b):
print(i)
```


The output is:


```
(1, 'a')
(2, 'b')
(3, 'c')
```


### 2.6 Other conventional operations


Of course, the Yuan group also supports some conventional operations, such as the Yuan Group `A = (1, 'y', 5, 5, 'x')` `` ``:


-In `A.INDEX ('X')` `
-Adl, such as `A [1: 4]`
-Accut, such as `A.Count (5)`
-Step, such as `a.sort ()` `
-Ame merger, such as `C = A + A`


## 3 Summary


The above content not only covers the basic operations of the turtle group, but also combines other functions, operators, and operators often used in actual work.When reviewing these knowledge, I mainly refer to two classic Python programming books: "Fastest Python" and "Thinking of Python like computer scientists", interested friends can read in depth!


I hope this article will be helpful to you. The next time I will summarize the use of the Python list.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>