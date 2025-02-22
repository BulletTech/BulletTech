---
template: overrides/blogs.html
tags:
  - app
  - python
---

# 免费实验平台 - Amazon SageMaker Studio Lab

!!! info
    作者：[Vincent](https://github.com/Realvincentyuan)，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:]()

## 1 SageMaker Studio Lab

本人一直是Google Colab的忠实用户，其免费的GPU对于数据科学研究人员是非常实用的计算资源，但是Colab的基础免费版只能同时使用一个运行时，并且必须科学上网才能访问产品。而Amazon最近推出的[SageMaker Studio Lab](https://studiolab.sagemaker.aws/ "Amazon SageMaker Studio Lab")可谓是Google Colab的同类产品，Amazon也十分慷慨地提供了免费的算力（有CPU和GPU供选择）。==注册账号之后即可在Web端随时开展实验，无需科学上网！==

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/SageMaker_studio_lab.jpg"  />
  <figcaption>Amazon SageMaker Studio Lab</figcaption>
</figure>

注意，笔者在使用CPU和GPU项目过程中`偶尔会碰到当前同时使用人数过多、无法启动项目的提示`，GPU的资源相比于Google Colab更加紧张。如遇到此类状况，可以稍候几分钟，如果仍然无法启动，只能使用别的环境进行实验，这一状况在Google Colab里是从未遇见的，不知日后此类状况会否有改进。

进入项目后，软件界面和原生的JupyterLab非常类似，如果有类似经验的话立马就可上手。同时，这也意味着用户可以同时运行多个代码文件，这是Amazon SageMaker Studio Lab相对于Google Colab的优势。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/Jupyter.png"  />
  <figcaption>Jupyter用户界面</figcaption>
</figure>

文件在项目关闭后仍然会储存在系统里，方便下次继续使用。总的来说，Amazon SageMaker Studio Lab的体验与原生的JupyterLab基本无异。

## 2 其他相关学习资源

Amazon SageMaker Studio Lab在项目主页展示了一些参考的项目，如`Dive into Deep Learning (D2L)`，`Hugging Face`等，这些都是很好的学习资源，点击详情可以将项目复制到自己的文件系统里进行实践。

其中`Dive into Deep Learning (D2L)`由Amazon的`Sr. Principal Scientist李沐`主导，沐神在多个平台免费地教授深度学习的课程：

- 《动手学深度学习》电子书：https://zh-v2.d2l.ai/
- Bilibili @跟李沐学AI：https://space.bilibili.com/1567748478/channel/seriesdetail?sid=358497

感兴趣地不妨前往相应的平台学习和实践！希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>

