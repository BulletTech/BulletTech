---
template: overrides/blogs.html
tags:
  - machine learning
---

# 决策树学习笔记

!!! info
    Author:：[Vincent](https://github.com/Realvincentyuan)，Posted on 2021-08-28，Reading time: 6 mins，WeChat Post Link:：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/waV7HG3KWs-Qx574aUHj3Q)

## 1 Introduction


Decision tree is a very classic machine learning model. Many classifications and regression problems in daily work can be solved by decision trees. Many more advanced and advanced machine learning models are also based on decision -making trees. In order to consolidate the foundation and use the decision -making tree correctly, todayLet's review the most important technical details in some decision trees.


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-28/1630120948129-iris_tree.png"  />

<FIGCAPTION> Classification Decision Tree Example </Figcaption>
</figure>




## 2 Algorithm important details


### 2.1 How to make predictions


The decision tree with a depth of 2 in the example shows the process and conclusion of making decisions. For 150 sample points, at the root node, whether the petal length is less than 2.45 cm, the data is divided into two parts, and the petals lengthSamples less than 2.45 cm are classified into SetOSA, and data greater than 2.45 cm continues whether the petal width (Petal Width) is less than 1.75 cm. The less part is considered to be Versicolor, and the part is Virginica.


The Samples in the figure is the number of samples in this large category, such as SAMPLES = 50 in the left leaf node with a depth of 1 means 50 samples with petal length (Petal Length) less than 2.45 cm.Value represents the distribution of training data in the current node. For example, in the left green node with depth 2 [0, 49, 5] indicates that in this node, there are 0 Setosa, 49 Versicolor and 5 Virginica, a total of 54 of 54Samples.


### 2.2 The basis for prediction


In the example's decision tree, an important indicator is called the `Gini -Curvit coefficient`. This coefficient measures the impurities of the current node. In intuitive, when all the samples in a node belong to the same category,, The pureness of the node is the highest, the Gini coefficient is 0.The definition of `gini` is


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-28/1630138292390-gini.png"  />

<figcaption>Gini</figcaption>
</figure>


Among them, $ p_ {i, k} $ is the proportion of the overall sample of the category K in the node.For example, the `gini` of the right node with a depth of 2 in the example is $ 1- (0/46)^{2}-(1/46)^{2}-(45/46)^{2} ~ = 0.043 $EssenceIn the most commonly used Python machine learning library `Scikit-Learn (V0.24.2)`
[DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)
As an example, when the Classification and Regression Tree (CART) is implemented, in the process of choosing a split node, the basis for the selection of split nodes and thresholds of the decision tree is related to the `Gini`.Its optimization target (loss function) is shown below:


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630206173092-CART_Loss.png"  />

<figcaption> CART Classification Loss Function </Figcaption>
</figure>


Among them, $ g_ {left/right} $ are the `gini` of the left and right nodes, and $ m_ {left/right} $ are the number of samples on the left and right nodes, respectively.CART algorithm will make greedy search, start from the root node, and search in layer nodes can effectively reduce the characteristics and thresholds of `gini` until the number of divisions reached the maximum depth (defined by the MAX_DEPTH parameter)Or can no longer be found nodes that can reduce `gini`.Inlea, finding the best tree is one
[NP-Pintete](https://zh.
The problem, so the algorithm will only find a relatively good solution instead of the best solution.


In addition to `gini`, Entropy can also be used to measure the effect of dividing nodes to measure the confusion. In the node of the decision tree, when the samples in a node belong to the same category, the value of the entropy is the value of the entropy is the value of the entropy is the value0.The definition is as follows:


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630205324586-Entropy.png"  />

<figcaption>熵（Entropy）</figcaption>
</figure>


Among them, $ p_ {i, k} $ is the proportion of the overall sample of the category K in the node.For example, the entropy of the right node with a depth of 2 in the example is $- (1/46) log_ {2} (1/46)-(45/46) log_ {2} (45/46) ~ = 0.151 $.When using the `decisionTreeClassifier` class in the` Scikit-Learn (v0.24.2) `, you can use the entropy as a measurement indicator by setting the` CRITERION` parameter as the `Entropy`.However, the trees obtained by `gini` and` Entropy` are not much different.The main difference is that the calculation of `gini` is faster, and the use of` gini` will make the tree divide the samples more concentrated into the node, and the use of `Entropy` will make the samples more balanced in the distribution of the tree.


### 2.3 Prevent overfitting


The decision tree itself has almost no assumptions, and does not depend on Feature Scaling, but the model itself needs to be restrained to prevent overfitting.Can achieve the purpose of regularization by controlling the model parameters.Take the `decisionTreeClassifier` class as an example in the` Scikit-Learn (V0.24.2) `` `DecisionTreeClassifier` class. The following parameters are often used to implement regularization to prevent overfitting:


- ** max_depth **: The maximum depth of the tree, the default value is empty, which means that the maximum depth of the tree is not limited.
- ** min_samples_split **: The minimum sample required before dividing a node, the default value is 2.
- ** min_samples_leaf **: The minimum number of samples required for a leaf node, the default value is 1.
- ** min_weight_fraction_leaf **: The default value is 0.After the `Class_weight` is set, the sample weight is different, and the parameter restricts the proportion of the weight of the overall sample in the leaf nodes. The meaning is similar to the` min_samples_leaf`, but it is represented by the proportion.
- ** max_feature **: The number of features considers in the split node, default to consider all features.Note that the decision tree will not stop searching before finding an effective split node.
- ** max_leaf_nodes **: The upper limit of the number of leaves nodes, the default value is empty.
- ** min_impurity_decrease **: The minimum impureness required to split a node, the default value is 0.


Generally, increasing the min_ parameter or reduction of the MAX_ parameter helps the regularization of the decision tree.


### 2.4 Return to task


It can
[DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor)
Class to perform the regression mission.




<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630228541305-iris_reg_tree.png"  />

<figcaption> Return </figcaption>
</figure>


At this time, the predictive value is the mean value of the sample target value in the leaf node.When doing the regression mission, the implementation method of the CART algorithm is basically the same as the classification. However, the optimized goal at this time is to reduce the equalization of the target value (MEAN SQUARED ERROR, MSE)


<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-8-29/1630229474823-CART_regression_loss.png" />

<figcaption> Loss of Return Tree </figcaption>
</figure>


The return tree model parameters are basically consistent with the classification number model parameters, and can prevent the model from overfitting through similar methods.


### 2.5 Other important attributes


In the implementation of the `scikit-asln`, the importance of the decision tree's` feature_importances_` The importance of the attribute performance display feature is the basis for the reduction of the value of each characteristic to measure the indicator, and the value of the return after returnees.If the number of different values in the features is very large (high number category attributes, high cardinality features), it is recommended to use
[sklearn.inspection.permutation_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance)
。


If you want to manually adjust the tree, such as changing the split threshold, you can use it
[sklearn.tree._tree.Tree](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py)
。


## 3 Summary


The decision -making tree should have a good performance of classification and regression issues, but there are also some restrictions and weaknesses. If the directionality and fluctuations of the data are more sensitive, these problems are difficult to solve perfectly.What about the performance?Next time we talk about random forests!


Example code:


```python
# 依 依 依
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz


import matplotlib.pylab as plt
import numpy as np




#
iris = load_iris()
X = Iris.data [:,: 2] # Select the length of the petals and the width of petals as a characteristic
y = iris.target


# View data distribution
plt.scatter(X[y==0,0], X[y==0,1])
plt.scatter(X[y==1,0], X[y==1,1])
plt.scatter(X[y==2,0], X[y==2,1])
plt.show()


#
tree_clf = DecisionTreeClassifier(criterion='entropy', max_depth=2)
tree_clf.fit(X, y)


# Export decision tree graphics
export_graphviz( tree_clf,
out_file="iris_tree.dot",
feature_names=iris.feature_names[:2],
class_names=iris.target_names,
rounded=True,
filled=True
)


# Decision -border drawing function
def plot_decision_boundary(model, x):
#Generate a grid point coordinate matrix to get two matrices
M, N = 500, 500
x0, x1 = np.meshgrid(np.linspace(x[:,0].min(),x[:,0].max(),M),np.linspace(x[:,1].min(),x[:,1].max(),N))
X_new = np.c_[x0.ravel(), x1.ravel()]
y_predict = model.predict(X_new)
z = y_predict.reshape(x0.shape)
from matplotlib.colors import ListedColormap
custom_cmap = ListedColormap(['#EF9A9A','#FFF59D','#90CAF9'])
plt.pcolormesh(x0, x1, z, cmap=custom_cmap)


# Decision boundary
plot_decision_boundary(tree_clf, X)
plt.scatter(X[y==0,0], X[y==0,1])
plt.scatter(X[y==1,0], X[y==1,1])
plt.scatter(X[y==2,0], X[y==2,1])
plt.show()


# View characteristic importance
print(tree_clf.feature_importances_)
```