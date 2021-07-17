---
template: overrides/blogs.html
---

# Git常用命令一览

!!! info
    作者：袁子弹起飞，发布于2021-07-15，阅读时间：约5分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

在[一行代码都不写，教你使用GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)这篇文章中，我们介绍了如何使用GitHub Desktop对GitHub进行操作，图形化的界面对不太熟悉命令的朋友非常友好，但有时候，在代码编辑器或者终端中直接运行命令操作Git更方便，所以这篇文章将介绍一些常用的命令，让你的Git水平更上一层楼。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-17/1626508940064-Git.png" width="700" />
  <figcaption>在终端中使用Git</figcaption>
</figure>

## 1 配置Git

首先你需要让Git知道你是谁，所以先设置你的用户名：

```bash
git config –-global user.name
```

设置邮箱：

```bash
git config --global user.email
```

## 2 设置Git仓库

创建一个空白的新仓库：

```bash
git init
```

克隆一个仓库到现在所在的文件夹：

```bash
git clone <repo URL>
```

显示远程仓库的列表：

```bash
git remote -v
```

删除一个远程仓库：

```bash
git remote rm <远程仓库名字>
```

将服务器上最新的修改拉回本地，但不与现在的工作文档合并：

```bash
git fetch
```

将服务器上最新的修改拉回本地，并直接与工作文档合并：

```bash
git pull
```

## 3 管理文件变更

将所有变更加入缓冲区：

```bash
git add <文件名>
```

移除一个文件并且不在保存它的修改历史：

```bash
git rm <文件名>
```

回复一个删除的文件并将它准备用于提交更新：

```bash
git checkout <删除的文件名>
```

展示修改文件的状态：

```bash
git status
```

有些文件因为对项目无用，如一些缓存和日志文件，是被版本管理忽略的，通过这个命令可查看被忽略的文件列表：

```bash
git ls-files –other –ignored –exclude-standard
```

显示当前目录中所有文件的变化情况：

```bash
git diff
```

## 4 Git提交的相关命令

提交代码，并且注释内容：

```bash
git commit -m "<提交内容>"
```

切换到某一次提交时的状态：

```bash
git checkout <commit>
```

撤销某次提交时的所有更改：

```bash
git reset –hard <commit>
```

撤销当前工作文件夹中的更改：

```bash
git reset –hard Head
```

显示修改历史：

```bash
git log
```

将当前修改先搁置，之后再用:

```bash
git stash
```

取回先前搁置的文件:

```bash
git stash pop
```

清空搁置的文件:

```bash
git stash drop
```

创建一个tag，标记当前的文件版本：

```bash
git tag <标签版本>
```

将改变推送到origin:

```bash
git push
```

将改变推送到另一个分支:

```bash
git push <当前分支>:<想推送的分支>
```

## 5 Git分支操作

显示所有分支:

```bash
git branch
```

创建一个新分支，并且切换到新的分支:

```bash
git checkout -b <分支名称>
```

切换到新的分支:

```bash
git checkout <分支名称>
```

删除分支:

```bash
git branch -d <分支名称>
```

将另一个分支合并到当前分支:

```bash
git merge <分支名称>
```

从远程仓库拉取分支:

```bash
git fetch remote <分支名称>
```

查看两个分支的区别：

```bash
git diff <源分支> <目标分支>
```

## 6 Git小贴士

五花八门的命令是否让你眼花缭乱了？在代码编辑器和终端中亲手试验吧！最后在总结一些日常使用Git的小贴士，帮助你减少错误，提高效率：

- 在开始工作前先看看最新的origin的状态，有可能你的同伴已经更新了文件，确保你在最新的文件基础上工作
- 提交更新之前确保完成足够的测试，确保你的更新是有效的
- 及时提交更新，这样能够让队友们同步工作进度
- 在更改和提交中记录明确的注释，对难懂的部分详细描述
- 充分利用分支进行更改，不建议直接在master上进行更改，以免出现意料不到的错误
