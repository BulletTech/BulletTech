---
template: overrides/blogs.html
---

!!! info 
    作者：Tina，发布于2021-10-27，阅读时间：，微信公众号文章链接：[:fontawesome-solid-link:]()
# 浅谈数据的搜索和排序

## 1. 引言
作为一名数据分析师，当然离不开数据结构中的重要概念 ——搜索和排序。了解各类排序和搜索算法，可以帮助我们在工作中选择排序和搜索方式时，不仅要考虑数据的特点，还要考虑计算资源。接下来，我们就来简单地用Python代码介绍几种数据搜索和数据排序方法。

## 2. Python的代码实现
### 2.1 数据搜索
#### 2.1.1 顺序搜索
Python列表的特点之一就是每一个元素都有自己的位置，数据项的位置就是它的下标。因为下标是有序的，所以能够有序访问每个元素，由此可以进行**顺序搜索**。顾名思义，顺序搜索将会从列表中最开始的位置开始按照顺序逐个查看，直到找到目标元素或查完列表为止。
```python
##此函数接受列表与目标元素作为参数， 并返回一个表示目标元素是否存在的布尔值。
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
其实，计算机在分析搜索算法前，需要定义计算的基本单元。每一次比较只有两种结果，找到或没有找到。在这我们做了一个假设，即元素的排列是无序的，也就是说，目标元素位于每个位置的可能性是一样大。如果是有序排列，那么计算资源就会由目标元素在列表中的位置而变化。

#### 2.1.2 二分搜索
与顺序搜索不一样的是，二分搜索不是从第一个位置开始搜索列表，而是从中间元素着手。如果这个元素就是目标元素，那就立即停止搜索；如果不是，则可以利用列表有序的特性，排除一半的元素。
针对右（左）半部分重复二分过程。从中间元素着手，将其和目标元素比较。同理，要么直接找到目标元素，要么根据比较结果将右（左）半部分一分为二，再次缩小搜索范围。
```python
## 有序列表的二分搜索
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
### 2.2 数据排序
### 2.2.1 冒泡排序
冒泡排序多次遍历列表。它比较相邻的元素，将不合顺序的交换，左小右大的顺序排列。每一轮遍历都将下一个最大值放到正确的位置上。本质上，每个元素都通过“冒泡”找到自己所属的位置。

第一轮遍历过程中，将第一个连续两个元素进行比较，如果有n个元素，那么将进行n-1次比较。注意，每次比较中，大的会一直往左挪，直到遍历结束。

第二轮遍历开始，最大值已经在正确位置上了。还剩n-1个元素需要排列，也就是说要比较n-2对。既然每一轮都将下一个最大值放到正确位置上，那么需要遍历的轮数就是n-1。

```python
def bubble_Sort(alist):
  for passnum in range(len(alist)-1, 0, -1):
    for i in range(passnum):
      if alist[i] > alist[i+1]:
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp
```
#### 2.2.2 选择排序
**选择排序**在冒泡排序的基础上做了改进，每次遍历列表只做一次交换。这就要求选择排序在每次遍历时只寻找最大值，并在遍历之后将它放到正确位置上。
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
#### 2.2.3 插入排序
**插入排序**是在列表较小的一端维护一个有序的子列表，并逐个将每个新元素“插入”这个子列表。

首先假设位置0处的元素是只含单个元素的有序子列表。从元素1到元素n-1，每一轮都将当前元素与有序子列表的元素进行比较。在有序子列表中，将比它大的都右移；当遇到一个比它小的元素或抵达子列表终点时，就可以插入当前元素了。
```python
def insert_Sort(alist):
  for index in range(1,len(alist)):
    current_value = alist[index]
    position = index
    
    while position > 0 and alist[position-1] > current_value:
      alist[position] = alist[position-1]
      position = position -1
      
    alist[position] = current_value
```
#### 2.2.4 希尔排序
**希尔排序**也称“递减增量排序”，它基于插入排序做了改进，将列表分成n个子列表，并对每一个子列表应用插入排序。希尔排序并不采用连续切分，而是有一个可以控制的增量参数i来选取间隔为i的元素从而组成子列表。
```python
def shell_Sort(alist):
  count_sub = len(alist) // 2
  while count_sub > 0:
    for start in range(count_sub):
        gap_sort(alist, start, count_sub)
    print("After increments of size", count_sub, "The list is", alist)

    count_sub = count_sub // 2
  
def gap_sort(alist,start,gap):
  for i in range(start+gap,len(alist), gap):
    current_value = alist[i]
    p = i
    
    while p >=gap and alist[p-gap] > current_value:
      alist[p] = alist[p-gap]
      p = p - gap
    alist[p] = current_value  
```
因为希尔排序最后一步要做一次完整的插入排序，是不是觉得希尔排序没有插入排序好？其实不然，列表已经由增量的插入排序做了预处理，所以最后一步插入排序不需要进行多次比较或者移动的，并不会消耗太多的计算资源。
#### 2.2.5 归并排序
**归并排序**是一种递归算法，每次将一个列表一分为二。如果列表为空或只有一个元素，那么从定义上说它就是有序的。如果列表不止有一个元素，就将一分为二，并对两部分都先递归调用再归并排序。当两部分都有序后，就再一次进行**归并**操作。

```python
def merge_Sort(alist):
  print("Splitting ", alist)
  if len(alist) > 1:
    mid = len(alist) // 2
    left_half = alist[:mid]
    right_half = alist[mid:]
    
    merge_Sort(left_half)
    merge_Sort(right_half)
    
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        alist[k] = left_half[i]
        i = i + 1
      else:
        alist[k] = right_half[j]
        j = j +1
      k = k + 1
      
    while i < len(left_half):
      alist[k] = left_half[i]
      i = i + 1
      l = k + 1
      
    while j < len(right_half):
      alist[k] = right_half[j]
      j = j + 1
      k = k + 1
    print("Merging ", alist)
```


### 2.2.6 快速排序
和归并排序一样，**快速排序**也采用分治策略，但不会使用额外的存储空间。不过，代价是列表可能不会被一分为二。快速排序首先会选出一个基准值。基准值的作用是帮助切分列表，也可理解为**分割点**，算法在分割点切分列表，以进行快速排序的子调用。

```python
def quick_Sort(alist):
  quick_Sort_Helper(alist, 0, len(alist)-1)

def quick_Sort_Helper(alist, first, last):
  if first < last:
    
    split_point = partition(alist,first,last)
    quick_Sort_Helper(alist, first, split_point - 1)
    quick_Sort_Helper(alist, split_point + 1, last)

def partition(alist, first, last):
  pivot_value = alist[first]
  left_mark = first + 1
  right_mark = last
  done = False
  while not done:
    
    while left_mark <= right_mark and alist[left_mark] <= pivot_value:
      left_mark = left_mark + 1
    while alist[right_mark] >= pivot_value and right_mark >= left_mark:
      right_mark = right_mark - 1
    if right_mark < left_mark:
      done = True
    else: 
      temp = alist[left_mark]
      alist[left_mark] = alist[right_mark]
      alist[right_mark] = temp
  temp = alist[first]
  alist[first] = alist[right_mark]
  alist[right_mark] = temp
      
  return right_mark
```

## 3.总结
总的来说，搜索和排序的算法有很多，但是没有哪一种是完美无缺的。只有了解每种算法的基本原理和优缺点，尽可能地去规避它的不足，才有可能帮助我们选择最适合自己工作内容的方法和相对应的开源接口。

希望这篇简单的介绍可以让你有所收获，也欢迎各位小伙伴留言讨论哦。
<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>

### 参考文献
[1] 《Python数据结构与算法分析》
