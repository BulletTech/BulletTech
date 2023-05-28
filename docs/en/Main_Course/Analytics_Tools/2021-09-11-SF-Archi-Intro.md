---
template: overrides/blogs.html
tags:
  - analytics
  - database
---

# Overview of SnowFlake Architecture

!!! info
    Author: [Vincent](https://github.com/Realvincentyuan), published on June 6, 2021, reading time: about 6 minutes, WeChat public account article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/772p9v4nJAGX36qBjNC3xA)

## 1 Introduction

SnowFlake, as a highly popular data warehousing application in recent years, has gained the favor of many users and investors. In my daily work, I also often use SnowFlake for analysis, so I have done some research on its underlying operation mechanism. Today, I will talk to you about the main architecture and working principles of SnowFlake.

<figure>
  <img src="https://user-images.githubusercontent.com/26101303/132982228-360bd20b-ed29-4ff6-84d3-c77d74169c9f.png"  />
  <figcaption>SnowFlake stock price</figcaption>
</figure>

## 2 Main Features of SnowFlake

- Security and Data Protection: SnowFlake supports multiple authentication methods, such as Multi-Factor Authentication (MFA), Federal Authentication, Single Sign-on (SSO), and OAuth. Communication between clients and servers is protected by [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security).
- Support Standard SQL and Many Extended SQL Features: SnowFlake supports most SQL data definition language (Data Definition Language) and data manipulation language (Data Manipulation Language), so there is no need to worry about finding corresponding operations when doing data analysis.
- SnowFlake supports software clients for connection, and also provides interfaces for various programming languages such as Python connector, Spark connector, Node.js driver, .NET driver, etc.
- Convenient Sharing Functionality: Users can easily share data and query statements with other users.

## 3 SnowFlake Architecture

The SnowFlake architecture combines the advantages of Shared-Disk architecture and Shared-Nothing architecture, and consists of three different layers: the Storage Layer, the Compute Layer, and the Cloud Services Layer. The architecture diagrams of these two types are shown below:

### 3.1 Shared-Disk Architecture Diagram

This is commonly used in traditional databases. It has a storage layer that all nodes in the cluster can access, and the computing nodes in the cluster do not have their own storage. They all access the central storage layer to retrieve data and perform processing. The cluster control software is used to monitor and manage data processing. All nodes obtain the same data, so it is absolutely forbidden for two or more nodes to update the same data at the same time.

This architecture is not conducive to performance, and lacks scalability. Applications that require frequent data updates are not suitable for this type of architecture because the Shared-Disk lock mechanism will impede them.

<figure>
  <img src="https://user-images.githubusercontent.com/26101303/132982226-1ccaf053-bddd-4c1c-933a-f555eebd1e29.png"  />
  <figcaption>Shared-Disk Architecture</figcaption>
</figure>


### 3.2 Shared-Nothing Architecture Diagram

As the name suggests, in the Shared-Nothing architecture, each node in the cluster has its own separate computing resources and storage space, and data can be stored in various nodes by partition. When processing user requests, the router assigns the request to the appropriate node for calculation. When a calculation error occurs, the processing process can be taken over by another node to ensure stable and correct processing of user requests. This architecture is very suitable for applications with a large amount of data reads, such as data warehouses.

<figure>
  <img src="https://user-images.githubusercontent.com/26101303/132982223-b99b67f5-3018-4f47-b03f-ac1f165f76b9.png"  />
  <figcaption>Shared-Nothing Architecture</figcaption>
</figure>

### 3.3 SnowFlake Architecture Diagram

SnowFlake uses three different layers to build the application: the storage layer, the compute layer, and the cloud services layer. The diagram is shown below:

<figure>
  <img src="https://user-images.githubusercontent.com/26101303/132982227-9cb5fbcd-cb8b-4c53-8f8d-448abddb2663.png"  />
  <figcaption>SnowFlake Architecture</figcaption>
</figure>

The Storage Layer is responsible for optimizing, compressing, and storing data in multiple tiny fragments. Data is stored in row column format and managed in a manner similar to Shared-Disk. Compute nodes retrieve and process data by connecting to the Storage Layer, which is independent of other resources. SnowFlake is deployed in the cloud, so its super large distributed storage system can ensure high performance, stability, availability, capacity, and scalability.

The Compute Layer uses virtual warehouses (based on virtual machines) to run query statements. The Compute Layer and the Storage Layer are designed to be separate, and SnowFlake implements intelligent caching mechanisms between them to optimize resource utilization and reduce unnecessary interaction between the Compute Layer and the Storage Layer. Virtual warehouses come in different sizes and can be used to process requests with different performance requirements. Each virtual warehouse is independent of each other, so compute resources are not shared. The advantages of this design are:

- Virtual warehouses can be created or deleted at any time. It is also easy to expand the computing resources of virtual warehouses without affecting the calculation of query statements.
- Virtual warehouses can be easily stopped or restarted, suitable for long periods of time without queries or need to participate in queries after a period of dormancy.
- Virtual warehouse cluster size can be automatically changed very easily.

The Cloud Services Layer is responsible for user information authentication, cluster management, security and encryption, metadata management of data, optimization of query statements, etc. These tasks are all completed by the Compute Layer. Common processing content examples include:

- User login
- After the query statement is submitted, it will first go through the optimizer of the Cloud Services Layer, and then be passed to the Compute Layer for processing
- Metadata required for optimizing queries and filtering data is also stored at this level

The three-layer architecture of SnowFlake can be independently expanded, but SnowFlake only charges for the Storage Layer and the Compute Layer, as the Cloud Services Layer is processed in the Compute Node. The advantage of independent expansion is obvious. If more data is needed, the Storage Layer can be individually expanded. If stronger computing performance is required, the Compute Layer can be individually expanded. Refer to the official SnowFlake [Architecture Guide](https://docs.SnowFlake.com/en/user-guide/intro-key-concepts.html) for more details.

## 4 Conclusion

After understanding the SnowFlake architecture, I believe you can better understand why so many companies choose SnowFlake. Its cloud-based architecture provides efficient, secure, stable, and cost-effective solutions for many enterprises. As a data analyst, I have personally experienced that SnowFlake is indeed easier to use than many traditional data warehouses.

For practical experience with SQL, please check out the previous SQL Tips: [Data Warehouse N Brothers](https://mp.weixin.qq.com/s?__biz=MzI4Mjk3NzgxOQ==&mid=2247484458&idx=1&sn=b103c9b9d205e0d6a4589b68687e9c95&chksm=eb90f75edce77e480d76a140289f4217c8f8de8cb6b5