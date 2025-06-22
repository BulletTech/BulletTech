---
template: overrides/blogs.html
tags:
  - git
---

# Explore GitHub

!!! info
    Author: Void, published on 2021-10-14, reading time: about 5 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)

## 1 Introduction

GitHub's main function is to manage and collaborate on code versions. In the article "Learn how to use GitHub without writing a single line of code," we detailed what GitHub can do and how to use it. 
In fact, GitHub can also be very interesting. From a different perspective, this article will talk about the fun features of GitHub.

## 2 Action

GitHub Action provides a set of services for automating script commands. Our team uses GitHub Pages to build our blog. When we update our articles on GitHub, naturally, we want this change to be automatically updated in our blog. 
Without this automated deployment service, we may need to manually run some scripts every time to deploy the articles to the blog. 
Now we just need to create a ci.yml file in this path (BulletTech/.github/workflows) and write the commands we need into it. When changes are pushed to the main branch, GitHub Action can automatically run the set script for us.

```yml
name: ci
on:
  push:
    branches:
      - master
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - run: python ./docs/Scripts/Update_reading_time.py
      - run: pip install mkdocs-material
      - run: pip install --upgrade mkdocs-material
      - run: pip install mkdocs-redirects
      - run: pip install mkdocs-minify-plugin
      - run: pip install mkdocs-macros-plugin
      - run: pip install mkdocs-git-revision-date-localized-plugin
      - run: git pull
      - run: mkdocs gh-deploy --force
```

In addition to the workflows we create ourselves, GitHub also has a rich workflow community where you can choose different workflows to meet your various needs.

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github4.png" width="500" />
</figure>

## 3 Projects

GitHub comes with project management functionality. 
First, we click on the Projects tab to see the projects we've created.

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github1.png" width="500" />
</figure>

Clicking on a project, we can see the board-like structure, with To do, In progress, Done, and other columns, and of course, we can create new ones.

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github2.png" width="500" />
</figure>

We can create notes by clicking the plus sign in a column. In the illustration, we can see that the note in the To do column is an issue. How is this achieved? 
During the issue creation process, we can notice a Projects item in the right hand sidebar. If we select the corresponding column, we can insert this issue as a card into this column.

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github3.png" width="500" />
</figure>

We can also add issues directly to the board with the add card function. 
With project board functionality, we can more easily manage projects and collaborate with teams.

## 4 Wiki

GitHub's Wiki allows us to build a wiki for this repo in markdown text, allowing users to better understand the repo content beyond README documents. Excellent examples include Pytorch's [Wiki](https://github.com/pytorch/pytorch/wiki).

## 5 Security

GitHub Security provides tools for code security. 

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github5.png" width="500" />
</figure>

For example, we can use Security.md to alert users to certain potential issues in the code, as TensorFlow Repo's [Security file](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md) shows. 
We can also set up a code security scan workflow with GitHub Action. It can automatically scan code for syntax errors, insecure input (user input displayed), etc. in branches and pull requests.

## 6 Insights

GitHub Insights provides repo-wide and individual commit, pull request, and other behavior information in intuitive chart form.

<figure>
  <img src="https://raw.githubusercontent.com/BulletTech2021/Pics/main/img/github6.png" width="500" />
</figure>

## 7 Summary

GitHub can also be very interesting. In addition to the provided regular features, GitHub provides many interesting and useful features. They not only greatly improve productivity, but also enrich GitHub's content.

