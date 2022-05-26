---
template: overrides/blogs.html
tags:
  - machine learning
---

# 特征选择之Permutation Importance

!!! info
    作者：袁子弹起飞，发布于2021-06-06，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247485194&idx=1&sn=60a358eeed0c7fa7b2ebb362cce92a9b&chksm=eb90f47edce77d68bc54cd35d12a5530c9639250b19b469269f2e0559eeb81c5b2d0052e74a4&token=120973643&lang=zh_CN#rd)


## 1 前言

之前的文章中提到了一些常用的特征选择的技巧，本文继续针对这一话题进行研究，讲解一种新的检查特征重要性的方法：Permutation Importance。继续阅读前，可先阅读相关前文回顾知识：

- [决策树学习笔记](https://mp.weixin.qq.com/s/waV7HG3KWs-Qx574aUHj3Q)
- [如何做特征选择](https://mp.weixin.qq.com/s/Cuw1ugpxm-5lF_rUkAu56Q)

## 2 算法解构

Permutation Importance适用于表格型数据，其对于特征重要性的评判取决于该特征被随机重排后，模型表现评分的下降程度。其数学表达式可以表示为：

- 输入：训练后的模型m，训练集（或验证集，或测试集）D
- 模型m在数据集D上的性能评分s
- 对于数据集D的每一个特征j
  - 对于K次重复实验中的每一次迭代k，随机重排列特征j，构造一个被污染的数据集$Dc_{k,j}$
  - 计算模型m在数据集$Dc_{k,j}$上的性能评分$s_{k,j}$
  - 特征j的重要性分数$i_{j}$则可以记作

$$ i_{j} = s - \frac{1}{K}\sum_{k=1}^{K}s_{k,j} $$

## 3 示例代码

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
diabetes = load_diabetes()
X_train, X_val, y_train, y_val = train_test_split(
    diabetes.data, diabetes.target, random_state=0)

model = Ridge(alpha=1e-2).fit(X_train, y_train)
model.score(X_val, y_val)


scoring = ['r2', 'neg_mean_absolute_percentage_error', 'neg_mean_squared_error']
# scoring参数可以同时加入多个计算指标，这样比重复使用permutation_importance更有效率，因为预测值能被用来计算不同的指标
r_multi = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0, scoring=scoring)

for metric in r_multi:
    print(f"{metric}")
    r = r_multi[metric]
    for i in r.importances_mean.argsort()[::-1]:
        if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
            print(f"    {diabetes.feature_names[i]:<8}"
                  f"{r.importances_mean[i]:.3f}"
                  f" +/- {r.importances_std[i]:.3f}")

```

输出为：

```python
r2
  s5      0.204 +/- 0.050
  bmi     0.176 +/- 0.048
  bp      0.088 +/- 0.033
  sex     0.056 +/- 0.023
neg_mean_absolute_percentage_error
  s5      0.081 +/- 0.020
  bmi     0.064 +/- 0.015
  bp      0.029 +/- 0.010
neg_mean_squared_error
  s5      1013.903 +/- 246.460
  bmi     872.694 +/- 240.296
  bp      438.681 +/- 163.025
  sex     277.382 +/- 115.126
```

## 4 总结

相比而言，树模型通常基于不纯净度的下降来判断特征重要性，该重要性通常是基于`训练集`的，当模型过拟合时，特征的重要性则具有误导性。在此情况下，看似重要的特征可能对于模型上线后的遇到的新数据并没有令人满意的预测能力。

同时，基于不纯净度的特征重要性容易受到高数量类别属性的影响（High Cardinality Features），所以那些数值型变量往往排名靠前。而Permutation Importance对模型的特征没有偏见，也不局限于特定的模型类别，适用性较广。请注意。如果特征有较强的多重共线性，建议只取一个重要的特征，方法可查看[示例](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-multicollinear-py 'Permutation Importance with Multicollinear or Correlated Features')。

同时，`Scikit Learn`还提供了一个直观的[示例](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py 'Permutation Importance vs Random Forest Feature Importance (MDI)')展现基于不纯净度的特征重要性和Permutation Importance的区别。

希望这次的分享对你有帮助，欢迎在评论区留言讨论！

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
