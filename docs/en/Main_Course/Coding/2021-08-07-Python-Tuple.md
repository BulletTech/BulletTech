---
template: overrides/blogs.html
tags:
  - python
---

# Tips for Common Operations with Python Tuples

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), published on August 7, 2021, Read time: about 6 minutes, WeChat article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/GmZ1Du4qJRai7D7oXKh75w)

## 1 Introduction

Python, as a popular programming language, has attracted a lot of attention in the fields of data science and artificial intelligence. Many people are learning it. However, on the road to excellence, we must not neglect the basics, such as common data structures, syntax specifications, and best practices for programming thinking. By mastering these most fundamental things, we can easily handle the work based on them.

Let's first review and summarize the commonly used operations in Python data structures: The common data structures in Python can be collectively referred to as containers. Sequences (such as lists and tuples), mappings (such as dictionaries), and sets are the three main types of containers. Flat sequences such as str, bytes, bytearray, memoryview, and array.array are not within the scope of this article.

Here, we will start with tuples.

## 2 Tuples are not just immutable lists

### 2.1 Record Function of Tuples

One of the significant differences between a tuple and a list is that it cannot be modified, but it has another function [as a record for which there are no field names](https://book.douban.com/subject/27028517/). As the latter is often ignored, let's first look at the role of tuples as records.

A tuple can be defined using parentheses. Each element in the tuple stores the data of a field in the record, plus the position of this field. It is precisely this positional information that gives the data meaning. In the example below, the tuple is used as a record:

```Python
# Latitude and longitude of Los Angeles International Airport, recorded in a tuple
lax_coordinates = (33.9425, -118.408056)

# Information for Tokyo: city name, year, population (in millions), population change (in percentage), and area (in square kilometers), recorded in a tuple
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# A list of tuples in the form (country_code, passport_number)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

# During iteration, the passport variable is bound to each tuple. The % format operator can be matched to the corresponding tuple element.
for passport in sorted(traveler_ids):
  print('%s/%s' % passport)
```

The output is:

```
BRA/CE342567
ESP/XDA205856
USA/31195855
```

### 2.2 Tuple Unpacking

The operation in the above for loop extracts the elements in the tuple, also known as tuple unpacking. Parallel assignment is an excellent application of unpacking tuples, as shown in the example below:

```Python
# Latitude and longitude of Los Angeles International Airport, recorded in a tuple
lax_coordinates = (33.9425, -118.408056)
# Unpack tuple and assign each element in the tuple to the corresponding variable
latitude, longitude = lax_coordinates
```

Another classic and elegant application is to swap the values of variables:

```Python
a, b = b, a
```

### 2.3 Tuples as Function Parameters

Use the `*` operator to unpack an iterable object as a function parameter. For example, Python's built-in function divmod takes two numeric arguments and returns the quotient and remainder. The following example uses `*` to pass the tuple to the function.

```Python
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)
```

The output is:

```
2 4
```

### 2.4 Tuples as Function Return Values

Some functions have multiple return values, and when they are assigned to a variable, the variable type is a tuple:

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

### 2.5 zip Function

Zip is a built-in function in Python that can take two or more sequences and form a list of tuples. In Python 3, it returns an iterator, as shown below:

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

### 2.6 Other Common Operations

Tuples also support some common operations, such as for the tuple `a = (1, 'y', 5, 5, 'x')`:

- Indexing, such as `a.index('x')`
- Slicing, such as `a[1:4]`
- Counting, such as `a.count(5)`
- Sorting, such as `a.sort()`
- Merging tuples, such as `c = a + a`

## 3 Summary

The above content not only covers the basic operations of tuples but also combines other functions, operators, and so on that are often used in practical work. When reviewing this knowledge, I mainly referred to two classic Python programming books: "Fluent Python" and "Think Python: How to Think Like a Computer Scientist," and interested friends can read them in-depth!

I hope this article is helpful to you, and next time, I will summarize the tips for using Python lists. 

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>