---
template: overrides/blogs.html
tags:
  - python
---

# SQL Parsing Tool: sqlparse

!!! info
    Author: Jeremy, Posted on October 20, 2021, Reading time: about 10 minutes, WeChat Official Account Article Link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484692&idx=1&sn=67ccf74a8d6b099ce03eaa43166849d5&chksm=eb90f660dce77f7666727e4889a09b58917cdeae57cbdb353ea5c902b0a053bf30c904cc972b&token=95681447&lang=zh_CN#rd)

## 1. Introduction

A data analysis team often accumulates a large amount of SQL-based code for daily reports, model data extraction, business decisions, etc. Sometimes, as the company develops and technology changes, the company's data warehouse may be migrated or restructured, and SQL code containing these tables needs to be rewritten accordingly. Manually rewriting segments of business code, especially modifications to fields or table names, is often repetitive and prone to omissions.

Laziness is the first productivity of programmers. Since it is repetitive work, is there any tool that can help us automate this process?

## 2. Python Open Source Tool: sqlparse

### 2.1 Introduction

To rewrite SQL code, a key step is to parse the SQL. [sqlparse](https://sqlparse.readthedocs.io/en/latest/intro/) is an unverified parser based on Python. It provides a simple `parse()` function to return a parsing structure similar to a syntax tree. Let's use the `_pprint_tree()` function to print the parsed SQL statement:

``` python
import sqlparse
query = 'Select a, col_2 as b from Table_A;'
sqlparse.parse(query)[0]._pprint_tree()
```

The output is:

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

We can see that sqlparse can accurately identify the keywords in the query statement, and the fields and table names are identified as Identifier types. Combining the keywords in the preceding and following tokens can further determine whether they are fields or table names. Before that, you need to understand the various methods contained in each type.

### 2.2 Type definition

The basic type of sqlparse is Token, which has two commonly used attributes: ttype and value. In addition, like the nodes of a tree structure, it can be associated with the previous token by the parent attribute. Its commonly used methods mainly access and judge the attributes of the token:

class sqlparse.sql.Token(ttype, value):

* flatten(): Resolve subgroups.

* has_ancestor(other): Returns True if other is in this tokens ancestry.

* is_child_of(other): Returns True if this token is a direct child of other.

* match(ttype, values, regex=False): checks whether the token matches the given arguments.

* within(group_cls): Returns True if this token is within group_cls.

TokenList is an inheritance of the Token type and is defined as a collection of tokens. Access is done by token.tokens. For example, 'col_2 as b' in the example was judged as IdentifierTypeTokenList. In addition to inheriting and partially rewriting the methods of the Token type, it also defines methods for obtaining the position, name, and matching search of child tokens:

class sqlparse.sql.TokenList(tokens=None):

* flatten(): Generator yielding ungrouped tokens. This method is recursively called for all child tokens. (overrides the flatten method)

* get_alias(): Returns the alias for this identifier or None.

* get_name(): Returns the name of this identifier.

* group_tokens(grp_cls, start, end, include_end=True, extend=False): Replace tokens by an instance of grp_cls.

* has_alias(): Returns True if an alias is present.

* token_first(skip_ws=True, skip_cm=False): Returns the first child token.

* token_index(token, start=0): Return list index of token.

* token_prev(idx, skip_ws=True, skip_cm=False): Returns the previous token relative to idx.*

### 2.3 Lexical analysis

For DDL(Data Definition Language) / DML(Data Manipulation Language) and other keywords in SQL, sqlparse mainly recognizes them through regular expressions. All regular expressions and token type correspondences are stored in the `SQL_REGEX` variable in [keywords.py](https://github.com/andialbrecht/sqlparse/blob/master/sqlparse/keywords.py). You can modify the regular expression to adapt to different data warehouse syntax and functions if necessary.

## 3. Case: Extracting Table Name from Query

The sqlparse author provides an example of extracting table names in the source code, mainly by extracting the subsequent `tokenList` when encountering keywords from or join during the parsing process.

``` python

ALL_JOIN_TYPE = ('LEFT JOIN', 'RIGHT JOIN', 'INNER JOIN', 'FULL JOIN', 'LEFT OUTER JOIN', 'FULL OUTER JOIN')


def is_subselect(parsed):
    """
    Whether sub-query
    :param parsed: T.Token
    """
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    """
    Extract module after from
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
    Extract module after join
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
    Extract table name from sql (select statement)
    """
    from_stream = extract_from_part(sqlparse.parse(sql)[0])
    join_stream = extract_join_part(sqlparse.parse(sql)[0])
    return list(extract_table_identifiers(from_stream)) + list(extract_table_identifiers(join_stream))
```

## 4. Conclusion

sqlparse is a relatively powerful SQL parsing tool based on the Python language. The open source library has received 2.6k stars and 522 forks on GitHub. Its code is concise and efficient, and the structure is clear. Interested students should read it carefully.