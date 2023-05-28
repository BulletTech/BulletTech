---
template: overrides/blogs.html
tags:
  - machine learning
---

# Uplift Model in Causal Inference

!!! info
    Author: Echo, published on 2022-02-03, reading time: about 6 minutes, WeChat public account article link: [:fontawesome-solid-link:]()

## 1 Background

During the Chinese New Year stay-at-home period, when chatting with my friends online, I found that we were all bombarded with the same game advertisement (since there are many ways to have fun, but the way to obtain joy beans is really single). My friend became the game's user after passively watching many 30-second ads. And I was moved by its marketing cost and decided to investigate the marketing strategy behind it.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/chat2223.jpg" width="400"/>
</figure>

Before we begin, let's review the four quadrants of users.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/用户四象限.png" width="500"/>
</figure>

The horizontal and vertical coordinates represent the user's purchase behavior with or without intervention, with intervention as an example of offering coupons:
- Persuadables: Intervention-sensitive users who only buy when given a coupon and won't buy if they don't get one.
- Sure things: Naturally converted users who will purchase regardless of whether they are offered a coupon.
- Lost causes: Granite-hearted users who won't buy whether or not you offer a coupon.
- Sleeping dogs: South-north style users who would buy without a coupon, and offering a coupon would instead deter them.

The purpose of offering coupons in the production environment is to increase the final conversion rate. The commonly used response model generally models whether or not to buy a product as the dependent variable to predict the probability of a user buying after giving them a coupon. However, this model focuses on correlation, only looking at whether the independent variable is correlated with the dependent variable, and cannot distinguish whether a user's purchase behavior is caused by the distribution of coupons. Therefore, it cannot identify the natural conversion crowd either and is unable to identify the utility of the coupons. Given that marketing incurs a cost, intervening in the intervention-sensitive user can reflect the role of the marketing activity, so a more effective estimate is to model the **causal effect** (increment) of an individual's behavior (e.g., purchase) regarding a certain treatment (intervention) with an increase model (Uplift Model). According to the three levels of causal relationships pointed out by Turing Award winner Judea Pearl, it is known that this is a counterfactual causal inference problem. Interested friends can refer to "The Book of Why: The New Science of Cause and Effect" for more detailed explanation.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/因果推断.png" width="500"/>
</figure>


## 2 Theoretical Basis

Let X be the user characteristics (e.g., gender, age, income), T be the treatment (with or without intervention, 1 for with, 0 for without), and Y be the dependent variable's result (e.g., click-through rate/conversion rate). Uplift Model aims to predict ITE (Individual Treatment Effect), which can be expressed as the difference in the conversion probability of a user when the intervention is given or not given, namely the difference between the treated and control groups' potential outcomes of independent samples. The objective of the Uplift Model is to maximize $\tau_{i}$. Considering that it is impossible to know the results of receiving and not receiving coupons for the same user at the same time (the counterfactual element), the model is thus heavily dependent on the assumption of conditional independence CIA(Conditional Independent Assumption), which requires that user characteristics and intervention policies are mutually independent.

$$
\left\{Y_{i}(1), Y_{i}(0)\right\} \perp T_{i} \mid X_{i}
$$

In actual applications, a random experiment can obtain samples of the experimental and control groups using intervention strategies, and the feature distributions of the two sample groups are consistent. Only under the CIA hypothesis, the expected value estimate of the causal effect of all samples can represent the overall users without bias. The conditional average intervention effect CATE(Conditional Average Treatment Effect) can be obtained, which is expressed as:

$$
\tau\left(X_{i}\right)=E\left[Y_{i}(1) \mid X_{i}\right]-E\left[Y_{i}(0) \mid X_{i}\right]=E\left[Y_{i}^{o b s} \mid X_{i}=x, T=1\right]-E\left[Y_{i}^{o b s} \mid X_{i}=x, T=0\right]
$$

where $Y_{i}^{o b s}=T_{i} Y_{i}(1)+\left(1-T_{i}\right) Y_{i}(0)$.

## 3 Model

### 3.1 Modified Tree Model

The traditional tree model's split rule is information gain. The objective is to maximize the difference in information before and after the split. The aim is to hope that the downstream nodes after feature splitting can distinguish people with higher and lower uplift. In other words, it is hoped that the positive and negative sample distributions between the experimental group and the control group inside the downstream nodes after splitting are more disparate than those of the upstream nodes. This difference can be measured by distance, such as KL divergence, Euclidean distance, chi-square distance, etc. The advantage of this method is that it directly models uplift more accurately. The disadvantage is that the model requires higher cost for reconfiguration.

### 3.2 Difference