---
template: overrides/blogs.html
tags:
  -docker
  -git
---

# Use github action to automatically build and push the Docker mirror

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published at 2021-11-20, read time: about 6 minutes, WeChat public account article link: [: fontaWesome-Solid-Link:] (https://mp.weixin.qq.q.com/s/bczu346DVNGA84veuxubtq)

## 1 Introduction

In this article, we will introduce how to automatically push the Docker mirror in the mirror warehouse with GitHub Action, which greatly simplifies the tedious steps of building mirrors and pushing mirrors!We have previously introduced a lot of GitHub's cool features. In order to facilitate understanding the content of this article, it is recommended that the previous article review the basic Github operation knowledge, especially Github Action:

- [Do not write a line of code, teach you to use github] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq=&mid=2247484191&IDX=1&SN=73AE46B2A836363637F2 EF & CHKSM = EB90F06BDCE7797D71DEE815E283559F05D0DB8DCAB9C6430C856A8DA05AA79617A9C0EEE39F & Token = 150554771 & Lang = zh_cn#RD)
- [List of common commands for git] (https://mp.weixin.qq.com/s ?_biz=mzi4mjk3ngxoq=&mid=2247484312&idx=1&Sn=ba2De61356B03B0C6&CHKHKKKKS M = EB90F0ECDCE779FAE14099E90400637B801DD4689372C466C0336CE0C9DDD55E9EC8DEB10BB & Token = 2142567738 & LANG = ZH_CN#RD)
- [Play to github] (https://mp.weixinin.qq.com/s ?__biz=mzi4mjk3ngxoq===2247484626&IDX=1&SN=BCD93607AE2DDE7CD0CB16&CHKSM= EB90F7A6DCE77EB0E8B97D3EF36195F91836FC83E897D44853F2424332AFC2A07FF53A0 & Token = 78049789 & LANG = zh_cn#RD)
- [Make a beautiful online resume with github] (https://mp.weixin.qq.com/s/ns0yqbezbujyx21l0w)
- [Github Action Overview] (https://mp.weixin.qq.com/s/agpifrxa3rhsg0iofgsbq)

At the same time, if you need to understand the knowledge of Docker, you can view the masterpiece of Teacher Tina:

- [Teach you to run docker in the win10 system] (https://mp.weixin.qq.com/8b9ye55zpwccvta4flqq)
- [Docker First Experience] (https://mp.weixin.qq.com/s/gfo5bik9fqrtwf8rjp8mpa)

## 2 Configure mirror warehouse

Here is an example of Alibaba Cloud's mirror container service as an example. Other mirror warehouse principles are similar, and you can touch the type of bypass.First log in to [Alibaba Cloud Mirror Image Container Service] (https://cr.Console.aliyun.com/cn-shanghai/instance/repositories 'Alibaba Cloud Mirror Image Container Service')).

-The creation of naming space (namespace) as a collection of mirror warehouses can be named by companies or organizations, such as we use the `Bullettech_Services`.
-Colid the mirror warehouse (registry) as a collection of mirror image, you can store different versions of mirror images to the warehouse.

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/img/registry.png"/>/>/>
  <figcaption> Mirror warehouse </figcaption>
</Figure>

## 3 Configure github action

### 3.1 Configuration password

Set a password in the GitHub warehouse for logging in to the mirror container service.You can find the password in the warehouse settings, and then store the accounts and passwords of the image container service.

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/img/secrets.png"/>/>/>
  <FIGCAPTION> Accounts and Passwords of Storage Mirror container services </figcaption>
</Figure>

### 3.2 Create Workflow

First create a workflow in the `.github/workflows` directory, such as` ci.yml`, then understand the command according to the annotation, and modify it according to the project.

`` `yml
name: ACTIONS

ON: [Push, PULL_REQUEST] # trigger event

Jobs:
  BT-PRODUCT-Release:
    IF: $ {{github.ref == 'Refs/heads/main'}} # to detect whether the main branch is updated
    runs-on: ubuntu-latest
    steps:
    -ses: actions/checkout@v2 # pull code to run the server
    -name: Login to aliyun container registry (ACR)
      uses: Aliyun/ACR-LOGIN@v1 # Use Alibaba Cloud Mirror Service ACTION
      with:
        login-server: registry.cn-shanghai.aliyuncs.com # must be correctly fill in the login address of the mirror container service
        Region-id: CN-SHANGHAI # must be correctly fill in the login address of the mirror container service
        username: "$ {secrets.regotion_username}}" # 引
        Password: "$ {secrets.regotion_password}}" # 引 p p p p p p p set the mirror container service password
    -name: build and push docker image
      ENV:
        Image_tag: $ {{github.sha}} # is used to mark the vector version number
      Run: | |
        docker build -t registry.cn-shanghai.aliyuncs.com/bullettech_services/app: $image_tag.
        docker push registry.cn-shanghai.aliyuncs.com/bullettech_services/app: $image_tag_tag
`` `

In this way, every time the branch is updated, GitHub will build a mirror image based on this updated code and push the image to the specified mirror warehouse (note version):

<figure>
  <img src = "https://cdn.jsdelivr.net/gh/bullettech2021/pics/img/images.png"/>/>/>
  <figcaption> mirror </figcaption>
</Figure>

## 4 Summary

This efficient workflow saves a lot of time, and avoids many errors that are prone to occur during manual operations. GitHub Action is really fragrant!

I hope this sharing will help you, please leave a message in the comment area!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>