---
template: overrides/blogs.html
tags:
  - docker
  - git
---

# 使用GitHub Action自动构建和推送Docker镜像

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-11-20，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/BCzu346DvNga84vEUXUbTQ)

## 1 Introduction


In this article, we will introduce how to automatically push the Docker mirror in the mirror warehouse with GitHub Action, which greatly simplifies the tedious steps of building mirrors and pushing mirrors!We have previously introduced a lot of GitHub's cool features. In order to facilitate understanding the content of this article, it is recommended that the previous article review the basic Github operation knowledge, especially Github Action:


-
[Do not write a line of code, teach you to use github] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3nzgxoq=&mid=2247484191&IDX=1&SN=73AAE2A836729C63637F2E f & chksm = EB90F06BDCE7797D71DEE815E283559F05D0DB8DCAB9C6430C856A8DA05AA79617A9C0EEE39F & Token = 150554771 & Lang = zh_cn#RD)
-
[Git common commands] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3ngxoq=&mid=2247484312&IDX=1&SN=ba2de61356b03b0c6&chkhksmm = EB90F0ECDCE779FAE14099E90400637B801dd4689372C466C036CE0C9dd55E9EC8Deb10bb & Token = 2142567738 & Lang = zh_cn#RD)
-
[玩 转 GitHub] (https://mp.weixin.qq.com/s?__biz=mzi4mjk3nzgxoq==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae0ae5Ad0cb16&chksm=b90f7a6d CE77B0E8B97d3ef36195f91836FC83E897d44853f24332AF13DAFC2A07ff53a0 & Token = 78049789 & Lang = zh_cn#RD)
-
[Make a beautiful online resume with github] (https://mp.weixin.qq.com/s/ns0yxyqbezbujyx21l0w)
-
[Github Action Overview] (https://mp.weixin.qq.com/s/agpifrxa3rhsg0iFCGSBQ)


At the same time, if you need to understand the knowledge of Docker, you can view the masterpiece of Teacher Tina:


-
[Teach you successfully running Docker in the win10 system]
-
[Docker First Experience] (https://mp.weixin.qq.com/s/gfo5bik9fqrtwf8rjp8MPa)


## 2 Configure mirror warehouse


Here is an example of Alibaba Cloud's mirror container service as an example. Other mirror warehouse principles are similar, and you can touch the type of bypass.First log in
[Alibaba Cloud Mirror Image Container Service]
, Perform the following operations:


-The creation of naming space (namespace) as a collection of mirror warehouses can be named by companies or organizations, such as we use the `Bullettech_Services`.
-Colid the mirror warehouse (registry) as a collection of mirror image, you can store different versions of mirror images to the warehouse.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/registry.png"  />

<figcaption> Mirror warehouse </figcaption>
</figure>


## 3 Configure github action


### 3.1 Configuration password


Set a password in the GitHub warehouse for logging in to the mirror container service.You can find the password in the warehouse settings, and then store the accounts and passwords of the image container service.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/secrets.png"  />

<FIGCAPTION> Accounts and Passwords of Storage Mirror container services </figcaption>
</figure>


### 3.2 Create Workflow


First create a workflow in the `.github/workflows` directory, such as` ci.yml`, then understand the command according to the annotation, and modify it according to the project.


```yml
name: actions


ON: [Push, PULL_REQUEST] # trigger event


jobs:
bt-product-release:
IF: $ {{github.ref == 'Refs/heads/main'}} # to detect whether the main branch is updated
runs-on: ubuntu-latest
steps:
-ses: actions/checkout@v2 # pull code to run the server
- name: Login to Aliyun Container Registry (ACR)
uses: Aliyun/ACR-LOGIN@v1 # Use Alibaba Cloud Mirror Service ACTION
with:
login-server: registry.cn-shanghai.aliyuncs.com # must be correctly fill in the login address of the mirror container service
Region-id: CN-SHANGHAI # must be correctly fill in the login address of the mirror container service
username: "$ {secrets.regotion_username}}" # 引
Password: "$ {secrets.regotion_password}}" # 引 p p p p p p p set the mirror container service password
- name: Build and Push Docker Image
env:
Image_tag: $ {{github.sha}} # is used to mark the vector version number
run: |
docker build -t registry.cn-shanghai.aliyuncs.com/bullettech_services/app:$IMAGE_TAG .
docker push registry.cn-shanghai.aliyuncs.com/bullettech_services/app:$IMAGE_TAG
```


In this way, every time the branch is updated, GitHub will build a mirror image based on this updated code and push the image to the specified mirror warehouse (note version):


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/images.png"  />

<figcaption> mirror </figcaption>
</figure>


## 4 Summary


This efficient workflow saves a lot of time, and avoids many errors that are prone to occur during manual operations. GitHub Action is really fragrant!


I hope this sharing will help you, please leave a message in the comment area!


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>