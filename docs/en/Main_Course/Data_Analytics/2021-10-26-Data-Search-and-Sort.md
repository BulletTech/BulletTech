---
template: overrides/blogs.html
tags:
  - analytics
  - python
---

# A Brief Discussion on Data Search and Sorting

!!! info
    Author: Tina, Published on 2021-10-28, Read Time: about 6 minutes, WeChat article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/r8WJdmDF4h7xsVRSXnHRKA)

## 1 Introduction

As a data analyst, we can't do without the important concepts of search and sorting in data structures.

Knowing various sorting and searching algorithms can help us choose the sorting and searching methods in our work, not only considering the characteristics of the data, but also considering the computing resources. Next, we will briefly introduce several data search and data sorting methods using Python code.

## 2 Implementation of Python Code

### 2.1 Data Search
#### 2.1.1 Sequential Search

One of the characteristics of Python lists is that each element has its own position, and the position of a data item is its subscript. Because subscripts are ordered, each element can be accessed in order, just like `Sequential Search`. As the name suggests, sequential search will start at the beginning of the list and look at each one in order until it finds the target element or completes the list.

```python
## This function accepts a list and a target element as parameters, and returns a Boolean value representing whether the target element exists.
def sequential_Search(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found
```

In fact, before the computer analyzes the search algorithm, it needs to define the basic unit of calculation. Each comparison has only two results, which are found or not found. We made an assumption here that the arrangement of the elements is disordered, in other words, the possibility of the target element being in each position is equal. If it is in an ordered arrangement, the computing resources will change with the position of the target element in the list.

#### 2.1.2 Binary Search

Unlike sequential search, `Binary Search` does not search the list from the first position, but starts from the middle element. If this element is the target element, the search stops immediately; if not, it can use the ordered feature of the list to exclude half of the elements.

Repeat the binary search process for the right (left) half. Starting from the middle element, compare it with the target element. Similarly, either directly find the target element, or split the right (left) half according to the comparison result and further narrow down the search scope.

```python
## Binary search of an ordered list
def binary_Search(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) //2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
     return found
```
### 2.2 Data Sorting
#### 2.2.1 Bubble Sort

Bubble sort traverses the list multiple times. It compares neighboring elements, swaps those that are out of order, and sorts them in order from left to right. Each round of traversal will place the next maximum value in its correct position. Essentially, each element finds its own position through "bubbling".

During the first round of traversal, the first two elements are compared continuously. If there are n elements, n-1 comparisons will be made. Note that, in each comparison, the larger one will keep moving to the left until the traversal is completed.

The second round of traversal begins with the largest value already in its correct position. There are still n-1 elements to be sorted, which means n-2 pairs need to be compared. Since each round places the next maximum value in its correct position, the number of rounds to be traversed is n-1.

```python
def bubble_Sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
```

#### 2.2.2 Selection Sort

`Selection Sort` improves on bubble sort by making only one swap during each traversal of the list. This requires that the sorting algorithm only looks for the maximum value during each traversal, and places it in its correct position after the traversal.

```python
def select_Sort(alist):
    for s in range(len(alist)-1, 0, -1):
        max_p = 0
        for p in range(1, s + 1):
            if alist[p] > alist[max_p]:
                max_p = p

        temp = alist[s]
        alist[s] = alist[max_p]
        alist[max_p] = temp
```

#### 2.2.3 Insertion Sort

`Insertion Sort` maintains an ordered sublist on the smaller end of the list and inserts each new element one by one into this ordered sublist.

First, assume that the element at position 0 is a sorted sublist containing only one element. From element 1 to element n-1, each element is compared with the