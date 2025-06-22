---
template: overrides/blogs.html
tags:
  - knowledge graph
---

# Introduction to Graph Databases

!!! info
    Author: Dragond41, Published on December 13, 2021, Read time: about 2 minutes, WeChat public account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485112&idx=1&sn=efd4f9b472a3d58378407bb6fad46a2f&chksm=eb90f5ccdce77cda0285d53331834a787364d4458a3588173c9fe8ef6953499362bd64f7c918&token=1650861834&lang=zh_CN#rd)

## 1 Introduction

Have you heard of "Graph Databases" before? Is it a database used to store images or a database that stores data in images? (Mistaken) If you've been duped by these two sentences, then read on for today's article~

## 2 Nodes and Relationships

Unlike traditional relational databases, graph databases consist of nodes and relationships (relationships between nodes). As shown below:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V1.png"  />
  <figcaption>Nodes and Relationships</figcaption>
</figure>

### 2.1 Nodes

A node represents an entity. A node is similar to a record in a relational database. The circular patterns in the above figure are all nodes. The orange nodes represent movie entities, and the blue nodes represent specific people.

### 2.2 Relationships

The relationship between two nodes is called a relationship. Three types of "person-movie" relationships appeared in the figure above:

- `ACTED_IN`-Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, and Hugo Weaving participated in the movie
- `DIRECTED`-The Wachowski sisters directed it
- `PRODUCED`-Produced by Joel Silver

### 2.3 Direction of Relationships

In Neo4J, relationships must have directions. For a node, a relationship can have two directions. The relationship pointing to it and the relationship pointing to other nodes from it. In the above figure, all relationships are from people to movies.

### 2.4 Labels

A label is the type of a node or relationship. In the above figure, when defining blue nodes, their label is "Person", and when defining orange nodes, their label is "Movie". The role of a label is that when you make a query, only specific types of nodes are returned. For example, only Person nodes are queried.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V2.png"  />
  <figcaption>Labels</figcaption>
</figure>

### 2.5 Properties

Both nodes and relationships can have properties. Properties are added in the form of name-value pairs. For example, return the name and born properties of all Person in the picture above. Attributes make the information in the graph database richer, and these attributes can also be used when querying, such as querying people born after 1970.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V3.png"  />
  <figcaption>Properties</figcaption>
</figure>

## 3 Why Graph Databases

After reading the general introduction to graph databases, you may find this technology very cool. What value can graph databases bring to business that relational databases cannot? The following two aspects can be used as a reference.

- Efficiently query the relationship between data, especially when the relationship is complex
- Conveniently visualize the relationship between data

When you see the following query results, isn't it pleasing to the eye? The relationship between movies and people is clear at a glance. Of course, this is only a small part of the data query results.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V4.png"  />
  <figcaption>Visualization of Results - 1</figcaption>
</figure>

When there is more data, the visualization results are like this...

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V5.png"  />
  <figcaption>Visualization of Results - 2</figcaption>
</figure>

Of course, no one can get valuable information from such visualization results. So, how should graph databases be applied in business? Please stay tuned for the upcoming series of graph database tutorials, which will definitely give you a more specific understanding of this new and trendy technology! I hope this sharing has helped you, and please feel free to leave a message in the comments section for discussion!

