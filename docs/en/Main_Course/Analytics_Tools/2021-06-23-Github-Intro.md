---
template: overrides/blogs.html
tags:
  - git
---

# How to Use GitHub without Writing a Single Line of Code

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), published on June 23, 2021, reading time: about 5 minutes, WeChat article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)

## 1 What is GitHub?

Many people think of GitHub as a tool mainly used by programmers for coding. In fact, the main feature of GitHub is version control and collaboration, which means that not only programmers but also non-technical people can use it to work more efficiently. Therefore, this article will teach you how to use GitHub from scratch, and help you get to know this powerful productivity tool. First, let's get familiar with some common GitHub terms:

- Repository: can be considered as a folder for storing code and files. When you are the repository owner, you can set access permissions.
- Remote Repository: a copy of the repository, usually used to make changes, which will be later added to the repository main branch.
- Main/Branch: the current status of the project.
- Branch: a copy of the main branch, used to temporarily store modified states, usually for updating the main branch.
- Push: submit modifications to the repository.
- Pull: synchronize updates from the repository to the current work state.
- Pull Request: used to merge modifications on the branch to the main branch.
- Merged: updates on the branch have been merged to the main branch, and the repository is updated.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-17/1626489355119-Github%20%E5%9B%BE%E4%BE%8B.png" width="600" />
  <figcaption>Diagram of common GitHub terms</figcaption>
</figure>

Next, we will mainly use the GitHub Desktop client (which can be downloaded for free from the official website) to introduce the functions, which allows you to use most of GitHub's core functions.

## 2 What Can GitHub Do?

GitHub is an excellent tool for version control and collaboration.

### 2.1 Version Control

Specifically, version management can help save the modified history of files, so that it can be easily checked and rolled back when needed.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-17/1626489404945-Github%20%E6%9F%A5%E7%9C%8B%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC.png" width="600" />
  <figcaption>GitHub Desktop view of version history</figcaption>
</figure>

In the example, BulletTech's repository saves the change history, and you can click on the change to see the modified files and the corresponding updates.

### 2.2 Collaboration

These changes were made by members of the BulletTech team. When multiple people collaborate, it is recommended to work on different branches. After completing the updates, you can merge the updates on your branch to the main branch through a pull request (⌘/Ctrl + R). At this time, the software will automatically guide you to the web page to create a request. Members of the team can review the changes. If they meet the requirements, the update can be merged to the main branch.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-7-17/1626489452783-Github%E5%90%88%E5%B9%B6%E8%AF%B7%E6%B1%82.png" width="600" />
  <figcaption>Merge request</figcaption>
</figure>

It is recommended to set the merge request template. Filling in the update information clearly will save a lot of communication time and make it easier to trace back in the future. You can find the corresponding template in our [repository](https://github.com/BulletTech/BulletTech/tree/main/.github) and modify it according to your needs for use in your own project.

### 2.3 Build a Blog

GitHub provides free server hosting for simple blogs. BulletTech's own blog is built on GitHub. You just need to enable the GitHub Pages feature in the repository settings, and the blog will be generated automatically. GitHub provides many templates to choose from, or you can write your own from scratch. We won't go into detail here. If you are interested, please visit our [repository](https://bullettech.github.io/BulletTech/) to view the source code and learn.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-24/1624539190066-Blog.jpeg" width="300" />
  <figcaption>BulletTech blog</figcaption>
</figure>

## 3 How to Use GitHub

### 3.1 Create a Repository

After registering for GitHub, on your homepage, click the most prominent green button (New) to create a new repository. Clicking into the repository and clicking the green button (Code) will open GitHub Desktop and download the files to your computer. You can now start your project!

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-24/1624540363015-%E5%88%9B%E5%BB%BA%E4%BB%93%E5%BA%93.png" width="600" />
  <figcaption>Create a repository</figcaption>
</figure>

<figure>
  <img src="https://user-images.githubusercontent.com/84658804/123267740-ecebfd00-d52f-11eb-85d9-b2f90583bf4c.png" width="600" />
  <figcaption>Open the repository with GitHub Desktop</figcaption>
</figure>

### 3.2 Basic Functions of GitHub Desktop

Basic operations are shown in the figure below. Please note that sometimes there may be conflicts when synchronizing (pulling) the repository. Most of the time it is because the local update has not been synchronized to the branch, but other people have updated the branch. In this case, you need to stash or discard your updates before synchronizing, which can be found in the top menu under Branch.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-26/1624676128227-%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C.png" width="600" />
  <figcaption>Basic operations of GitHub Desktop</figcaption>
</figure>

In summary, after mastering these basic knowledge and skills, you can use GitHub smoothly for file management, collaborative work, and create your own blog, and so far, without writing a single line of code. Of course, using code can also operate GitHub conveniently. Next time we will use command operations to explore GitHub. Stay tuned!

