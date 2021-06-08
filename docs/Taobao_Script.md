# 下载一些需要的包


```python
# Selenium 常用于网页的自动化测试，在此我们借助它自动化淘宝下单的过程
!pip install selenium
```

    Collecting selenium
      Using cached selenium-3.141.0-py2.py3-none-any.whl (904 kB)
    Requirement already satisfied: urllib3 in /opt/anaconda3/lib/python3.8/site-packages (from selenium) (1.25.11)
    Installing collected packages: selenium
    Successfully installed selenium-3.141.0



```python
!which python
```

    /opt/anaconda3/bin/python


# 前提: 
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

    2021-06-08 19:24:15.897631



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


```python
browser = webdriver.Chrome()
login()
picking()
```


```python
times = input("请输入抢购时间，格式如(2021-06-08 19:30:00.000000):")
```

    请输入抢购时间，格式如(2021-06-08 19:30:00.000000): 2021-06-08 19:55:00.000000



```python
buy(times)
```


```python

```
