---
template: overrides/blogs.html
tags:
  -Python
---

# Python dictionary common operation tips

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published at 2021-08-21, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-Solid-Link:] (https://mp.weixin.qqqpom/s ?__biz=mzi4mjk3nzgxoq===224748449&IDX=1&SN=227c9fdfaacbfeb8775752&CHKSM=EB90F75DCE77E4305 305E43305 D6B352E8D4D828EDC10456edd92e5d77010ba316582ce9fdd8F2E715AF & Token = 874200166 & Lang = zh_cn#rd))

## 1 Introduction

In the previous article, we reviewed the [common operation of the python list] (https://mp.weixin.qq.com/s?__biz=mzi4mjk3nzgxoq==2247484437IDX=1&8DBD242157E216CB0E5E5E5E5E5E5E5E5E5E5E5E5E5E5E5E5E5E5E5E 73678686d9 & chksm = EB90F761DCE77711AD25F26BE3FF212DB386A74D5902AF124E027E1108C84EC8D0FB7C & Token = 379425388 & LANG = ZH_CN#rd), the list as a commonly used data type plays a very important role in daily work. In this article, we continue to talk about another commonly used data type-dictionary (DICT) in Python.

The definition dictionary can use the `diction ()` method, or use the parentheses `name2code = {'tony': 1, 'kevin': 2, 'luis': 3}`, if you want to increase the element, you can use the key value pair pair pair pairAssignment mode: `name2code ['nick'] = 0`.It is easy to see that different from the list, the dictionary does not use integers as a bid.Let's take a look at the common methods of dictionary.

## 2 Dictionary Common methods

### 2.1 index

The dictionary appears in the form of key value pair, so you can use keys to index the values required by the key, such as:

`` `python
Print (name2code ['nick'])
`` `

The output is:

`` `python
0
`` `

Similar to the list, you can use the `In` operating character to view the key to the dictionary. It is worth noting that the implementation of the` in` operator in the list and the dictionary is different. The list uses the search algorithm, so the list changesFor a long time, the search time will also become longer, but the dictionary uses the algorithm of the hashtable, so no matter how much the key value is in the dictionary, the time is almost the same as the operating symbol.

`` `python
Print ('nick' in name2code)
`` `

The output is:

`` `python
True
`` `

If you want to check whether the value is in the dictionary, you can use the `values ()` method to take out the value of the dictionary, and then check it with an IN operator:

`` `python
Values = name2code.values ()
Print (0 in Values)
`` `

The output is:

`` `python
True
`` `

### 2.2 Delete element

The method of deleting elements of the dictionary is similar to the list:

-Cleway dictionary: `name2code.clear ()`, pay attention to `clear ()` method does not return the value
-An the corresponding value of the key K, and then remove the key value right: `name2code.pop (k, [default])`
-At the key value added and remove the key value.

### 2.3 cycle

You can traverse the dictionary key to use the FOR loop. Please note that because the key can be scattered, it does not follow a specific order. The following code may have different output order on your computer (Note: Python 3.6 and laterThe version retains the order of the key value, so the result is certain):

`` `python
for I in name2code:
    Print (i, name2code [i])
`` `

The output is:

`` `python
Tony 1
Kevin 2
Luis 3
Nick 0
`` `

If you want to traverse with your key and values at the same time, you can also use the `Items () method:

`` `python
for k, v in name2code.items ():
    Print (k, v)
`` `

The output is:

`` `python
Tony 1
Kevin 2
Luis 3
Nick 0
`` `

### 2.4 reverse search

For a dictionary, the operation of using the key to find the value has been introduced above. If you want to use the value to find the key, you should do the reverse search operation at this time. Note that you use a `raise statement.There is a problem with the value of the display parameter.

`` `python
defundest_lookup (d, v):
    for I in D:
        if d [i] == v:
            Return i
    Raise Valueerror ("The value you find is not in the dictionary")

Reversed_Lookup (name2code, 5)
`` `

The output is:

`` `python
---------------------------------------------------------------------------
Valueerror Traceback (MOST Recent Call Last)
<iPython-Input-33-832e824fe6b4> in <Module>
----> 1 reversed_lookup (name2code, 5)

<ipython-input-32-BE75152F6E58> in reversed_lookup (d, v)
      4 Return i
      5
----> 6 Raise Valueerror ("The value you find is not in the dictionary")

Valueerror: The value you find is not in the dictionary
`` `

### 2.5 Dictionary derivation

Starting from Python 2.7, the list derivation and generator expression have also been transplanted on the dictionary. As follows,

`` `python
code2Name = {code: name for name, code in name2code.items () if code <2}
Print (code2Name)
`` `

The output is:

`` `python
{1: 'Tony', 0: 'Nick'}
`` `

## 3 Dictionary variants

In addition to DICT, there are several different mapping types in the Collections module in the Python standard library:

-CollectionS.OnRedDict: This type will keep the order of the key when adding keys, so the iterative order of the key is always consistent.However, please note that if the data is not inserted after the orderly dictionary is defined, the original key value is still disorderly, the same as the ordinary dictionary.
-Collections.chainmap: This type can accommodate multiple different mapping objects. When the key search operation is performed, these objects will be found one by one until they find the corresponding keys.Commonly used to manage dictionaries that represent different scope and context.
-COLLECTIONS.COUNTER: As the name suggests, this is a counter. When the key is updated, the counter is updated.It is often used for counting or as a multi -collection (many elements in the collection).
-Colllections.userdict: This class is mainly used to allow users to inherit. Inheritance this class will be more convenient than inheriting DICT, mainly because the built -in types such as DICT usually ignore the user coverage, causing unexpected trouble. DetailSee [Flowing Python "Chapter 12-The advantages and disadvantages of inheritance] (https://book.douban.com/subject/27028517/).

## 4 Summary

The above knowledge points are very commonly used in daily work. The following content also covers the summary of many Python programmers' years of practical experience. Let's review it again:

-Dit's key must be scattered.It means that the dispersing value of the life cycle of this object is unchanged, and the object must implement the `__hash__` method, and support the use of the` __eq__` method to verify equal nature.
-DICT memory is huge.Because the dictionary uses the scattered list, the spread list must be sparse, resulting in low space utilization.If the amount of data is huge, it is recommended to use the meta -group or list.
-The key inquiry is very high.As long as the dictionary can be installed in memory, the key query speed does not slow down with the increase in data volume, but the cost of fast speed is a large space.
-In new keys to DICT may change the order of existing keys.The specific reasons are related to the DICT implementation method. It is recommended not to iterate and modify the DICT at the same time. It is best to divide it into two steps: first iterate to find the content that needs to be modified and record, and then change the original DICT after iteration.

When reviewing these knowledge, I also have a new understanding and gain. I hope these content will also help you!