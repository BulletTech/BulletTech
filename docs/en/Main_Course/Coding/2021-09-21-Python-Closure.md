---
template: overrides/blogs.html
tags:
  - python
---

# Understanding Python Closures

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), published on 2021-09-21, Reading time: about 6 minutes, WeChat Official Account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484557&idx=1&sn=bd624bdb21757e391d01c5ced51cb5f8&chksm=eb90f7f9dce77eef2a8c67bc0d3637e9d90708ffd061ce4773916fa3c58d137e4b859adf1c40&token=1570026209&lang=zh_CN#rd)

## 1 Introduction

When working with Python in daily work, you may have encountered code like this:

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

Why define functions like this - with one function inside another, and the outer function returning the inner function as its output? What are the benefits of this approach? In this article, we will uncover the mysterious veil of closures.

## 2 Key points of closures

A closure is a function that extends the scope of a function, referring to a non-global variable (such as count in the example above) that is not defined in the function. By adding nonlocal, the variable is marked as a free variable (nonlocal keyword was added in Python 3), allowing the nested function to modify the immutable variable outside the scope.

When we call make_counter, it returns a counter function object. Each time we call the counter, it updates count, as shown below:

```Python
# Run the closure function
counter = make_counter()
print(counter())
print(counter())
```

Output:

```python
1
2
```

In this example, one thing that needs to be expanded is the storage location of the historical value of count. Count is a local variable in the make_counter function, and its initial value is 0. However, when counter is called, the make_counter function has already been returned, and the local scope should no longer exist.

In the counter function, count is a free variable, and the counter function implements the binding of this variable. We can check the names of stored local variables and free variables using the __code__ attribute (which represents the compiled function definition body) in Python. For example:

```Python
# View free variables
counter.__code__.co_freevars
```

Output:

```
('count',)
```

The binding of count is in the __closure__ attribute of the returned counter function, where each element of __closure__ corresponds to a name in `counter.__code__.co_freevars`. These elements are cell objects, and their stored values can be accessed through the cell_contents attribute, as shown below:

```python
counter.__closure__[0].cell_contents
```

Output:

```
2
```

Closures can solve lightweight problems very concisely and intuitively. If we were to use a `class` to implement the functionality above, it would look like this:

```Python
# Define a counter using a class, starting from 0
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

Output:

```Python
1
2
```

## 3 Summary

A closure is a function that retains the binding of free variables that were present when the function was defined, so even if the scope no longer exists after the function is returned, the bindings can still be used. Closures can easily implement simple class functionality, and there are many Python "magic" functions that can be implemented based on this, such as decorators, which we will explore next time!

I hope this article has been helpful to you, and feel free to discuss in the comments!

