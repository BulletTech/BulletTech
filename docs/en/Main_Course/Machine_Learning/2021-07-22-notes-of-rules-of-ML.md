---
template: overrides/blogs.html
tags:
  - machine learning
---

# Reflections on "Rules of Machine Learning" (Part 1)

!!! info
    Author: Void, published on 2021-07-26, reading time: about 10 minutes, link to article on WeChat Official Account: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/mhEt3WCvwKNuFSv8tVlPeA)

## 1 Introduction

The title of "Rules of Machine Learning" caught me off guard the first time I heard it. Who dares to name their article that, and claim to have all the answers?  
Upon seeing the author and source, okay, it's written by a respected Google expert. So let's see what this ambitious article can teach us.  
As the article is quite long (divided into 3 parts, with 43 rules), this is part 1 of the series (including the first phase). This article is based on my limited experience and knowledge, with some added personal insights based on my translation. Comments and discussions are welcome.

## 2 Overview

The article begins with an overview:

```
To make great products:
do machine learning like the great engineer you are, not like the great machine learning expert you aren’t.
```

In practical work, the top priority is the engineering implementation: defining the problem clearly, and having a solid pipeline for solving it. Only after that do fancy algorithms come into play to improve performance.

## 3 Before using machine learning

```
Rule #1: Don’t be afraid to launch a product without machine learning.
```

Simple models and direct rules are always your baseline. They may not be perfect, but they are effective when you have nothing else.

```
Rule #2: First, design and implement metrics
```

Design good evaluation metrics, and keep records.

```
Rule #3: Choose machine learning over a complex heuristic
```

When your rules become too complex, use machine learning. The magic of machine learning lies in its ability to learn complex relationships, and updates to the model are relatively simple.

## 4 Your first pipeline

```
Rule #4: Keep the first model simple and get the infrastructure right.
```

Have a solid baseline, because everything that follows will be built on it.

```
Rule #5: Test the infrastructure independently from the machine learning
```

Even though the infrastructure is probably already provided, you can still examine it with a critical eye to deepen your understanding of it, and even possibly discover ancestral bugs.

```
Rule #6: Be careful about dropped data when copying pipelines.
```

Different scenarios may have different requirements for data (e.g. some need historical data, while others only need the latest data). In addition, pay close attention to the data and check for small details you may have missed (such as multiple records with the same key when joining), as they may affect the final results and differ from what you expected.

```
Rule #7: Turn heuristics into features, or handle them externally.
```

Effective rules that already exist can become features for the model, or can be used directly (as in black and white lists).

## 5 Monitoring

```
Rule #8: Know the freshness requirements of your system.
```

Monitor the performance of the model according to its importance.

```
Rule #9: Detect problems before exporting models.
```

Try to discover all problems before the model goes live.

```
Rule #10: Watch for silent failures.
```

Monitor the model's dependencies, such as the data and features behind it, for missing or abnormal conditions beyond its evaluation metrics. This is actually quite tricky, as there will always be problematic data, and you may wonder how it will affect the model.

```
Rule #11: Give feature column owners and documentation.
```

Create good documentation; this is a common problem, even for big companies.

## 6 Your first objective

```
Rule #12: Don’t overthink which objective you choose to directly optimize.
```

Don't get bogged down in optimizing specific objectives. In my understanding, optimizing objectives can be more or less important. For instance, catching bad actors can be more beneficial than falsely accusing innocent people in some scenarios. Therefore, the model should focus on the catch rate. It is difficult for a new model to outperform existing solutions in various dimensions.

```
Rule #13: Choose a simple, observable and attributable metric for your first objective.
```

Choose a simple, observable, and attributable evaluation metric for your model. Leave complex and indirect metrics to policy analysts.

```
Rule #14: Starting with an interpretable model makes debugging easier.
```

Start with an interpretable model for easy debugging. Don't immediately use fancy algorithms, as they will only increase the difficulty of problem discovery.

```
Rule #15: Separate Spam Filtering and Quality Ranking in a Policy Layer.
```

Different tasks have different backgrounds, so don't rely on a model that performs well in Task A to perform well in Task B.

## 7 Conclusion

These 15 rules mainly focus on specific steps before modeling, and provide a good general direction for building models. These rules are surely the result of many past pitfall experiences, and are valuable lessons to keep in mind.  
The next part will cover more specific modeling content, discussing rules related to feature engineering and optimizing models, so stay tuned.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>