# Notes on Decision Tree Learning

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan)，Published on August 28th, 2021, Reading time: about 6 minutes. WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/waV7HG3KWs-Qx574aUHj3Q)

## 1 Introduction

Decision tree is a very classic machine learning model that can be used to solve many classification and regression problems in daily work. Many more advanced machine learning models are also based on decision trees. To solidify the foundation and use decision trees correctly, today we will review some of the most important technical details of decision trees.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-28/1630120948129-iris_tree.png"  />
  <figcaption>Decision tree example for iris plant classification</figcaption>
</figure>


## 2 Important algorithm details

### 2.1 How to make predictions

In the example, the decision tree with a depth of 2 shows the process and conclusion of making decisions. For 150 sample points, the decision tree divides the data into two parts at the root node based on whether the petal length is less than 2.45 centimeters. The sample with a petal length of less than 2.45 centimeters is classified as Setosa, and the data with a petal width greater than 2.45 centimeters continues to be divided according to whether the petal width is less than 1.75 centimeters. The part less than the threshold is considered Versicolor, and the part greater than the threshold is considered virginica.

The samples in the figure represent the number of samples in this category. For example, the sample in the left leaf node with a depth of 1 has 50 `samples`, which means that there are 50 samples with a petal length less than 2.45 centimeters. The `value` represents the distribution of the training data in the current node. For example, the green node on the left of depth 2 represents that there are 0 setosa, 49 versicolor, and 5 virginica in the current node, with a total of 54 `samples`.

### 2.2 Basis for prediction

In the decision tree example, there is also an important indicator called `Gini impurity`, which measures the impurity of the current node intuitively. When all the samples in a node belong to the same category, the node has the highest purity and the Gini impurity is 0. The `Gini` is defined as follows:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-28/1630138292390-gini.png"  />
  <figcaption>Gini impurity</figcaption>
</figure>

Where $P_{i,k}$ is the proportion of the k-th class of samples in i nodes. For example, the `Gini` of the right node with a depth of 2 in the example is $1-(0/46)^{2}-(1/46)^{2}-(45/46)^{2} ~= 0.043$. Using the most commonly used Python machine learning library `Scikit-Learn(v0.24.2)` as an example, when implementing the Classification and Regression Tree (CART), the decision tree chooses the splitting node and threshold based on Gini impurity. The optimization objective (loss function) is shown below:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630206173092-CART