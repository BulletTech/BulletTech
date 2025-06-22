---
template: overrides/blogs.html
tags:
  - deep learning
  - tensorflow
  - recommendation
---

# TensorFlow Recommendation System (2)

!!! info
    Author: Tina, published on 2021-12-10, Reading time: about 6 minutes, WeChat public account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/0WcTB6WLBZX0EwbVZ_DeCg)

## 1 Introduction
Readers who have read [TensorFlow Recommendation System (1)](https://mp.weixin.qq.com/s/OUsG-JqqYeh9q6oAa_uhmg) should still have an impression. Last time we introduced the retrieval model, and there is another task model in the recommendation system, which is information ranking. In the ranking stage, the main task is to adjust the entries produced by the retrieval model to select the movie entries that are most likely to be liked and selected by users. 

Today, we will introduce in detail the principles and calling examples of the ranking model.

## 2 Source Code Analysis

- Prepare data, obtain and split the dataset. 
- Build the ranking model. 
- Fit and evaluate the model.

### 2.1 Data Preparation

```Python
import os
import pprint
import tempfile

from typing import Dict, Text

import numpy as np
import tensorflow as tf
## TensorFlow Dataset Resource
import tensorflow_datasets as tfds

## TensorFlow Recommendation System
import tensorflow_recommenders as tfrs

```

Import the `movielens` movie dataset from `TensorFlow Dataset` as the information retrieval model, and retain only the following three variables:
```Python
ratings = tfds.load("movielens/100k-ratings", split="train")

ratings = ratings.map(lambda x: {
    "movie_title": x["movie_title"],
    "user_id": x["user_id"],
    "user_rating": x["user_rating"]
})
```

Randomly shuffle the data, and take 80% as the training dataset and the remaining 20% as the test dataset:
```Python
tf.random.set_seed(42)
shuffled = ratings.shuffle(100_000, seed=42, reshuffle_each_iteration=False)

train = shuffled.take(80_000)
test = shuffled.skip(80_000).take(20_000)
```

In order to embed categorical variables, here use continuous integers to match each numerical value of movie titles and user IDs:
```Python
movie_titles = ratings.batch(1_000_000).map(lambda x: x["movie_title"])
user_ids = ratings.batch(1_000_000).map(lambda x: x["user_id"])

unique_movie_titles = np.unique(np.concatenate(list(movie_titles)))
unique_user_ids = np.unique(np.concatenate(list(user_ids)))
```

### 2.2 Build the Ranking Model

In the text model, you need to do word embedding (Embeddings) for users and movies first. Simply put, it is the process of converting text type data into computable numeric vector. Here, the embedding vectors of each dimension are 32. The second step is to build a sequential model. The model calls the fully connected layer of `Keras Dense`, and the activation function is `relu ` rectified linear unit function, which has the characteristic that when returning with default values, it returns `max(x,0)` element by element. Finally, use the `call()` function to input the input and return the ranking result.

```Python
class RankingModel(tf.keras.Model):

  def __init__(self):
    super().__init__()
    ## The embedding dimension is 32
    embedding_dimension = 32

    ## Compute embeddings for users.
    self.user_embeddings = tf.keras.Sequential([
      tf.keras.layers.StringLookup(
        vocabulary=unique_user_ids, mask_token=None),
      tf.keras.layers.Embedding(len(unique_user_ids) + 1, embedding_dimension)
    ])

    # Compute embeddings for movies.
    self.movie_embeddings = tf.keras.Sequential([
      tf.keras.layers.StringLookup(
        vocabulary=unique_movie_titles, mask_token=None),
      tf.keras.layers.Embedding(len(unique_movie_titles) + 1, embedding_dimension)
    ])

    # Compute predictions.
    self.ratings = tf.keras.Sequential([
      # Learn multiple dense layers.
      tf.keras.layers.Dense(256, activation="relu"),
      ## The output dimension is 256
      tf.keras.layers.Dense(64, activation="relu"),
      ## The output dimension of the output layer is 64
      # Make rating predictions in the final layer.
      tf.keras.layers.Dense(1)
  ])

  def call(self, inputs):
    ## The user ID and movie title are the input values of the model
    user_id, movie_title = inputs

    user_embedding = self.user_embeddings(user_id)
    movie_embedding = self.movie_embeddings(movie_title)

    return self.ratings(tf.concat([user_embedding, movie_embedding], axis=1))

```
As shown in the figure below, using an untrained model, recommend the movie "One Flew Over the Cuckoo's Nest (1975)" to user 9, and the predicted probability is 0.016:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/rank_result11.png" width="500"/>
</figure>


In order to obtain an evaluation value during training, the mean square error (MSE) loss function and root mean square error (RMSE) evaluation function are added to the original model task:

```Python
task = tfrs.tasks.Ranking(
  loss = tf.keras.losses.MeanSquaredError(),
  metrics=[tf.keras.metrics.RootMeanSquaredError()]
)
```

Package the ranking model and the above function into a new movie model, and prepare the `call ()` function and `compute_loss ()` function to fit and evaluate the model's performance:

```Python
class MovielensModel(tfrs.models.Model):

  def __init__(self):
    super().__init__()
    self.ranking_model: tf.keras.Model = RankingModel()
    self.task: tf.keras.layers.Layer = tfrs.tasks.Ranking(
      loss = tf.keras.losses.MeanSquaredError(),
      metrics=[tf.keras.metrics.RootMeanSquaredError()]
    )

  def call(self, features: Dict[str, tf.Tensor]) -> tf.Tensor:
    return self.ranking_model(
        (features["user_id"], features["movie_title"]))

  def compute_loss(self, features: Dict[Text, tf.Tensor], training=False) -> tf.Tensor:
    labels = features.pop("user_rating")

    rating_predictions = self(features)

    # The task computes the loss and the metrics.
    return self.task(labels=labels, predictions=rating_predictions)
```



### 2.3 Fit and Evaluate the Model

Call the model to compile the `compile()` method and use the Adagrad optimizer to specify a learning rate of 0.1:

```Python
model = MovielensModel()
model.compile(optimizer=tf.keras.optimizers.Adagrad(learning_rate=0.1))
```

During data fitting, shuffle the training set, batch processing, and data caching, for a total of three epochs:

```Python
cached_train = train.shuffle(100_000).batch(8192).cache()
cached_test = test.batch(4096).cache()

model.fit(cached_train, epochs=3)
```

```Python
model.evaluate(cached_test, return_dict=True)

## output:
#{'root_mean_squared_error': 1.1102582216262817,
# 'loss': 1.2078243494033813,
# 'regularization_loss': 0,
# 'total_loss': 1.2078243494033813}
```

Finally, three movies recommended for user 9 are recommended with the model's predicted ranking results:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/rank_result2.png" width="500" />
</figure>


## 3 Summary

In TensorFlow's movie recommendation system, the first step is to obtain movie entries that users may like from the data set, and the second step is to predict and rank these movie entries, in order to recommend the movie that users are most likely interested in and click on with limited information. In real life, you are the user. Therefore, I teach you a small trick to solve the problem of watching too few movies: instead of random browsing, search for some movies that you have watched and liked. The movies similar to what you like are in the "recommended for you" column. Why not give it a try!

I hope this article can help you, welcome everyone to leave a message for discussion.

