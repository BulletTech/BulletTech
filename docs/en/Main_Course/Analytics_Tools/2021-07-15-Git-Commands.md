---
template: overrides/blogs.html
tags:
  - git
---

# Git常用命令一览

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-07-15，Reading time: 5 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)

在[一行代码都不写，教你使用GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)这篇文章中，我们介绍了如何使用GitHub Desktop对GitHub进行操作，图形化的界面对不太熟悉命令的朋友非常友好，但有时候，在代码编辑器或者终端中直接运行命令操作Git更方便，所以这篇文章将介绍一些常用的命令，让你的Git水平更上一层楼。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-17/1626508940064-Git.png" width="700" />
  <figcaption>在终端中使用Git</figcaption>
</figure>

## 1 Configure git


First of all, you need to let Git know who you are, so set your username first:


```bash
git config –-global user.name
```


Set mailbox:


```bash
git config --global user.email
```


## 2 Set the git warehouse


Create a blank new warehouse:


```bash
git init
```


A folder of a clone warehouse to the present:


```bash
git clone <repo URL>
```


Display the list of remote warehouses:


```bash
git remote -v
```


Delete a remote warehouse:


```bash
git remote RM <remote warehouse name>
```


Pull the latest modification on the server back to the local area, but do not merge with the current work documents:


```bash
git fetch
```


Pull the latest modification on the server back to the local area and merge directly with the working document:


```bash
git pull
```


## 3 Management file changes


Add all changes to the buffer:


```bash
git add <file name>
```


Remove a file and not save its modification history:


```bash
git rm <file name>
```


Reply to a deleted file and prepare it to submit the update:


```bash
git checkout <deleted file name>
```


Display the status of the modified file:


```bash
git status
```


Some files are useless for projects, such as cache and log files, which are ignored by versions of management. Through this command, you can view the neglected file list:


```bash
git ls-files –other –ignored –exclude-standard
```


Show the change of all files in the current directory:


```bash
git diff
```


## 4 Git submitted related commands


Submit code and comment content:


```bash
git commit -m "<submit content>" "" "" ""
```


Switch to a certain state of submission:


```bash
git checkout <commit>
```


Revisit all changes when submitting:


```bash
git reset –hard <commit>
```


Rejection of changes in the current work folder:


```bash
git reset –hard Head
```


Show modification history:


```bash
git log
```


Stay on the current modification first, and then use it:


```bash
git stash
```


Retrieve the previously shelved file:


```bash
git stash pop
```


Clear the shelves file:


```bash
git stash drop
```


Create a TAG, mark the current file version:


```bash
git tag <tag version>
```


Push the change to Origin:


```bash
git push
```


Push the change to another branch:


```bash
git push <Current branch>: <Want to push the branch>
```


## 5 git branch operation


Show all branches:


```bash
git branch
```


Create a new branch and switch to the new branch:


```bash
git checkout -b <branch name>
```


Switch to the new branch:


```bash
git checkout <branch name>
```


Delete branch:


```bash
git Branch -d <branch name>
```


Merge another branch to the current branch:


```bash
Git Merge <branch name>
```


Pull the branch from the remote warehouse:


```bash
git fetch remote <branch name>
```


View the difference between the two branches:


```bash
Git Diff <Source Branch> <Target Branch>
```


## 6 git tips


Is there a dazzling command to make you dazzling?Test it yourself in the code editor and terminal!Finally, we are summing up some small tips to use git daily to help you reduce errors and improve efficiency:


-At look at the latest Origin status before starting work. May
-Yessor enough tests before submitting updates to ensure that your update is effective
-Submit the update in time, so that teammates can work in synchronized work progress
-Rearly record the clear annotations in the change and submission, and describe it in detail for the difficult part of the unknown part
-M full use of the branch for changes. It is not recommended to change it directly on the master, so as not to have unexpected errors.