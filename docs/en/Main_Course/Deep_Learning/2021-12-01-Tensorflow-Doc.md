# Reading "30 Days to Eat TensorFlow2"

!!! info
    Author: Void, published on 2021-12-01, reading time: about 6 minutes, WeChat official account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/cw2DW7al5nJV93roAN_gwg)

## 1 Introduction

In work, TensorFlow is needed to build models (due to the need for fancy effects and good models). To solve problems, searching for other people's answers or TensorFlow's official documents is an efficient method. However, programming toward search engines inevitably leads to knowledge that is fragmented.

In order to build a more complete knowledge system of TensorFlow, and not to fall into the official documents at first sight, the author found "30 Days to Eat TensorFlow2", an open-source toolbook about TensorFlow, which not only provides documentation but also provides an environment that can directly run examples. In fact, readers with some foundation may not need 30 days to complete the reading. If you have a certain foundation and want to quickly build a TensorFlow knowledge system, you may want to have a look.

## 2 Modeling Process

This book first gives the modeling process of common tasks using TensorFlow, including structured data, images, text, and time series data. The specific technical details can be ignored for now, such as LSTM, CNN, and so on. This part is just to show that TensorFlow has a wide range of usage scenarios and can be applied to different mainstream tasks.

## 3 Core Concepts

This part introduces the core components of TensorFlow: tensors, computation graphs, and automatic differentiation.

Tensors can be understood as multidimensional arrays, which are the basic data structures in TensorFlow.

The computation graph is the overall computing relationship. TensorFlow 1.0 used a static computation graph. After creating the computation graph, you need to start a session to execute it explicitly. After entering TensorFlow 2.0, for ease of debugging, TensorFlow adopted a dynamic computation graph. Since the efficiency of the dynamic computation graph will be lower, TensorFlow allows us to use the @tf.function decorator to build a static computation graph, which is also called Autograph.

When updating the weights in a neural network, a very important step is to solve the gradient. TensorFlow provides tf.GradientTape, which enables us to easily solve the gradient and update the network.

## 4 Hierarchical Structure

The third part introduces the hierarchical structure of TensorFlow, mainly low-, medium-, and high-level API examples.

Low-level APIs directly manipulate tensors, computation graphs, and automatic differentiation. Although they may seem more complex and primitive, they are essential tools for us to leave the novice village and customize models.

For example, defining a model:

```python
w = tf.Variable(tf.random.normal(w0.shape))
b = tf.Variable(tf.zeros_like(b0,dtype = tf.float32))

# Define a model
class LinearRegression:     
    # Forward propagation
    def __call__(self,x):
        return x@w + b

    # Loss function
    def loss_func(self,y_true,y_pred):  
        return tf.reduce_mean((y_true - y_pred)**2/2)

model = LinearRegression()
```

The medium-level API provides a higher level of encapsulation, such as loss functions, optimizers, and other components.

```python
model = layers.Dense(units = 1)
model.build(input_shape = (2,)) # use the build method to create variables
model.loss_func = losses.mean_squared_error
model.optimizer = optimizers.SGD(learning_rate=0.001)
```

We only need to choose the optimizer we want and adjust the learning rate. We do not need to care about how the optimizer itself is implemented. These small components provide us with a lot of convenience for modeling.

The high-level API mainly consists of the model class interface. It mainly includes the following three points:

- Serialization model
    ```python
    model = models.Sequential()
    model.add(layers.Dense(1,input_shape =(2,)))
    model.summary()
    ```
- Functional API
    ```python
    input_tensor = Input(shape=(64, ))
    z = layers.Dense(32, activation='relu')(input_tensor)
    z = layers.Dense(32, activation='relu')(z)
    y = layers.Dense(10, activation='softmax')(z)
    from keras.models import Model
    model = Model(input_tensor, y)
    ```
- Inheriting the Model base class and customizing the model
    ```python
    class DNNModel(models.Model):
        def __init__(self):
            super(DNNModel, self).__init__()

        def build(self,input_shape):
            self.dense1 = layers.Dense(4,activation = "relu",name = "dense1")
            self.dense2 = layers.Dense(8,activation = "relu",name = "dense2")
            self.dense3 = layers.Dense(1,activation = "sigmoid",name = "dense3")
            super(DNNModel,self).build(input_shape)

        # Forward propagation
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

## 5 API

Finally, there is a specific introduction of low-, medium-, and high-level APIs. Interested readers can read it on their own. There are examples and Chinese, and it feels easy and pleasant to read.

## 6 Conclusion

"30 Days to Eat TensorFlow2" can quickly establish a knowledge framework for TensorFlow for us. The content is not too much, but the depth is enough. Suitable for readers with some foundation and who want to further understand TensorFlow.