---
template: overrides/blogs.html
tags:
  - analytics
---

# Using Recursive Thinking to Process Semi-Structured Data

!!! info
    Author: Jermey, Posted on August 22, 2021, Reading time: about 6 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/VGutEZWDWwNswAKoUAVsRg)

## 1 Background

In daily data analysis work, the raw data we collect is sometimes not in neat tabular form. For example, when fetching data from web pages or APIs, the results are often returned in XML or JSON (similar to Python dictionaries) format and are nested. Just like this JSON format:

```
[{
    'state': 'Florida',
    'shortname': 'FL',
    'info': {
        'governor': 'Rick Scott'
    },
    'counties': [
        {'name': 'Dade', 'population': 12345},
        {'name': 'Broward', 'population': 40000},
        {'name': 'Palm Beach', 'population': 60000}
    ]},
    {
    'state': 'Ohio',
    'shortname': 'OH',
    'info': {
        'governor': 'John Kasich'
    },
    'counties': [
        {'name': 'Summit', 'population': 1234},
        {'name': 'Cuyahoga', 'population': 1337}]
    }]
```

If this nested data is very complex, it really is not suitable for humans to read. If we want to further clean or analyze the data, the first step we need to do is to "open" the nested data and convert it to a table format like the following:

|       name | population |   state | shortname | info.governor |
|-----------:|-----------:|--------:|----------:|--------------:|
|       Dade |      12345 | Florida |        FL |    Rick Scott |
|    Broward |      40000 | Florida |        FL |    Rick Scott |
| Palm Beach |      60000 | Florida |        FL |    Rick Scott |
|     Summit |       1234 |    Ohio |        OH |   John Kasich |
|   Cuyahoga |       1337 |    Ohio |        OH |   John Kasich |

We hope that each record in the table is county-level. But how can we convert it? Let's try pandas:

```Python
# Try to convert directly to DataFrame
df = pd.DataFrame(data)
print(df)
```

The output is:

| name   | shortname | info    | counties  | name" |
|--------|-----------|---------|-----------|-------|
| Florida | FL | {'governor': 'Rick Scott'}  | [{'name': 'Dade', 'population': 12345}, {'name... | NaN   |
| NaN     | OH | {'governor': 'John Kasich'} | [{'name': 'Summit', 'population': 1234}, {'nam... | Ohio  |

It is found that pandas only parses the first level state-level records, and the data at the county-level is still shown in nested form. After a little searching, it was discovered that pandas comes with a function called json_normalize which can achieve our needs:

```Python
# Use json_normalize():
pd.json_normalize(
    data,
    record_path = 'counties',  # Define the data granularity
    meta = ['state', 'shortname',['info', 'governor']] # Define the column names stored in the result table
    )
```

The output is:

|       name | population |   state | shortname | info.governor |
|-----------:|-----------:|--------:|----------:|--------------:|
|       Dade |      12345 | Florida |        FL |    Rick Scott |
|    Broward |      40000 | Florida |        FL |    Rick Scott |
| Palm Beach |      60000 | Florida |        FL |    Rick Scott |
|     Summit |       1234 |    Ohio |        OH |   John Kasich |
|   Cuyahoga |       1337 |    Ohio |        OH |   John Kasich |

This is the same as our expected result. But how was this process implemented? In fact, this is one of the examples of the application of recursive thinking.

## 2 What is Recursion?

Want to know what recursion is? First, understand what recursion is.

Yes, the essence of recursion is "echoing". In computer programming, recursion is through calling the function itself to transform the problem into solving a similar but smaller problem, until the boundary condition, which is the smallest problem size, is reached. A complete recursive function generally has the following three elements:

- Termination condition
- Function running state, and each run is gradually approaching the termination condition
- Calling the function itself

Taking the Fibonacci sequence as an example of using recursive algorithm:

``` Python
def Fibonacci(n):
    def _recurse(n):
        if n == 0: # Boundary condition
            return 0
        elif n == 1: # Boundary condition
            return 1
        else:
            return _recurse(n-1) + _recurse(n-2) # Call itself to reduce the problem scale
    return _recurse(n)
```

To find the nth Fibonacci number f(n), we only need to calculate the values of f(n-1) and f(n-2), which is equivalent to reducing the problem scale. This problem can be traced back to calculating f(2) = f(1) + f(0). And because the values of f(1) and f(0) are our known boundary conditions, we can derive the value of f(2), gradually reaching f(n).

Similarly, when parsing nested JSON data, we can design a function f() to parse the dictionary at the current level. When the type of a value (value) in the dictionary is a dictionary or a dictionary list, the same function f(n) is called, until the value contains no dictionary, which is the