---
template: overrides/blogs.html
---

# Python argparse 模块介绍

!!! info
作者：Jeremy，发布于 2021-11-22，阅读时间：约 7 分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 前言

Python 作为脚本语言，可以简单地在命令行中进行启动，但有的时候我们往往需要传入一些参数让同一套程序解决更多类型的任务。例如在 [12306 智能订票](http://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484848&idx=1&sn=7e5b0b4e4740c42fa629a2c98e159839&chksm=eb90f6c4dce77fd266441c22a659668af98bc34e1bea9c264a296bc89a4f5c7da3570c6cb1e8#rd)项目中，脚本根据命令行中传入参数的不同，有三种不同的运行模式，如:

- python run.py -r: 运行抢票程序
- python run.py -c: 过滤 cdn
- python run.py -t: 测试邮箱和 server 酱

是不是像极了我们平时使用 shell 脚本的习惯？今天就想向大家介绍一下 Python 背后支持命令行交互(command line interface,CLI)的模块——argparse。

## 2 argparse 介绍

argparse 模块可以让人轻松编写用户友好的命令行接口，通常在一个项目的 CLI.py 文件中可以看到他的影子。

argparse 的使用主要分为三步：

1. 实例化对象
2. 使用 add_argument() 方法定义可以传递的参数
3. 使用 parse_args() 方法将参数对象传入程序

### 2.1 传递位置参数

位置参数是在命令行中唤起脚本时，必须携带的参数。在 add_argument()方法中定义时，参数名称前缀没有"-"或"--"。如果定义了位置参数，该参数在命令行中必不可少。

我们看一个简单的实例:

```python
import argparse

def compute_square(d):
    '''计算平方'''
    return d ** 2

def create_parser():
    # 实例化parser对象
    parser = argparse.ArgumentParser()
    # 添加参数
    parser.add_argument("d", type=int, help="return the square of the input numebr")
    # 返回parser对象
    return parser

if __name__ == "__main__":
    # 创建解析器对象
    parser = create_parser()
    # 解析命令行参数
    args = parser.parse_args()
    # 调用函数
    print("return value: ",compute_square(args.number))
```

我们设置改文件名为 `ap.py`。当我们在终端中启动该文件并传入一个整数时，程序将会打印整数的平方:

```shell
$ python ap.py 4
return value: 16
```

注意在 `add_argument`方法中我们定义了传入参数的类型为整数，如果传入参数类型不能转换成整数则会报错。

```shell
$ python ap.py four
usage: ap.py [-h] number
ap.py: error: argument number: invalid int value: 'four'
```

### 2.2 传递可选参数

可选参数的名称前缀含"-","--"。"-"后一般接简称，如"-h"，"--"后一般接全称，如"--help"。可选参数一般可以与 Python 脚本中的条件逻辑结合，如:

```python
import argparse


def compute_area(d, objshape="square", return_int=False):
    '''计算正方形或圆形的面积'''
    if objshape == "square":
        result = d**2
    elif objshape == "circle":
        result = 3.14*(d/2)**2
    else:
        return "Error: invalid shape"

    return f"Area: {int(result) if return_int else result}"


def create_parser():
    # 实例化parser对象
    parser = argparse.ArgumentParser()
    # 添加参数
    parser.add_argument("d",
                        type=int,
                        help="return the square of the input numebr")

    parser.add_argument("-s", "--shape",
                        type=str,
                        dest="objshape",  # parse_args()返回的Namespace中参数对象的名字，如不添加则默认为"shape"
                        choices=['square','circle'],
                        help="return the area of the shape")

    parser.add_argument("-i", "--int",
                        action="store_true",
                        dest="return_int",
                        help="return the area as an integer")
    # 返回parser对象
    return parser


if __name__ == "__main__":
    # 创建解析器对象
    parser = create_parser()
    # 解析命令行参数
    args = parser.parse_args()
    # 获取参数字典
    print('args dict:', vars(args))
    # 调用函数
    print(compute_area(**vars(args)))
```

注意这里分别用了 add_argument()方法中一些常用参数来实现更规范和流畅的参数传递:

- dest: 指定传入的命名空间(Namespace)的参数对象名称
- choices: 限定参数的可选输入范围
- action: 处理参数，这里将参数设定为 boolean。

我们尝试计算一个圆的面积并取整：

```shell
$ python ap.py 4 -s circle -i
args dict: {'d': 4, 'objshape': 'circle', 'return_int': True}
Area: 12
```

这样一来，我们不需要改动脚本内的代码，就可以简洁地在终端内实现重要参数的控制，提高代码的有效性。

## 3. 小结

除了常用的方法以外，argparse 模块还包含

- add_argument_group(): 添加参数组
- add_subparsers(): 添加子命令
- add_mutually_exclusive_group(): 创建互斥组

等等实现相对复杂的参数传递逻辑的方法，了解并适时地运用这些方法可以节省不少设定规则的时间。

频繁的修改代码难免会有失手让代码崩溃的时候，如果不想再危险的边缘试探又想要保留一定的灵活性的话，不妨试试 argparse 吧！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
