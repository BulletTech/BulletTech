---
template: overrides/blogs.html
tags:
  -Python
---

# Understand Python closure

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published at 2021-09-21, read time: about 6 minutes, WeChat public account article link: [: fontaWesome-Solid-Link:] (https://mp.weixin.qqqpom/s ?__biz=mzi4mjk3nzgxoq==&mid=224748557IDX=1&Sn=bd621757e391c51CB5F8F7F9DCE777EF2A 8C67BC0D3637E9D90708FFD061CE4773916FA3C58D137E4B859ADF1C40 & Token = 1570026209 & Lang = zh_cn#rd))

## 1 Introduction

In the daily work of Python, you may have encountered this code similar to this:

`` `Python
DEF MAKE_COUNTTE ():
    # Outer closure function
    Count = 0
    def counter ():
      # Nested function

        nonLocal Count
        count += 1
        Return Count

    Return counter
`` `

There is a function in a function, and the return value of the outer function is the function of the inner layer. Why do you define the function like this?What are the benefits of this, we will unveil this mysterious veil -closure.

## 2 The main points of closing

The closure refers to the function that extends the scope of action. It will quote a non -global variable that is not in the definition of the function (such as the count in the above example)., Make the inner nested function that can modify the unable variables outside the domain.

When calling make_counter, return a counter function object. Each time you call the counter, it will update the count. The example is as follows:

`` `Python
# Run closure function
counter = Make_counter ()
Print (counter ()))
Print (counter ()))
`` `

The output is:

`` `python
1
2
`` `

In this example, one thing that needs to be expanded is the storage location of the historical value of Count. Count is a local variable of the Make_Counter function. When initializationThe scope of action should no longer exist.

In the counter function, Countnt is a free variable, and the Counter function implements the binding of variables.You can view the name of the saved local variables and free variables in the __code__ attribute (indicating the function definition body after compiled) in Python, as shown below:

`` `Python
# View free variable
counter .__ code __. Co_freevars
`` `

The output is:
`` `
('count',)
`` `

The COUNT is binding in the __closure__ attribute of the returned counter function, where the elements of __clOSURE__ correspond to a name in the `Counter .__ CODE __. Co_freevars'.These elements are Cell objects, which can access the storage values through the cell_contents property. The example is as follows:

`` `python
counter .__ closure __ [0] .Cell_contents
`` `

The output is:

`` `
2
`` `

The closure can solve the problem of lightweight very concisely and intuitively. If the above functions are implemented in category `, it will grow:

`` `Python
# Define a counter with a class, start counting from 0
class counter:
    DEF __init __ (Self):
        Self.Count = 0

    DEF __call __ (Self):
        Self.Count += 1
        Return Self.Count

counter = counter ()
Print (counter ()))
Print (counter ()))
`` `

The output is:

`` `Python
1
2
`` `

## 3 Summary

Closure is a function that retains the binding of free variables when defining a function. Therefore, even if the function of the function is returned, the scope does not exist, and those binding can still be used.Closures can easily achieve some simple classes. At the same time, there are many Python magics that can be achieved, such as decorators, to be decomposed next!

I hope this sharing will help you, welcome to discuss in the comment area!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>