---
template: overrides/blogs.html
---

# 读《30天吃掉那只TensorFlow2》

!!! info
    作者：Void，发布于2021-12-01，阅读时间：约6分钟，微信公众号文章链接：[:fontawesome-solid-link:](https://mp.weixin.qq.com/s/z2uBxwe8UNDXWMDNS_k-Gg)

## 1 前言

在工作中，需要使用TensorFlow来构建模型(由于不断内卷，需要模型又Fancy效果又好)。碰到问题，搜索他人的回答或是TensorFlow的官方文档是解决问题的高效方法。但是面向搜索引擎编程，不免觉得获取的知识有点破碎。  

为了构建一个较为完整的TensorFlow的知识体系，而又不一上来就陷入官方文档难以自拔，作者找到了《30天吃掉那只TensorFlow2》这一关于TensorFlow的[开源工具书](https://jackiexiao.github.io/eat_tensorflow2_in_30_days/chinese/ '30天吃掉那只TensorFlow2')。  

这一项目不仅提供了文档，还提供了环境，可以直接运行示例。事实上，有一定基础的读者也并不需要30天就能完成阅读。有一定基础，想快速构建TensorFlow知识体系的读者不妨吃下这颗安利。

## 2 建模流程

本书首先给出了常见任务应用TensorFlow的建模流程，包括结构化数据、图片、文本、时间序列数据。具体的技术细节可以先不做理会，如LSTM、CNN等，这一部分只是为了展示TensorFlow使用场景广、可以应用于主流的不同任务。

## 3 核心概念

这一部分介绍了TensorFlow的核心组成：张量，计算图以及自动微分。  

张量可以理解为多维数组，是TensorFlow中的基本数据结构。  

计算图就是整个计算关系。TensorFlow1.0采用的是静态计算图，在创建完计算图后，需要开启一个session才会显式执行。进入TensorFlow2.0后，为了方便调试，TensorFlow采用了动态计算图。由于动态计算图效率会低一些，TensorFlow允许我们使用@tf.function装饰器构建静态计算图，也被称作Autograph。  

神经网络在更新权重时，很重要的一步是求解梯度。TensorFlow提供了tf.GradientTape(梯度磁带)，使我们可以很方便的求解梯度，更新网络。

## 4 层次结构

第三部分介绍了TensorFlow的层次结构，主要是低、中、高三阶的api示例。  
低阶api直接操作张量、计算图和自动微分。虽然显得有些复杂和原始，但是是我们离开新手村，自定义模型时不可获取的知识点。

如定义模型：

```python
w = tf.Variable(tf.random.normal(w0.shape))
b = tf.Variable(tf.zeros_like(b0,dtype = tf.float32))

# 定义模型
class LinearRegression:     
    #正向传播
    def __call__(self,x): 
        return x@w + b

    # 损失函数
    def loss_func(self,y_true,y_pred):  
        return tf.reduce_mean((y_true - y_pred)**2/2)

model = LinearRegression()
```

中阶api提供了更高程度的封装，如损失函数、优化器等组件。

```python
model = layers.Dense(units = 1) 
model.build(input_shape = (2,)) #用build方法创建variables
model.loss_func = losses.mean_squared_error
model.optimizer = optimizers.SGD(learning_rate=0.001)
```

我们只需要选择想要的优化器，调节学习速率即可。并不需要关心优化器本身是如何实现的。这些小组件给我们的建模提供了很多便利。

高阶api主要是模型类的接口。主要包括以下三点：

- 序列化模型
    ```python
    model = models.Sequential()
    model.add(layers.Dense(1,input_shape =(2,)))
    model.summary()
    ```
- 函数式api
    ```python
    input_tensor = Input(shape=(64, ))
    z = layers.Dense(32, activation='relu')(input_tensor)
    z = layers.Dense(32, activation='relu')(z)
    y = layers.Dense(10, activation='softmax')(z)
    from keras.models import Model
    model = Model(input_tensor, y)
    ```
- 继承Model基类，自定义模型
    ```python
    class DNNModel(models.Model):
        def __init__(self):
            super(DNNModel, self).__init__()

        def build(self,input_shape):
            self.dense1 = layers.Dense(4,activation = "relu",name = "dense1") 
            self.dense2 = layers.Dense(8,activation = "relu",name = "dense2")
            self.dense3 = layers.Dense(1,activation = "sigmoid",name = "dense3")
            super(DNNModel,self).build(input_shape)

        # 正向传播
        @tf.function(input_signature=[tf.TensorSpec(shape = [None,2], dtype = tf.float32)])  
        def call(self,x):
            x = self.dense1(x)
            x = self.dense2(x)
            y = self.dense3(x)
            return y

    model = DNNModel()
    model.build(input_shape =(None,2))

    model.summary()
    
    ```
## 5 api

最后是低、中、高阶api具体的介绍。感兴趣的读者可以自行阅读。有示例、有中文，读起来感觉轻松又愉快。

## 6 总结

《30天吃掉那只TensorFlow2》这本工具书可以让我们很快对TensorFlow建立起知识框架。内容不会太多，深度也足够。适合有一定基础，又想进一步了解TensorFlow的读者。

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
