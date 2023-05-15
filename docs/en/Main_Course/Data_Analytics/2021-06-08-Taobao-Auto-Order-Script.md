---
template: overrides/blogs.html
tags:
  - python
  - automation
---

# 两 mins打造淘宝抢单机器人

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)、Void，Posted on 2021-06-08，Reading time: 4 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/du-t9DyeC2INQsXg1m1xOQ)

## 1 pain point


Major e -commerce websites will start promotional activities on some specific days, such as 618 and Double Eleven, and sometimes have to stare at the time -limited sale products, but are your success rate?After loading, after refreshing, I found that the product was swept away?The fact is that many opponents who are competing with you to buy products are faster and more accurate than your hands, because many of them are `robots that can accurately execute orders.


Must be angry?It doesn't matter. This article will teach you to build your own robot with zero infrastructure to help you place an order automatically at the set time. You don't have to worry about the baby who can't grab your beloved!


## 2 Preparation


Before building a robot, make sure you prepare the following tools:


- ** A computer **: No need to be more fast and new, you can use it
- ** chrome browser **: The robot will complete the automatic ordering work on chrome
- ** Python programming environment **: Don't be afraid, you don't need to be programmed, the code has been written for you.But you need to install a software to run it, so you need to simply configure the Python programming environment.Windows and Mac users, please configure according to the corresponding manner.


!!! Example "Configure the programming environment of python" "


=== "Windows configuration python"


The following steps are suitable for Windows system.


Anaconda is an open source Python distribution version that integrates Python and many scientific packages.


-Step 1: Download Anaconda Windows version
[64-Bit Graphical Installer](https://www.anaconda.com/products/individual-b)
-Step 2: Install Anaconda
-Step 3: Open Anacondda Navigator, click Launch Notebook or Jupyterlab


Then you will see such a picture:


<figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="600" />

<figcaption>Jupyter Lab</figcaption>
</figure>


See the Notebook area on the right, add a notebook, and then use the following code to create a robot!


=== "mac configuration python"


The following steps are suitable for Intel Mac and M1 Mac.


-Step 1: Open the terminal (Command + Space to activate SpotLight, enter terminal)


<figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623155498233-image.png" width="600" />

<figcaption> Terminal Terminal </figcaption>
</figure>




-Step 2: Enter `PIP3 Install Jupyter`
-Step 3: Enter the `PIP3 Install Jupyter-Lab`
-Fied Step 4: Enter the `Jupyter Lab`


Then you will see such a picture:


<figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="500" />

<figcaption>Jupyter Lab</figcaption>
</figure>


See the Notebook area on the right, add a notebook, and then use the following code to create a robot!






## 3 code


!!! tip
The following code is running in the Notebook you just created.


### 3.1 Download the required program package


```python
#Slenium is commonly used for the automation test of the webpage. Here we use the process of automation Taobao to place an order
!pip install selenium
```


```python
!which python
```
The above code returns/OPT/Anaconda3/Bin/Python, and this address will be used next.


### 3.2 Download a small accessory
-Chat version of your Chrome browser (enter the software version about chrome` to see the software version)
-The
[Official download address of chromedriver]
After downloading the corresponding version of Chrome Driver, put it here `` ``/opt/anaconda3/bin```




```python
from selenium import webdriver
import datetime
import time
```


Tips: This time can be used to quickly set up buying time




```python
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(now)
```


2021-06-18 00:00:00.000000


### 3.3 Robot parts


```python
def login():
# Open Taobao Homepage, log in with code scanning
browser.get("https://www.taobao.com")
if browser.find_element_by_link_text ("dear, please log in"):
browser.find_element_by_link_text ("dear, please log in") .CLick ().
Print (f "please scan the code as soon as possible"))
time.sleep(10)
```


```python
def picking():
# Open the shopping cart list page
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)
# METHOD = 0 All -choice shopping cart
method = 0
if method == 0:
while True:
try:
if browser.find_element_by_id("J_SelectAll1"):
browser.find_element_by_id("J_SelectAll1").click()
break
except:
Print (F "can't find the purchase button")
#Method = 1 manually checked
else:
Print (f "please check the goods you need to buy manually"))
time.sleep(5)
```




```python
#Waiting for the purchase time, timing spike, here we define a buy function
def buy(order_time, browser):
print(order_time)


order_placed_status = False
while order_placed_status != True:
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# Comparison time, click settlement if time arrives
if now >= order_time:
browser.refresh()
picking(browser)
# Click the settings button


while True:
clear_element = WebDriverWait(browser, 10).until(
EC.element_to_be_clickable((By.LINK_TEXT, "结 算"))
)
try:
if browser.find_element_by_link_text("结 算").is_enabled():
browSer.find_element_by_Link_text ("Calculation") .clICK ().
clear_element.click()
Print (f "settled successfully, ready to submit orders"))
break
except:
pass


order_element = WebDriverWait(browser, 20).until(
Ec.element_to_be_clickable (by.link_text, "Submit order")))
# Click to submit the order button
order_element.click()
order_placed_status = True


time.sleep(0.01)
```




### 3.4 Start the robot


```python
browser = webdriver.Chrome()
login()
picking()
```


### 3.5 Plus order regularly


```python
Order_time = Input ("Please enter the snap-up time, the format is (2021-06-08 19: 30: 00.000000):")
```


Please enter the purchase time, the format is (2021-06-08 19: 30: 00000000): 2021-06-08 19: 55: 00000000


```python
buy(order_time, browser)
```


## 4 The final effect


Please move the WeChat public account article to view the carefully made small videos:
[:Fontawesome-solid-link:](https://mp.weixixin.QQ.com/s/du-t9dyec2inqxxg1m1m1m1m


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />

</figure>