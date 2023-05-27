# Introduction to Python argparse module

!!! info
    Author: Jeremy, published on 2021-11-22, reading time: about 7 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/A58uLo9wbMGLSdYqAJXqsw)

## 1 Introduction

As a scripting language, Python can be easily launched on the command line, but sometimes we often need to pass some parameters to the same set of programs to solve more types of tasks. For example, in the [12306 intelligent booking](http://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484848&idx=1&sn=7e5b0b4e4740c42fa629a2c98e159839&chksm=eb90f6c4dce77fd266441c22a659668af98bc34e1bea9c264a296bc89a4f5c7da3570c6cb1e8#rd) project, the script has three different running modes based on the different parameters passed in the command line, such as:

- python run.py -r: run the ticket grabbing program
- python run.py -c: filter CDN
- python run.py -t: test email and server sauce

Doesn't it look like our habit of using shell scripts? Today, I want to introduce to you the module that supports command line interaction (CLI) behind Python - argparse.

## 2 Introduction to argparse

The argparse module allows people to easily write user-friendly command-line interfaces, which can typically be seen in a project's CLI.py file.

The use of argparse mainly consists of three steps:

1. Instantiate an object
2. Use the add_argument () method to define the parameters that can be passed
3. Use the parse_args () method to pass the parameter object to the program

### 2.1 Passing Positional Parameters

Positional parameters are parameters that must be carried when the script is inaugurated on the command line. When defined in the add_argument () method, the parameter name prefix does not have "-" or "--". If a positional argument is defined, the argument is essential on the command line.

Let's take a look at a simple example:

```python
import argparse

def compute_square(d):
    '''Calculate the square'''
    return d ** 2

def create_parser():
    # Instantiate the parser object
    parser = argparse.ArgumentParser()
    # Add parameters
    parser.add_argument("d", type=int, help="return the square of the input numebr")
    # Return the parser object
    return parser

if __name__ == "__main__":
    # Create the parser object
    parser = create_parser()
    # Parse the command line arguments
    args = parser.parse_args()
    # Call the function
    print("return value: ",compute_square(args.number))
```

We set the filename to `ap.py`. When we start the file in the terminal and pass in an integer, the program will print the square of the integer:

```shell
$ python ap.py 4
return value: 16
```

Note that in the `add_argument` method, we defined the type of the incoming parameter as an integer. If the input parameter type cannot be converted to an integer, an error will be reported.

```shell
$ python ap.py four
usage: ap.py [-h] number
ap.py: error: argument number: invalid int value: 'four'
```

### 2.2 Passing Optional Parameters

Optional parameters have a prefix containing "-", "--". "-" usually comes after an abbreviation, such as "-h", and "--" generally comes after a full name, such as "--help". Optional parameters can generally be combined with the conditional logic in Python scripts, such as:

```python
import argparse


def compute_area(d, objshape="square", return_int=False):
    '''Calculate the area of ​​a square or circle'''
    if objshape == "square":
        result = d**2
    elif objshape == "circle":
        result = 3.14*(d/2)**2
    else:
        return "Error: invalid shape"

    return f"Area: {int(result) if return_int else result}"


def create_parser():
    # Instantiate the parser object
    parser = argparse.ArgumentParser()
    # Add parameters
    parser.add_argument("d",
                        type=int,
                        help="return the square of the input numebr")

    parser.add_argument("-s", "--shape",
                        type=str,
                        dest="objshape",  # The name of the parameter object in the Namespace returned by parse_args (), if not added, defaults to "shape"
                        choices=['square','circle'],
                        help="return the area of the shape")

    parser.add_argument("-i", "--int",
                        action="store_true",
                        dest="return_int",
                        help="return the area as an integer")
    # Return the parser object
    return parser


if __name__ == "__main__":
    # Create the parser object
    parser = create_parser()
    # Parse the command line arguments
    args = parser.parse_args()
    # Get the parameter dictionary
    print('args dict:', vars(args))
    # Call the function
    print(compute_area(**vars(args)))
```

Note that we used some commonly used parameters in the add_argument () method to achieve more standardized and fluent parameter passing:

- dest: specify the parameter object name in the Namespace passed in, if not added, defaults to the name of the parameter in add_argument ()
- choices: limits the range of optional input for the parameter
- action: handles parameters, here the parameter is set to boolean.

We try to calculate the area of ​​a circle and take it as an integer:

```shell
$ python ap.py 4 -s circle -i
args dict: {'d': 4, 'objshape': 'circle', 'return_int': True}
Area: 12
```

In this way, we can elegantly control important parameters in the terminal without changing the code in the script, improving the effectiveness of the code.

## 3. Summary

In addition to the commonly used methods, the argparse module also includes methods such as:

- add_argument_group (): add parameter groups
- add_subparsers (): add subcommands
- add_mutually_exclusive_group (): create an exclusive group

And other methods that implement relatively complex parameter passing logic. Understanding and appropriately using these methods can save a lot of time in setting rules.

Frequent code modifications are inevitably prone to accidents that crash the code. If you don't want to try on the dangerous edge anymore and want to retain a certain degree of flexibility, why not try argparse!