---
template: overrides/blogs.html
tags:
  -git
---

# Github action overview

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-11-13, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-solid-Link:] (https://mp.weixin.qq.q.q.qq.q.qq.qq.qq.qq.qq.qq.qq.qq.qq.qq.com/s/agpifrxa3rhsg0iFCGSBQ)

## 1 Introduction

We have previously introduced a lot of GitHub's cool features. In order to facilitate understanding the content of this article, it is recommended that the previous article review the basic Github operation knowledge:

- [Do not write a line of code, teach you to use github] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq=&mid=2247484191&IDX=1&SN=73AE46B2A836363637F2 EF & CHKSM = EB90F06BDCE7797D71DEE815E283559F05D0DB8DCAB9C6430C856A8DA05AA79617A9C0EEE39F & Token = 150554771 & Lang = zh_cn#RD)
- [List of common commands for git] (https://mp.weixin.qq.com/s ?_biz=mzi4mjk3ngxoq=&mid=2247484312&idx=1&Sn=ba2De61356B03B0C6&CHKHKKKKS M = EB90F0ECDCE779FAE14099E90400637B801DD4689372C466C0336CE0C9DDD55E9EC8DEB10BB & Token = 2142567738 & LANG = ZH_CN#RD)
- [Play to github] (https://mp.weixinin.qq.com/s ?__biz=mzi4mjk3ngxoq===2247484626&IDX=1&SN=BCD93607AE2DDE7CD0CB16&CHKSM= EB90F7A6DCE77EB0E8B97D3EF36195F91836FC83E897D44853F2424332AFC2A07FF53A0 & Token = 78049789 & LANG = zh_cn#RD)
- [Make a beautiful online resume with github] (https://mp.weixin.qq.com/s/ns0yqbezbujyx21l0w)

In this article, we will introduce how to use GitHub Action to simplify the work of repeated machinery to greatly improve efficiency and save time.

## 2 GitHub Action Overview

GitHub Action can automatically execute the custom script to complete the pre -set work.Users need to set the command (event) and commands when the conditions are met. Github can automatically complete the preset operation. For example, when there is a update merged to the master/main branch, the test script check error is automatically executed.The following figure shows the component of GitHub Action:

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/img/overView-Actor-design.png"/>/>/>
  <figcaption> GitHub Action component, source: github official website </figCaption>
</Figure>

GitHub automatically trigger the workflow when the incident occurs.The program is then executed according to the step.

## 3 Create ACTION

Github action uses [yaml] (https://yaml.org/ 'yaml') to define trigger events, work, and steps. The workflow file needs to be stored in a specific location in the code warehouse: `.github/workflows`.

With the [Bullettech Blog's continuous integrated workflow] (https://github.com/bullettech/bullettech/blob/main/.github/workflows/ci.yml 'Bullettech blog'),::

`` `yml
Name: ci
ON:
  push:
    Branches:
      -Main
Jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      -sES: Actions/Checkout@v2
      -sES: Actions/Setup-Python@v2
        with:
          python-version: 3.x
      -run: python ./docs/scripts/Update_reaming_time.py
      -run: PIP Install MKDocs-Material
      -run: PIP Install Mkdocs-Redirects
      -run: PIP Install mkdocs-minify-plugin
      -run: PIP Install mkdocs-macros-plugin
      -run: PIP Install Mkdocs-Git-Revision-Date-Localized-Plugin
      -run: PIP Install-Upgrade MKDocs-Material
      -run: PIP Install-Upgrade MKDocs-Redirects
      -run: PIP Install-Upgrade MKDocs-minify-plugin
      -run: PIP Install-Upgrade MKDocs-Macros-Plugin
      -run: PIP Install-Upgrade MKDocs-Git-Revision-Date-Localized-Plugin
      -run: git pull
      -run: MKDOCS GH-DEPLOY-FORCE
`` `

The main points are as follows:

-` Name` defines the name of the workflow, here is the continuing integration (CI).
-` On` is the event that triggers the workflow, which is defined as an update command to execute the command when pushing to the main branch.
-`Jobs` defines the work task. Deploy is the name of the job, running a series of steps on Github's Ubuntu Linux virtual machine.
  -` USES` and then connect [Github Action market] (https://github.com/marketplace?Type=actions 'github action market').Here is using Action to check out warehouse and download the code to the server running code. At the same time, the Python operating environment is configured.
  -` Run` connect the commands to be executed. Here are some Python packets relying on blogs and run the deployment command.

## 4 View Action run status

In the github warehouse's Actions tag, you can see the running status of the Action:

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/img/action_status.png"/>/>/>
  <figcaption> github action status </figcaption>
</Figure>

You can see the CI workflow used by Bullettech. Click RUNS to view the running status of each step.

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/img/action_Steps.png"/>/>/>
  <figcaption> Action operation </figcaption>
</Figure>


## 5 Summary

The use of github action has automated many repeated mechanical labor. The saving time can be used for more meaningful things. More content can view the following reference materials to customize the workflow that is suitable for your own.

I hope this sharing will help you, please leave a message in the comment area!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>