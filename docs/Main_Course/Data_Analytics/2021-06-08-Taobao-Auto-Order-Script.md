---
template: overrides/blogs.html
---

# 淘宝自动定时下单机器人

!!! info 
    作者：袁子弹起飞、Void，发布于2021年6月8日，阅读时间：约6分钟

## 1 痛点

各大电商网站在一些特定的日子都会开启促销活动，如618、双十一等，有时还得盯着时间抢限量发售的商品，但你的成功率高吗?是否经常会遇到App一直加载，刷新后发现商品被一扫而光了？事实是，很多和你竞争抢购商品的对手比你的手更快更准，因为他们很多都是能精准执行命令的`机器人`。

气不气？没关系这篇文章将手把手教你零基础建设一个自己的机器人，帮你在设定好的时间自动下单，再也不用为抢不到心爱的宝贝烦恼了！

## 2 准备工作

在建设机器人之前，请确保你准备好了如下工具：

- **一台电脑**：不需要多快多新，能用就行
- **Chrome浏览器**：机器人将在Chrome上完成自动下单的工作
- **Python编程环境**：别怕，你不需要会编程，代码已经帮你写好了。但你需要安装一个软件能让它跑起来，所以需要简单配置一下python的编程环境。Windows和Mac用户，请按照相对应的方式配置。

!!! example "配置Python的编程环境"

    === "Windows 配置Python"

        Anaconda是一个开源的Python发行版本，集成了Python和众多科学包。
        
        - 第一步：下载Anaconda Windows版本的[64-Bit Graphical Installer](https://www.anaconda.com/products/individual-b)
        - 第二步：安装Anaconda
        - 第三步：打开Anaconda Navigator，点击Launch Notebook或JupyterLab
        
        然后你会看到这样的画面：
        
        <figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="500" />
          <figcaption>Jupyter Lab</figcaption>
        </figure>
        
        看到右侧的Notebook区域，添加一个Notebook，然后使用下面的代码打造机器人！

    === "Mac 配置Python"
        
        下列步骤适用于Intel Mac和M1 Mac。
        
        - 第一步：打开终端（command + space 激活Spotlight，输入Terminal）
        
        <figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623155498233-image.png" width="500" />
          <figcaption>终端Terminal</figcaption>
        </figure>
        
        
        - 第二步：输入`pip3 install jupyter`
        - 第三步：输入`pip3 install jupyter-lab`
        - 第四步：输入`jupyter lab`
        
        然后你会看到这样的画面：
        
        <figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="500" />
          <figcaption>Jupyter Lab</figcaption>
        </figure>
        
        看到右侧的Notebook区域，添加一个Notebook，然后使用下面的代码打造机器人！
        


## 3 代码

!!! tip
    以下代码请在你刚才创建的Notebook中运行。

### 3.1 下载需要的程序包

```python
# Selenium 常用于网页的自动化测试，在此我们借助它自动化淘宝下单的过程
!pip install selenium
```

```python
!which python
```
上面的代码返回了/opt/anaconda3/bin/python，接下来就要用到这个地址。

### 3.1 下载一个小配件
- 查看自己Chrome浏览器的版本(进入`关于Chrome`即可看到软件版本)
- 前往[ChromeDriver的官方下载地址](https://chromedriver.storage.googleapis.com/index.html)下载对应版本的chrome driver后，放在此```/opt/anaconda3/bin``` 文件夹里


```python
from selenium import webdriver
import datetime
import time
```

小技巧：这个时间可以用来快速设定抢购时间


```python
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(now)
```

2021-06-18 00:00:00.000000

### 3.3 机器人的零件

```python
def login():
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com")
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print(f"请尽快扫码登录")
    time.sleep(10)
```

```python
def picking():
    # 打开购物车列表页面
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # method = 0全选购物车
    method = 0
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print(f"找不到购买按钮")
    #method = 1 手动勾选
    else:
        print(f"请手动勾选需要购买的商品")
        time.sleep(5)
```


```python
#等待抢购时间，定时秒杀，这里我们定义一个buy函数
def buy(times):
    print(times)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print(f"抢购成功，请尽快付款")
                except:
                    print(f"再次尝试提交订单")
            time.sleep(0.01)
```


### 3.4 启动机器人

```python
browser = webdriver.Chrome()
login()
picking()
```

### 3.5 定时下单

```python
order_time = input("请输入抢购时间，格式如(2021-06-08 19:30:00.000000):")
```

请输入抢购时间，格式如(2021-06-08 19:30:00.000000): 2021-06-08 19:55:00.000000

```python
buy(order_time)
```

## 4 最终效果

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="450" />
  <figcaption>自动抢单</figcaption>
</figure>
