# Obtaining rental housing data

!!! info
    Author: Echo, published on 2021-12-04, Reading time: about 6 minutes, WeChat Official Account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/NHgnYaelpcDKYWnAqL6vSw)

## 1 Introduction

Attention all folks who rent or have houses for rent~

Food, clothing, shelter, and transportation are the basic needs of life. Clothing and food are easy to deal with - you can buy new clothes and switch to a different restaurant if the food isn't good. But when it comes to housing, the cost of buying or renting a house is relatively high, which is why choosing the right place to live is so important. As a person who cannot currently afford to buy a house, I typically rely on real estate agents to help me find a rental, such as Ziroom, Beike, and Lianjia. Just like how Tieling is the end of the universe, Lianjia is the end of the road for finding a rental...Lianjia dominates the rental market and provides relatively fair information. However, when I scroll through more than ten houses, I can't remember all the information about each one, nor can I compare them visually. So let's get started and use the all-powerful Python to make Lianjia feel like your home, and obtain the information you want from Lianjia's website (this is not an advertisement)!

## 2 Obtaining Housing Data

In this section, we will focus on the use of XPath and anti-spider techniques. XPath is an expression in the path language used to select nodes from an XML document, which can also be used to search HTML documents.

### 2.1 Determining the URL

Open the rental page on the Lianjia website