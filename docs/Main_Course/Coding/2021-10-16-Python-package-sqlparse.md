---
template: overrides/blogs.html
---

# SnowFlake权限概览

!!! info
    作者：Jeremy，发布于2021-10-20，阅读时间：约10分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 引言

一个数据分析团队往往会积累大量基于SQL的代码，用于日常的报表，模型数据提取，业务决策等等。有时随着公司的发展和技术更替，公司的数据仓库会进行迁移或重构，当表结构，字段名或者表名发生变化时，包含这些表的SQL代码就需要相应地进行改写。人为改写一段段业务代码，尤其是对字段或者表名的修改，往往比较重复而且容易遗漏。

懒惰是程序员的第一生产力，既然是重复的工作，那么有没有什么工具可以帮助我们自动化这一过程呢？


## 2 Python开源工具——sqlparse 

### 2.1 介绍

想要改写SQL代码，关键的一步是对SQL进行解析。[sqlparse](https://sqlparse.readthedocs.io/en/latest/intro/)是基于Python的一个无验证解析器，他提供了一个简单的parse()函数来f返回类似语法树的解析结构。我们用_pprint_tree()函数打印下解析后的SQL语句:

``` Python
import sqlparse 
query = 'Select a, col_2 as b from Table_A;'
sqlparse.parse(query)[0]._pprint_tree()
```

输出为：

```
|- 0 DML 'Select'
|- 1 Whitespace ' '
|- 2 IdentifierList 'col_1,...'
|  |- 0 Identifier 'col_1'
|  |  `- 0 Name 'col_1'
|  |- 1 Punctuation ','
|  |- 2 Whitespace ' '
|  `- 3 Identifier 'col_2 ...'
|     |- 0 Name 'col_2'
|     |- 1 Whitespace ' '
|     |- 2 Keyword 'as'
|     |- 3 Whitespace ' '
|     `- 4 Identifier 'b'
|        `- 0 Name 'b'
|- 3 Whitespace ' '
|- 4 Keyword 'from'
|- 5 Whitespace ' '
|- 6 Identifier 'Table_A'
|  `- 0 Name 'Table_A'
`- 7 Punctuation ';'
```

可以看到sqlparse可以准确的识别出查询语句中的关键词，并且字段，表名被识别成了Identifier类型。结合前后token中的关键词就可以进一步判断出具体是字段还是表名。在此之前还需要了解各种类型包含的各种方法。

### 2.2 类型定义

sqlparse的基础类型是Token,其中ttype和value两个常用属性。此外类似树结构的节点，他可以通过parent属性关联上一层token。它的常用方法主要是对该token属性的访问和判断:

class sqlparse.sql.Token(ttype, value):

* flatten(): Resolve subgroups.

* has_ancestor(other): Returns True if other is in this tokens ancestry.

* is_child_of(other): Returns True if this token is a direct child of other.

* match(ttype, values, regex=False): checks whether the token matches the given arguments.

* within(group_cls): Returns True if this token is within group_cls.

TokenList是Token类型的继承，定义为一群token的集合。通过token.tokens属性来访问。如例子中的'col_2 as b'就被判定为了Identifier类型的TokenLis他。除了继承和部分覆写了Token类型的方法以外，还定义了获取子token位置，名称，匹配搜索子token等方法:

class sqlparse.sql.TokenList(tokens=None):

* flatten(): Generator yielding ungrouped tokens. This method is recursively called for all child tokens. (覆写了flatten方法)

* get_alias(): Returns the alias for this identifier or None.

* get_name(): Returns the name of this identifier.

* group_tokens(grp_cls, start, end, include_end=True, extend=False): Replace tokens by an instance of grp_cls.

* has_alias(): Returns True if an alias is present.

* token_first(skip_ws=True, skip_cm=False): Returns the first child token.

* token_index(token, start=0): Return list index of token.

* token_prev(idx, skip_ws=True, skip_cm=False): Returns the previous token relative to idx.*


### 2.3 词法解析

对于SQL中的DDL/DML等关键词，sqlparse主要通过正则表达式识别，所有的正则表达与token类型的对应关系储存在[keywords.py](https://github.com/andialbrecht/sqlparse/blob/master/sqlparse/keywords.py)里的SQL_REGEX变量中，必要时可以修改正则表达来适应不同的数据仓库语法和函数。

## 3 案例:从查询中提取表名

sqlparse作者在源码中提供了提取表名的范例，主要思路是在解析过程中遇到关键词from或者join后，提取其后的tokenList。

``` python 

ALL_JOIN_TYPE = ('LEFT JOIN', 'RIGHT JOIN', 'INNER JOIN', 'FULL JOIN', 'LEFT OUTER JOIN', 'FULL OUTER JOIN')


def is_subselect(parsed):
    """
    是否子查询
    :param parsed:
    :return:
    """
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    """
    提取from之后模块
    """
    from_seen = False
    for item in parsed.tokens:
        if from_seen:
            if is_subselect(item):
                for x in extract_from_part(item):
                    yield x
            elif item.ttype is Keyword:
                from_seen = False
                continue
            else:
                yield item
        elif item.ttype is Keyword and item.value.upper() == 'FROM':
            from_seen = True


def extract_join_part(parsed):
    """
    提交join之后模块
    """
    flag = False
    for item in parsed.tokens:
        if flag:
            if item.ttype is Keyword:
                flag = False
                continue
            else:
                yield item
        if item.ttype is Keyword and item.value.upper() in ALL_JOIN_TYPE:
            flag = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                yield identifier.get_name()
        elif isinstance(item, Identifier):
            yield item.get_name()
        elif item.ttype is Keyword:
            yield item.value


def extract_tables(sql):
    """
    提取sql中的表名（select语句）
    """
    from_stream = extract_from_part(sqlparse.parse(sql)[0])
    join_stream = extract_join_part(sqlparse.parse(sql)[0])
    return list(extract_table_identifiers(from_stream)) + list(extract_table_identifiers(join_stream))
```

## 4 总结

sqlparse是一个比较强大的基于python语言的SQL解析工具，开源库在GitHub上获得了2.6k个星星和522次Fork。其代码简洁高效，结构清晰，值得感兴趣的同学细细阅读。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>