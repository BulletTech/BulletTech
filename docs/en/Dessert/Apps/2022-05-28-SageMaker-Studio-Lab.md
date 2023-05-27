# Free Experiment Platform - Amazon SageMaker Studio Lab

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), published on 2021-06-06, reading time: about 6 minutes, WeChat official account article link: [:fontawesome-solid-link:]()

## 1 SageMaker Studio Lab

I have always been a loyal user of Google Colab, and its free GPUs are very useful computing resources for data science researchers. However, the basic free version of Colab can only use one runtime at a time and must have scientific internet access to access the product. Recently, Amazon launched the [SageMaker Studio Lab](https://studiolab.sagemaker.aws/ "Amazon SageMaker Studio Lab"), which can be seen as a similar product to Google Colab. Amazon also generously provides free computing power (with CPU and GPU options). ==After registering an account, experiments can be conducted anytime on the web without needing scientific internet access! ==

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/SageMaker_studio_lab.jpg"  />
  <figcaption>Amazon SageMaker Studio Lab</figcaption>
</figure>

Note: I occasionally encountered a prompt saying "there are too many users currently using the CPU and GPU projects concurrently, and they cannot be launched" during the use of CPU and GPU projects, and the resources of the GPU are more scarce compared with Google Colab. If this situation occurs, you can wait a few minutes. If it still cannot be launched, you can only use another environment for experiments. I have never encountered this situation in Google Colab, and I am not sure if it will be improved in the future.

After entering the project, the software interface is very similar to the native JupyterLab, and if you have similar experience, you can start using it immediately. At the same time, this also means that users can run multiple code files at the same time, which is an advantage of Amazon SageMaker Studio Lab compared to Google Colab.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/1_V/Jupyter.png"  />
  <figcaption>Jupyter user interface</figcaption>
</figure>

Files will still be stored in the system after the project is closed, which makes it convenient to continue using them next time. Overall, the experience of Amazon SageMaker Studio Lab is basically the same as the native JupyterLab.

## 2 Other related learning resources

Amazon SageMaker Studio Lab displays some reference projects on the project homepage, such as `Dive into Deep Learning (D2L)`, `Hugging Face`, etc. These are all excellent learning resources. You can click to copy the project to your own file system and practice.

Among them, `Dive into Deep Learning (D2L)` is led by Amazon's `Sr. Principal Scientist Li Mu` (also known as Mu Li), and Mu Li offers free courses on deep learning on multiple platforms:

- The e-book "Dive into Deep Learning": https://d2l.ai/
- Bilibili @Learning AI with Li Mu: https://space.bilibili.com/1567748478/channel/seriesdetail?sid=358497

If you are interested, you can go to the corresponding platform to learn and practice! I hope this sharing is helpful to you, and I welcome you to discuss it in the comments section!

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>