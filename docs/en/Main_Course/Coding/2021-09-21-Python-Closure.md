---
template: overrides/blogs.html
tags:
  - python
---

# 理解Python闭包

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-09-21，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484557&idx=1&sn=bd624bdb21757e391d01c5ced51cb5f8&chksm=eb90f7f9dce77eef2a8c67bc0d3637e9d90708ffd061ce4773916fa3c58d137e4b859adf1c40&token=1570026209&lang=zh_CN#rd)

## 1 Introduction


In the daily work of Python, you may have encountered this code similar to this:


```Python
def make_counter():
# Outer closure function
count = 0
def counter():
# Nested function


nonlocal count
count += 1
return count


return counter
```


There is a function in a function, and the return value of the outer function is the function of the inner layer. Why do you define the function like this?What are the benefits of this, we will unveil this mysterious veil -closure.


## 2 The main points of closing


The closure refers to the function that extends the scope of action. It will quote a non -global variable that is not in the definition of the function (such as the count in the above example)., Make the inner nested function that can modify the unable variables outside the domain.


When calling make_counter, return a counter function object. Each time you call the counter, it will update the count. The example is as follows:


```Python
# Run closure function
counter = make_counter()
print(counter())
print(counter())
```


The output is:


```python
1
2
```


In this example, one thing that needs to be expanded is the storage location of the historical value of Count. Count is a local variable of the Make_Counter function. When initializationThe scope of action should no longer exist.


In the counter function, Countnt is a free variable, and the Counter function implements the binding of variables.You can view the name of the saved local variables and free variables in the __code__ attribute (indicating the function definition body after compiled) in Python, as shown below:


```Python
# View free variable
counter.__code__.co_freevars
```


The output is:
```
('count',)
```


The COUNT is binding in the __closure__ attribute of the returned counter function, where the elements of __clOSURE__ correspond to a name in the `Counter .__ CODE __. Co_freevars'.These elements are Cell objects, which can access the storage values through the cell_contents property. The example is as follows:


```python
counter.__closure__[0].cell_contents
```


The output is:


```
2
```


The closure can solve the problem of lightweight very concisely and intuitively. If the above functions are implemented in category `, it will grow:


```Python
# Define a counter with a class, start counting from 0
class Counter:
def __init__(self):
self.count = 0


def __call__(self):
self.count += 1
return self.count


counter = Counter()
print(counter())
print(counter())
```


The output is:


```Python
1
2
```


## 3 Summary


Closure is a function that retains the binding of free variables when defining a function. Therefore, even if the function of the function is returned, the scope does not exist, and those binding can still be used.Closures can easily achieve some simple classes. At the same time, there are many Python magics that can be achieved, such as decorators, to be decomposed next!


I hope this sharing will help you, welcome to discuss in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>