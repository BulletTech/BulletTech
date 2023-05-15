---
template: overrides/blogs.html
tags:
  - git
---

# GitHub Action概览

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-11-13，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/aGPIfrXA3rHsg0ioFcGsBQ)

## 1 Introduction


We have previously introduced a lot of GitHub's cool features. In order to facilitate understanding the content of this article, it is recommended that the previous article review the basic Github operation knowledge:


-
[Do not write a line of code, teach you to use github] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq=&mid=2247484191&IDX=1&Sn=73a2a836729C63637F2E f & chksm = EB90F06BDCE7797D71DEE815E283559F05D0DB8DCAB9C6430C856A8DA05AA79617A9C0EEE39F & Token = 150554771 & Lang = zh_cn#RD)
-
[Git common commands] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3ngxoq=&mid=2247484312&IDX=1&SN=ba2de61356b03b0c6&chkhksmm = EB90F0ECDCE779FAE14099E90400637B801dd4689372C466C036CE0C9dd55E9EC8Deb10bb & Token = 2142567738 & Lang = zh_cn#RD)
-
-
[Make a beautiful online resume with github] (https://mp.weixin.qq.com/s/ns0yxyqbezbujyx21l0w)


In this article, we will introduce how to use GitHub Action to simplify the work of repeated machinery to greatly improve efficiency and save time.


## 2 GitHub Action Overview


GitHub Action can automatically execute the custom script to complete the pre -set work.Users need to set the command (event) and commands when the conditions are met. Github can automatically complete the preset operation. For example, when there is a update merged to the master/main branch, the test script check error is automatically executed.The following figure shows the component of GitHub Action:


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/overview-actions-design.png"  />

<figcaption> GitHub Action component, source: github official website </figCaption>
</figure>


GitHub automatically trigger the workflow when the incident occurs.The program is then executed according to the step.


## 3 Create ACTION


Github action use
[YAML](https://yaml.org/ 'YAML')
Define the trigger events, work, and steps. The workflow file needs to be stored in a specific location in the code warehouse: `.github/workflows`.


by
[Bullettech Blog's continuous integrated workflow]
For example:


```yml
Name: CI
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


The main points are as follows:


-` Name` defines the name of the workflow, here is the continuing integration (CI).
-` On` is the event that triggers the workflow, which is defined as an update command to execute the command when pushing to the main branch.
-`Jobs` defines the work task. Deploy is the name of the job, running a series of steps on Github's Ubuntu Linux virtual machine.
-`users`
[GitHub Action Market]
Action in it.Here is using Action to check out warehouse and download the code to the server running code. At the same time, the Python operating environment is configured.
-` Run` connect the commands to be executed. Here are some Python packets relying on blogs and run the deployment command.


## 4 View Action run status


In the github warehouse's Actions tag, you can see the running status of the Action:


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Action_Status.png"  />

<figcaption> github action status </figcaption>
</figure>


You can see the CI workflow used by Bullettech. Click RUNS to view the running status of each step.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/Action_steps.png"  />

<figcaption> Action operation </figcaption>
</figure>




## 5 Summary


The use of github action has automated many repeated mechanical labor. The saving time can be used for more meaningful things. More content can view the following reference materials to customize the workflow that is suitable for your own.


I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>