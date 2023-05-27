---
template: overrides/blogs.html
tags:
  - python
  - automation
---

# Build a Taobao Robotic Purchasing Tool in Two Minutes

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan)、Void; Published on 2021-06-08; Read time: about 4 minutes; WeChat Public Account Article Link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/du-t9DyeC2INQsXg1m1xOQ)

## 1 Pain Points

Major eCommerce websites offer promotional activities on specific days, such as 618 and Singles' Day. Sometimes, you need to be alert to snap up limited-release products. However, is your success rate high? Do you often encounter situations where the app is always loading, and after refreshing, you find that a product has been snapped up before you? The fact is that many of your competitors who compete for the same products are faster and more accurate than you because they can execute commands precisely with a `robot`.

Are you frustrated? It doesn't matter. This article will teach you how to build a robot of your own from scratch. It will automatically place orders at the set time, and you will no longer worry about missing your favorite products!

## 2 Preparation

Before building a robot, please make sure you have the following tools:

- **A computer**: it doesn't need to be fast or new, just anything that works.
- **Chrome browser**: the robot will complete the automatic purchasing process on Chrome.
- **Python programming environment**: Don't worry; you don't need to know how to code because the code has been written for you. However, you need to install software that can run it, so you need to configure the Python programming environment. Windows and Mac users should configure it according to their corresponding methods.

!!! example "Configure the Python Programming Environment"

    === "Configure Python on Windows"

        The following steps apply to Windows systems.

        Anaconda is an open-source Python distribution that integrates Python and numerous scientific packages.

        - Step 1: Download the Windows version of Anaconda's [64-Bit Graphical Installer](https://www.anaconda.com/products/individual-b)
        - Step 2: Install Anaconda
        - Step 3: Open Anaconda Navigator and click `Launch Notebook` or `JupyterLab`.

        Then you'll see this screen:

        <figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="600" />
          <figcaption>Jupyter Lab</figcaption>
        </figure>

        In the Notebook area on the right, add a Notebook and use the code below to build a robot!

    === "Configure Python on Mac"

        The following steps apply to Intel Mac and M1 Mac.

        - Step 1: Open Terminal (command + space activate Spotlight, and enter Terminal)
        <figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623155498233-image.png" width="600" />
          <figcaption>Terminal</figcaption>
        </figure>

        - Step 2: Enter `pip3 install jupyter`
        - Step 3: Enter `pip3 install jupyter-lab`
        - Step 4: Enter `jupyter lab`

        Then you'll see this screen:

        <figure>
          <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-8/1623156140452-Jupyter_lab_blur.png" width="500" />
          <figcaption>Jupyter Lab</figcaption>
        </figure>

        In the Notebook area on the right, add a Notebook and use the code below to build a robot!

## 3 Code

!!! tip
    Run the following code in the Notebook you created.

### 3.1 Download the Required Packages

```python
# Selenium is commonly used for Web testing automation. Here we will use it to automate the Taobao purchasing process.
!pip install selenium
```

```python
!which python
```

The above code returns `/opt/anaconda3/bin/python`. We will use this address in the following steps.

### 3.2 Download the Auxiliary Program

- Check the version of your Chrome browser (you can see the software version by entering "About Chrome").
- Go to the [official download site of ChromeDriver](https://chromedriver.storage.googleapis.com/index.html) and download the version that matches your Chrome browser. Then, place the file in the `/opt/anaconda3/bin` folder.


```python
from selenium import webdriver
import datetime
import time
```

Quick Tip: you can use the following time code to quickly set the purchasing time

```python
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(now)
```

Output: 2021-06-18 00:00:00.000000

### 3.3 Parts of the Robot

```python
def login():
    # Open the Taobao homepage and log in via QR code
    browser.get("https://www.taobao.com")
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("Please log in quickly via QR code")
    time.sleep(10)

def picking():
    # Open the shopping cart list page
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    # method = 0 selects all items in the shopping cart
    method = 0
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print("Could not find the purchase button.")
    # method = 1 manually selects items
    else:
        print("Please manually select the items you want to purchase")
        time.sleep(5)

#Wait for the purchasing time and initiate automatic purchasing. Here we define a buy function
def buy(order_time, browser):
    print(order_time)

    order_placed_status = False
    while order_placed_status != True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # Check the time and click "checkout" when the time arrives
        if now >= order_time:
            browser.refresh()
            picking(browser)
            
            # Click "checkout"
            while True:
                clear_element = WebDriverWait(browser, 10).until(
                            EC.element_to_be_clickable((By.LINK_TEXT, "结 算"))
                        )
                try:
                    if browser.find_element_by_link_text("结 算").is_enabled():
                        browser.find_element_by_link_text("结 算").click()
                        clear_element.click()
                        print("Checkout was successful. Preparing to submit the order")
                        break
                except:
                    pass

            order_element = WebDriverWait(browser, 20).until(
                            EC.element_to_be_clickable((By.LINK_TEXT, "提交订单")))
            # Click "submit order"
            order_element.click()
            order_placed_status = True

            time.sleep(0.01)
```

### 3.4 Launch the Robot

```python
browser = webdriver.Chrome()
login()
picking()
```

### 3.5 Schedule Automatic Purchasing

```python
order_time = input("Please enter the purchasing time (format: 2021-06-08 19:30:00.000000):")
```

e.g., Please enter the purchasing time (format: 2021-06-08 19:30:00.000000):2021-06-08 19:55:00.000000

```python
buy(order_time, browser)
```

## 4 Final Effect

Please refer to the WeChat public account article for a video demonstrating the tool's functionality: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/du-t9DyeC2INQsXg1m1xOQ)

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>