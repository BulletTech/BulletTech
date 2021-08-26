---
template: overrides/blogs.html
---

# 利用递归思想处理半结构化数据

!!! info
    作者：Jermey，发布于2021-08-22，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]

## 1. 背景

在日常数据分析的工作中，我们收集到的原始数据有时并不是整齐的表格形式，例如在爬取网页或者爬取API里的数据时，结果往往是以XML或者JSON（类似Python中的字典）格式返回，并且层层嵌套。就像如下这样的JSON格式：

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

这种嵌套形式的数据如果很复杂，确实不适合人类阅读，如果要对数据进行进一步地清洗或者分析，我们要做的第一步是把嵌套"打开"，转化成类似如下形式的表格：

|       name | population |   state | shortname | info.governor |
|-----------:|-----------:|--------:|----------:|--------------:|
|       Dade |      12345 | Florida |        FL |    Rick Scott |
|    Broward |      40000 | Florida |        FL |    Rick Scott |
| Palm Beach |      60000 | Florida |        FL |    Rick Scott |
|     Summit |       1234 |    Ohio |        OH |   John Kasich |
|   Cuyahoga |       1337 |    Ohio |        OH |   John Kasich |

我们希望表格内每一条记录是county-level，和可是怎么转化呢？试试万能的pandas吧：

```Python
# 尝试直接转化为DataFrame
df = pd.DataFrame(data)
print(df)
```

输出为：

