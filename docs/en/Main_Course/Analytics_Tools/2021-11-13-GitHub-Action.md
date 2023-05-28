---
template: overrides/blogs.html
tags:
  - git
---

# GitHub Action Overview

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan)，Published on 2021-11-13，Reading time: about 6 minutes，WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/aGPIfrXA3rHsg0ioFcGsBQ)

## 1 Introduction

We have introduced many cool features of GitHub before. To better understand the content of this article, it is recommended to review the basic GitHub operation knowledge in the previous articles:

- [Teach You How to Use GitHub without Writing Any Code](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)
- [Git Commonly Used Commands](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)
- [Play with GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)
- [Create a Beautiful Online Resume Using GitHub](https://mp.weixin.qq.com/s/Ns0YXYQBEZbUJEJyX21L0w)

In this article, we will introduce how to use GitHub Actions to simplify repeated mechanical tasks and greatly improve efficiency and save time.

## 2 GitHub Action Overview

GitHub Action can automatically execute custom scripts to complete preset work. Users need to set the triggering conditions (events) and the commands to be executed when the conditions are met. GitHub can automatically complete the preset operations, for example, when a update is merged to the master/main branch, automatically execute the test script to check for errors. The following figure shows the components when GitHub Action is executed:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/overview-actions-design.png"  />
  <figcaption>GitHub Action components, source: GitHub</figcaption>
</figure>

When an event occurs, GitHub automatically triggers the workflow. Then the program executes step by step.

## 3 Create Action

GitHub Action uses [YAML](https://yaml.org/ 'YAML') to define the triggered events, work, and steps. The workflow file needs to be stored in a specific location in the code repository: `.github/workflows`.

Take the continuous integration workflow of the [BulletTech blog](https://github.com/BulletTech/BulletTech/blob/main/.github/workflows/ci.yml 'BulletTech workflow') as an example:

```yml
name: ci
on:
  push:
    branches:
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
      - run: pip install mkdocs-redirects
      - run: pip install mkdocs-minify-plugin
      - run: pip install mkdocs-macros-plugin
      - run: pip install mkdocs-git-revision-date-localized-plugin
      - run: pip install --upgrade mkdocs-material
      - run: pip install --upgrade mkdocs-redirects
      - run: pip install --upgrade mkdocs-minify-plugin
      - run: pip install --upgrade mkdocs-macros-plugin
      - run: pip install --upgrade mkdocs-git-revision-date-localized-plugin   
      - run: git pull
      - run: mkdocs gh-deploy --force
```

Key points are as follows:

- `name` defines the name of the workflow, in this case, continuous integration (CI).
- `on` is the event that triggers the workflow. Here, it is defined that the command needs to be executed when a push is updated to the main branch.
- `jobs` defines the work tasks. `deploy` is the name of the work. It runs a series of steps on GitHub's Ubuntu Linux virtual machine.
  - `uses` is followed by an action in GitHub Action Marketplace. Here, actions are used to check out the repository and download the code to the server that runs the code, and configure the Python runtime environment.
  - `run` is followed by the command to be executed. Here, some Python packages required by the blog are installed and the deployment command is run.

## 4 Check Action Status

In the Actions tab of the GitHub repository, you can see the running status of the action:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Action_Status.png"  />
  <figcaption>GitHub Action status</figcaption>
</figure>

You can see the `ci` workflow used by BulletTech, and click on `runs` to view the running status of each step of the action.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Action_steps.png"  />
  <figcaption>Action running status</figcaption>
</figure>

## 5 Conclusion

Using GitHub Action automates many repetitive and mechanical labor tasks, saving time that can be used for more meaningful things. For more information, please refer to the following reference materials to customize your own workflow.

I hope this sharing can help you. Feel free to leave a comment in the comment section for discussion!

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>