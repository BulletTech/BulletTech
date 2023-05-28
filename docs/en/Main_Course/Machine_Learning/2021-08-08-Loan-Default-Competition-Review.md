---
template: overrides/blogs.html
tags:
  - machine learning
---

# Summary of Tianchi Zero-based Financial Risk Control Competition

!!! info
    Author: Jeremy, posted on 2021-08-08, reading time: about 12 minutes, WeChat public account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/dvHbk5NaKz4a15oke3FXkA)

## 1 Background

Last September, I participated in the Zero-based Introduction to Financial Risk Control-Loan Default Prediction Competition hosted by Tianchi. The competition was set against the background of personal credit in financial risk control. Participants were required to predict the possibility of default based on the information of loan applicants to determine whether to pass the loan. This is a typical classification problem.

## 2 Data

The competition data comes from loan records of a certain credit platform, with a total volume of 1.2 million. The training set, Test set A, and Test set B each have 800,000, 200,000, and 200,000 data. The original data contains 47 columns of variable information, mainly including: loan information (amount, interest rate, loan grade, etc.), borrower information (employment information, income information, debt ratio, FICO (a credit score), loan record, etc.), and anonymous feature information of borrower behavior counts. You can visit the [competition official website](https://tianchi.aliyun.com/competition/entrance/531830/information)"competition official website" to query the complete field table, or click **Read the original article** to view the article on our blog.

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| id                 | Unique credit certificate identification assigned to the loan list|
| loanAmnt           | Loan amount                                                     |
| term               | Loan term (year)                                                |
| interestRate       | Loan interest rate                                              |
| installment        | Installment payment amount                                      |
| grade              | The level of the loan                                           |
| subGrade           | The subordinate level of the loan level                          |
| employmentTitle    | Employment title                                                |
| employmentLength   | Employment length (years)                                        |
| homeOwnership      | The housing ownership status provided by the borrower at