| name   | shortname | info    | counties  | name" |
|--------|-----------|---------|-----------|-------|
| Florida | FL | {'governor': 'Rick Scott'}  | [{'name': 'Dade', 'population': 12345}, {'name... | NaN   |
| NaN     | OH | {'governor': 'John Kasich'} | [{'name': 'Summit', 'population': 1234}, {'nam... | Ohio  |

发现pandas只解析了第一层state-level的记录，而county-level的数据还是以嵌套的形式展现。经过亿点点查找，发现pandas自带一个叫做json_normalize的函数可以实现我们的需求:

```Python
# 使用json_normalize():
pd.json_normalize(
    data, 
    record_path = 'counties',  # 定义数据粒度
    meta = ['state', 'shortname',['info', 'governor']] # 定义存入结果表的列名
    )
```

输出为：

|       name | population |   state | shortname | info.governor |
|-----------:|-----------:|--------:|----------:|--------------:|
|       Dade |      12345 | Florida |        FL |    Rick Scott |
|    Broward |      40000 | Florida |        FL |    Rick Scott |
| Palm Beach |      60000 | Florida |        FL |    Rick Scott |
|     Summit |       1234 |    Ohio |        OH |   John Kasich |
|   Cuyahoga |       1337 |    Ohio |        OH |   John Kasich |

这和我们预期的结果一样。但是这一过程是如何实现的呢？其实，这是递归思想的在实际应用的范例之一。

## 2. 什么是递归？

想要知道什么是递归？先了解什么是递归。

没错，递归的本质就是"复读"，在计算机编程中，递归就是通过函数调用自身，把问题转化成解决一个过程相似，但是规模较小的问题，直到到达边界条件即最小化的问题。一个完整的递归函数一般具有以下三要素：

- 终止条件
- 函数运行状态，每次运行都逐步逼近终止条件
- 调用函数自身

以通过递归算法求解斐波那契数列为例:

``` Python
def Fibonacci(n):
    def _recurse(n):
        if n == 0: # 边界条件
            return 0
        elif n == 1: # 边界条件
            return 1
        else:
            return _recurse(n-1) + _recurse(n-2) # 调用自身，缩小问题规模
    return _recurse(n)
```

想要求第n个斐波那契数f(n)，我们只需要计算f(n-1)和f(n-2)的值，这一步相当于把问题规模缩小。这个问题可以递推到计算f(2)=f(1)+f(0)。又因为f(1)和f(0)的值是我们已知的边界条件，我们便可以推导出f(2)值，由此逐步得出f(n)。

类似地，在解析嵌套的JSON数据时，我们可以设计一个函数f()解析当前层的字典，当字典中的某个值(value)为的type为字典或者字典列表时，调用同样的函数f(n)，直到满足value中不含字典这一边界条件。同时，我们需要记录解析遍历的键值对，字典的键即为输出表格中的字段，字典的值为表格中的record。

我们来看下pandas v1.2.0 源码中_json_normalize()的核心代码：

``` Python

def _json_normalize(
    data: Union[Dict, List[Dict]],
    record_path: Optional[Union[str, List]] = None,
    meta: Optional[Union[str, List[Union[str, List[str]]]]] = None,
    meta_prefix: Optional[str] = None,
    record_prefix: Optional[str] = None,
    errors: str = "raise",
    sep: str = ".",
    max_level: Optional[int] = None,
) 
    # 定义一些辅助函数
    def _pull_field(js: Dict[str, Any], spec: Union[List, str])：
        """Internal function to pull field"""
        # 省略具体实现代码
        ...
        return result
        
    def _pull_records(js: Dict[str, Any], spec: Union[List, str]) -> List:
        """
        Internal function to pull field for records, and similar to
        _pull_field, but require to return list.
        """
        # 省略具体实现代码
        ...
        return result  
       
    # 省略一些对输入参数的处理和判定的代码   
    
    # 定义一些函数内变量
    _meta = [m if isinstance(m, list) else [m] for m in meta] # 需要展现在结果里的字段
    records: List = []
    lengths = []
    # meta_val用于存储fields对应的数值
    meta_vals: DefaultDict = defaultdict(list)
    # 在深层字典里的字段，用上一层的字段名+分隔符+这一层的字段名代替，防止字段重复，如例子中的 ['info', 'governor'] 处理成 info.governor
    meta_keys = [sep.join(val) for val in _meta]
    
    # 核心代码：
    # Disastrously inefficient for now
    def _recursive_extract(data, path, seen_meta, level=0):
        if isinstance(data, dict):
            data = [data]

        if len(path) > 1: #这里对于多个record_path的情况进行递归
            for obj in data:
                for val, key in zip(_meta, meta_keys):
                    if level + 1 == len(val):
                        seen_meta[key] = _pull_field(obj, val[-1])

                _recursive_extract(obj[path[0]], path[1:], seen_meta, level=level + 1)

        else:
            # 遍历当前层的data
            for obj in data:
                # 取出当前层所有的records (list of dict)
                recs = _pull_records(obj, path[0])
                # pandas 中的另一个内置函数，如果records里面有dict,将dict打开。
                # 例如如果有一条记录是{'a':{'b':1}} 则会变成 {'a.b':1}
                recs = [
                    nested_to_record(r, sep=sep, max_level=max_level)
                    if isinstance(r, dict)
                    else r
                    for r in recs
                ]

                # For repeating the metadata later
                lengths.append(len(recs)) # 记录当前层级records的数量
                for val, key in zip(_meta, meta_keys):
                    if level + 1 > len(val): # 如果字段在下一层dict，如val为['info', 'governor']，则取seen_meta['info.governer']
                        meta_val = seen_meta[key]
                    else: # 取出当前层字段对应的value
                        try:
                            meta_val = _pull_field(obj, val[level:])
                        except KeyError as e:
                            if errors == "ignore":
                                meta_val = np.nan
                            else:
                                raise KeyError(
                                    "Try running with errors='ignore' as key "
                                    f"{e} is not always present"
                                ) from e
                    meta_vals[key].append(meta_val)
                records.extend(recs) 

    _recursive_extract(data, record_path, {}, level=0)
    
    # 省略一些对result的格式后处理代码
    
    return result
```

可以看出源码还是稍微有些难以理解的，此外代码作者也吐槽目前的执行效率很低，但这个函数好在可以通过定义record_path控制解析的深度，防止将过深的半结构化数据完全展开，产生过多的记录。

## 3. 总结

虽然数据分析师的日常工作中往往不需要直接接触算法，但掌握一些算法思想往往可以帮助我们更好地理解手边的工具。必要时也可以自己编写代码提高效率。除了刷算法题之外，读读优秀开源项目地源码也是很好的提升方式。如果实在没有时间，那就常来我们的公众号上看看吧！
