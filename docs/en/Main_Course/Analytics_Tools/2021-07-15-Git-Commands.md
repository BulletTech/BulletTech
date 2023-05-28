---
template: overrides/blogs.html
tags:
  - git
---

# A List of Common Git Commands

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-07-15, Reading Time: about 5 minutes, Article link on WeChat Official Account: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)

In the article [Teach You to Use GitHub with Zero Code](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd) where we introduced how to use GitHub Desktop to operate GitHub, the graphical interface is very friendly for friends who are not familiar with commands. However, sometimes it is more convenient to directly run Git commands in a code editor or terminal, so this article will introduce some commonly used commands to help you level up your Git skills.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-17/1626508940064-Git.png" width="700" />
  <figcaption>Using Git in the terminal</figcaption>
</figure>

## 1 Configuring Git

First, you need to let Git know who you are, so set your username:

```bash
git config –-global user.name
```

Set your email:

```bash
git config --global user.email
```

## 2 Setting up Git repository

Create a new blank repository:

```bash
git init
```

Clone a repository to the current folder:

```bash
git clone <repo URL>
```

Display the list of remote repositories:

```bash
git remote -v
```

Delete a remote repository:

```bash
git remote rm <remote repository name>
```

Fetch the latest changes from the server, but do not merge them into the current working document:

```bash
git fetch
```

Fetch and merge the latest changes from the server into the current working document:

```bash
git pull
```

## 3 Managing changes to files

Add all changes to the cache:

```bash
git add <file name>
```

Remove a file and do not keep its modification history:

```bash
git rm <file name>
```

Recover a deleted file and prepare it for update submission:

```bash
git checkout <deleted file name>
```

Display the status of modified files:

```bash
git status
```

Some files are ignored by version control because they are unnecessary for the project, such as some cache and log files. Use this command to view the list of ignored files:

```bash
git ls-files –other –ignored –exclude-standard
```

Display the changes of all files in the current directory:

```bash
git diff
```

## 4 Git commands related to submitting changes

Submit the changes and comment the content:

```bash
git commit -m "<commit content>"
```

Switch to the state of a certain submission:

```bash
git checkout <commit>
```

Undo all changes made in a certain submission:

```bash
git reset –hard <commit>
```

Undo changes in the current working folder:

```bash
git reset –hard Head
```

Display modification history:

```bash
git log
```

Stash current changes and use later:

```bash
git stash
```

Retrieve previously stashed files:

```bash
git stash pop
```

Clear stashed files:

```bash
git stash drop
```

Create a tag to mark the current file version:

```bash
git tag <tag version>
```

Push changes to origin:

```bash
git push
```

Push changes to another branch:

```bash
git push <current branch>:<branch to push to>
```

## 5 Git branch operations

Display all branches:

```bash
git branch
```

Create a new branch and switch to the new branch:

```bash
git checkout -b <branch name>
```

Switch to a new branch:

```bash
git checkout <branch name>
```

Delete a branch:

```bash
git branch -d <branch name>
```

Merge another branch into the current branch:

```bash
git merge <branch name>
```

Fetch a branch from a remote repository:

```bash
git fetch remote <branch name>
```

Check the differences between two branches:

```bash
git diff <source branch> <destination branch>
```

## 6 Git Tips

Are the myriad of commands making you dizzy? Try it out in your code editor and terminal! Finally, summarize some tips for using Git in your daily life to help you reduce errors and improve efficiency:

- Before you start work, check the current status of origin first. Your teammates may have updated the files, make sure you work on the latest files.
- Make sure to complete sufficient testing before submitting updates to ensure your updates are valid.
- Submit updates in a timely manner to allow your teammates to synchronize their progress.
- Clearly describe the comments in the changes and submissions, describe the difficult parts in detail.
- Make full use of branching to make changes. It is not recommended to make changes directly on the master branch to avoid unexpected errors.