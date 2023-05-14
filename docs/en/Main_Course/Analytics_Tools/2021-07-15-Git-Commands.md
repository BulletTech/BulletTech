---
template: overrides/blogs.html
tags:
  -git
---

# Git common commands list

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-07-15, reading time: about 5 minutes, WeChat public account article link: [: fontaWesome-Solid-Link:] (https:: https:: https:: https:: https://mp.weixinIn.qqpom/s ?__biz=mzi4mjk3nzgxoq===2247484312&IDX=1&SN=420520ba2de61eedb13569b0c6&Chksm=ECDCDCE779FAE11111 4099e90400637B801dd4689372C466C033C36CE0C9DD55E9EC8DEB10BB & Token = 2142567738 & Lang = zh_cn#RD)

Do not write in [one line of code, teach you to use using github] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq=&MID=2247484191&IDX=1&SN=73AE46B2A836729C636B937F2 EF & CHKSM = EB90F06BDCE7797D71DEE815E283559F05D0D0DCAB9C6430C856A8AA79617A9C0EEE39F & Token = 150554771 & Lang = zh_cn#RD)In this article, we introduced how to use GitHub Desktop to operate GitHub. The graphical interface is very friendly to face friends who are not familiar with the command, but sometimes it is more convenient to operate the command directly in the code editor or terminal, so it is more convenient to operate Git, soThis article will introduce some commonly used commands to make your Git level go to the next level.

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-7-17/1626508940064-git.png" width = "700"/>/>/>/>/>/>/>/>/>/>/>/>/>/>/> 700 "/>
  <figcaption> Use git </figcaption> in the terminal
</Figure>

## 1 Configure git

First of all, you need to let Git know who you are, so set your username first:

`` `Bash
git config ---global user.name
`` `

Set mailbox:

`` `Bash
git config --global user.email
`` `

## 2 Set the git warehouse

Create a blank new warehouse:

`` `Bash
git init
`` `

A folder of a clone warehouse to the present:

`` `Bash
git clone <repo url>
`` `

Display the list of remote warehouses:

`` `Bash
git remote -V
`` `

Delete a remote warehouse:

`` `Bash
git remote RM <remote warehouse name>
`` `

Pull the latest modification on the server back to the local area, but do not merge with the current work documents:

`` `Bash
git fetch
`` `

Pull the latest modification on the server back to the local area and merge directly with the working document:

`` `Bash
git pull
`` `

## 3 Management file changes

Add all changes to the buffer:

`` `Bash
git add <file name>
`` `

Remove a file and not save its modification history:

`` `Bash
git rm <file name>
`` `

Reply to a deleted file and prepare it to submit the update:

`` `Bash
git checkout <deleted file name>
`` `

Display the status of the modified file:

`` `Bash
git Status
`` `

Some files are useless for projects, such as cache and log files, which are ignored by versions of management. Through this command, you can view the neglected file list:

`` `Bash
git LS-Files –other – Ignored -exClude-Standard
`` `

Show the change of all files in the current directory:

`` `Bash
git diff
`` `

## 4 Git submitted related commands

Submit code and comment content:

`` `Bash
git commit -m "<submit content>" "" "" ""
`` `

Switch to a certain state of submission:

`` `Bash
git checkout <Commit>
`` `

Revisit all changes when submitting:

`` `Bash
git reset – Hard <Commit>
`` `

Rejection of changes in the current work folder:

`` `Bash
Git Reset – Hard Head
`` `

Show modification history:

`` `Bash
git log
`` `

Stay on the current modification first, and then use it:

`` `Bash
git Stash
`` `

Retrieve the previously shelved file:

`` `Bash
git Stash Pop
`` `

Clear the shelves file:

`` `Bash
git Stash Drop
`` `

Create a TAG, mark the current file version:

`` `Bash
git tag <tag version>
`` `

Push the change to Origin:

`` `Bash
git push
`` `

Push the change to another branch:

`` `Bash
git push <Current branch>: <Want to push the branch>
`` `

## 5 git branch operation

Show all branches:

`` `Bash
git Branch
`` `

Create a new branch and switch to the new branch:

`` `Bash
git checkout -b <branch name>
`` `

Switch to the new branch:

`` `Bash
git checkout <branch name>
`` `

Delete branch:

`` `Bash
git Branch -d <branch name>
`` `

Merge another branch to the current branch:

`` `Bash
Git Merge <branch name>
`` `

Pull the branch from the remote warehouse:

`` `Bash
git fetch remote <branch name>
`` `

View the difference between the two branches:

`` `Bash
Git Diff <Source Branch> <Target Branch>
`` `

## 6 git tips

Is there a dazzling command to make you dazzling?Test it yourself in the code editor and terminal!Finally, we are summing up some small tips to use git daily to help you reduce errors and improve efficiency:

-At look at the latest Origin status before starting work. May
-Yessor enough tests before submitting updates to ensure that your update is effective
-Submit the update in time, so that teammates can work in synchronized work progress
-Rearly record the clear annotations in the change and submission, and describe it in detail for the difficult part of the unknown part
-M full use of the branch for changes. It is not recommended to change it directly on the master, so as not to have unexpected errors.