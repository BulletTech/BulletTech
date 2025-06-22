---
template: overrides/blogs.html
tags:
  - docker
  - git
---

# Automatically Build and Push Docker Image with GitHub Action

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), Published on 2021-11-20, Read time: About 6 minutes, WeChat Official Account Article Link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/BCzu346DvNga84vEUXUbTQ)

## 1 Introduction

In this article, we will introduce how to use GitHub Action to automatically push Docker images to a registry, greatly simplifying the tedious process of building and pushing images! We have introduced many cool features of GitHub before. To facilitate the understanding of the content of this article, we recommend reviewing the basic GitHub operation knowledge in the previous article, especially GitHub Action:

- [Teaching You to Use GitHub with One Line of Code](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484191&idx=1&sn=73a2aae2e46b2a836729c636b937f2ef&chksm=eb90f06bdce7797d71dee815e283559f05d0db8dcab9c6430c856a8da05aa79617a9c0eee39f&token=150554771&lang=zh_CN#rd)
- [Git Common Commands Overview](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484312&idx=1&sn=420520ba2de61eedb13569b8cb03b0c6&chksm=eb90f0ecdce779fae14099e90400637b801dd4689372c466c033c36ce0c9dd55e9ec8deb10bb&token=2142567738&lang=zh_CN#rd)
- [Playing with GitHub](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484626&idx=1&sn=bcd9360a407ae2dde75e0ae5acd0cb16&chksm=eb90f7a6dce77eb0e8b97d3ef36195f91836fc83e897d44853f2424332af13dafc2a07ff53a0&token=78049789&lang=zh_CN#rd)
- [Create a Beautiful Online Resume with GitHub](https://mp.weixin.qq.com/s/Ns0YXYQBEZbUJEJyX21L0w)
- [Overview of GitHub Action](https://mp.weixin.qq.com/s/aGPIfrXA3rHsg0ioFcGsBQ)

At the same time, if you need to understand Docker knowledge, you can check out Tina's masterpiece:

- [Teaching You to Run Docker Successfully on Win10 System](https://mp.weixin.qq.com/s/8B9ye55zpWCCVTA4g4fLQQ)
- [Experience Docker for the First Time](https://mp.weixin.qq.com/s/gfO5BiK9fqRtWf8rjP8mPA)

## 2 Configure the Image Registry

Here we take Aliyun's image registry as an example for demonstration. The principles of other image registries are similar and can be applied by analogy. First, log in to the [Aliyun image registry](https://cr.console.aliyun.com/cn-shanghai/instance/repositories 'Aliyun Image Registry'), and perform the following operations:

- Create a namespace as a collection of image repositories, named after the company or organization. We use `bullettech_services`.
- Create an image repository as a collection of images that can store different versions of images in the repository.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/registry.png"  />
  <figcaption>Image Registry</figcaption>
</figure>

## 3 Configure the GitHub Action

### 3.1 Configure the Password

Set a password in the GitHub repository for logging in to the image registry. You can find the password in the repository settings and then store the login name and password of the image registry service.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/secrets.png"  />
  <figcaption>Store the login name and password of the image registry service</figcaption>
</figure>

### 3.2 Create the Workflow

First, create a workflow in the `.github/workflows` directory, such as `ci.yml`, and understand the commands based on the comments, and modify them according to the project situation.

```yml
name: actions

on: [push, pull_request] # Trigger Event

jobs:
  bt-product-release:
    if: ${{ github.ref == 'refs/heads/main' }}  # Check if the main branch is updated
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2 # pull the code to the running server
    - name: Login to Aliyun Container Registry (ACR)
      uses: aliyun/acr-login@v1 # Use the Aliyun Image Service Action
      with:
        login-server: registry.cn-shanghai.aliyuncs.com # Be sure to correctly fill in the login address of the image registry service
        region-id: cn-shanghai
        username: "${{ secrets.REGISTRY_USERNAME }}" # Reference the username of the image registry service set in GitHub repo
        password: "${{ secrets.REGISTRY_PASSWORD }}" # Reference the password of the image registry service set in GitHub repo
    - name: Build and Push Docker Image
      env:
        IMAGE_TAG: ${{ github.sha }} # Used to mark the container version number
      run: |
        docker build -t registry.cn-shanghai.aliyuncs.com/bullettech_services/app:$IMAGE_TAG .
        docker push registry.cn-shanghai.aliyuncs.com/bullettech_services/app:$IMAGE_TAG
```

This way, every time the main branch is updated, GitHub will build the image based on the updated code, and push the image to the designated image repository (pay attention to the version):

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/images.png"  />
  <figcaption>Image</figcaption>
</figure>

## 4 Conclusion

This efficient workflow saves a lot of time and avoids many errors that are prone to occur during manual operations. GitHub Action is so awesome!

I hope this sharing will help you, and welcome to leave a message in the comments to discuss!

