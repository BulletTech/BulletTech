---
template: overrides/blogs.html
tags:
  -nalytics
  -Database
---

# Snowflake architecture overview

!!! Info
    Author: [vincent] (https://github.com/realvincentyuan), published in 2021-06-06, reading time: about 6 minutes, WeChat public account article link: [: fontaWesome-solid-Link:] (https://mp.weixin.qq.q.com/s/772p9v4njagx36qbjnc3xa))

## 1 Introduction

Snowflake has been favored by many users and investors in recent years.Main architecture and working principles.

<figure>
  <img src = "httts://user-images.githubusercontent.com/26101303/13298228-360BD20B-ED29-84d3-77d74169f.png"/>
  <figcaption> Snowflake Stock Price </figcaption>
</Figure>

## 2 Snowflake main feature

-Anowflake supports multiple verification methods, such as Multi-Factor Authentication (MFA), Federal Authentication, SINGLE SIGN-ON (SSO) and OAUTH.The communication between the client and the server is protected by [TLS] (https://en.wikipedia.org/wiki/transport_layer_security "transport layer security").
-The characteristic SQL and many extended SQL features, which are supported by most SQL data definition language (Data Definition Language) and data operation language. Therefore, you don't have to worry about finding data analysis when doing data analysis.Corresponding operation.
-Snowflake supports software clients to connect, and also provides interfaces for multiple programming languages such as Python Connector, Spark Connector, Node.js Driver, .NET DRIVER, etc.
-The convenient sharing function, users can easily share data and query statements to other users.

## 3 Snowflake architecture

Snowflake's architecture blends [Shared-disk] (https://en.wikipedia.org/wiki/shaRd_disk_architecture "shared-disk Architecture") and [Shared- Nothing] (http] s: //en.wikipedia.org/wiki/Shared-nothing_architecture "shared-nothing Architecture" architecture to integrate the advantages of the two. Below is the sign of these two architectures:

### 3.1 Shared-DISK architecture signal

Commonly used in traditional databases, it has a storage layer that can be accessed by all nodes in the cluster. The computing nodes in the cluster do not have their own storage. They all obtain data by accessing the central storage layer and process it.Monitor and manage data processing through cluster control software.It is absolutely prohibited to update a piece of data at the same time.

This architecture is not conducive to performance play and lacks expansion.It is not suitable for such architectures that need to be updated, because Shared-DISK's lock mechanism will restrain it.

<figure>
  <img src = "httts://user-images.githubusercontent.com/26101303/13298226-1ccAF053-4C1C-933a-F555EEBD1E29.png">/>
  <figcaption> Shared-DISK architecture </figcaption>
</Figure>


### 3.2 Shared-Nothing architecture

As the name suggests, in the Shared-Nothing architecture, the cluster nodes have their own separate computing resources and storage space. Its advantage is that data can be stored in each node.When the user request is required, the route will allocate the request to the appropriate node for calculation. When there is an error in the calculation, the processing process can be taken over by other nodes to ensure that the user request can be handled and correctly processed.This architecture is very suitable for applications with a large amount of data reading, such as data warehouses.


<figure>
  <img src = "httts://user-images.githubusercontent.com/26101303/13298223-b99b67f5-47-b03F-AC165f76b9.png"/>
  <figcaption> Shared-Nothing architecture </figcaption>
</Figure>

### 3.3 Snowflake's architecture

Snowflake uses 3 different layers to build applications: `storage layers`, `calculating layer` and `cloud service layers, as follows:

<figure>
  <img src = "httts://user-images.githubusercontent.com/26101303/13298227-9cb5fbcd-cb8b8b8d-448abddb2663.png"/>
  <figcaption> Snowflake architecture </figcaption>
</Figure>

`Storage layer` is responsible for optimizing the data, compression and existence of multiple tiny areas.The data is stored in the ranks, and managed in a way similar to Shared-DISK.The calculation node obtains the data to obtain data for query calculations. The storage layer is independent of other resources. Snowflake is deployed on the cloud. Therefore, its ultra -large distributed storage system can ensure high performance, stability, availability, capacity and scalabilityEssence

`Calculating layer` uses virtual warehouse (virtual warehouse, relies on virtual machines) to run query statements, and the calculation layer and storage layer are designed to be separated. Between this, Snowflake realizes the intelligent cache mechanism to ensure the use of resource utilizationOptimize and reduce the unnecessary interaction between the computing layer and the storage layer.The virtual warehouse is divided into size. It can create multiple virtual warehouses to deal with different performance requirements, and the virtual warehouse is independent, so computing resources are not shared.The advantages of this design are:

-Capons or delete the virtual warehouse at any time, and it can also be convenient to expand the computing resources of the virtual warehouse without affecting the calculation of the query statement.
-D virtual warehouse can be easily disabled or enabled. It is suitable for re -participation in the inquiry after long -term without inquiries or discontinuation for a period of time
-It can change the cluster size of the virtual warehouse very conveniently

`Cloud service layer` is responsible for user information verification, cluster management, security and encryption, metadata management, query query sentence optimization, etc. These tasks are completed by calculating nodes.Common processing content examples include:

- User login
-After the query statement is submitted, the optimizer of the cloud service layer will be passed through the cloud service layer, and then passed into the calculating layer for processing
-The metadata required for optimizing query and filtering data is also stored on this layer

Snowflake's three -layer architecture can be expanded independently, but Snowflake only charges the storage layer and calculating layer because the service layer is processed in the calculating node.The advantages of separate expansion are obvious. If you need more data, you can expand the storage layer separately. The strong computing performance is required. You only need to expand the calculation layer alone.For details, see Snowflake's [Official Architecture Guide] (https://docs.snowflake.com/en/user-keide/intro- key-html "Snowflake architecture").

## 4 Summary

After understanding the Snowflake architecture, I believe you can better understand why so many companies choose Snowflake, which rely on the cloud architecture to provide many companies with efficient, safe, stable, and cost -effective solutions.As a data analyst, it is better to find that Snowflake is better than many traditional data warehouses.

Regarding the practical experience of SQL, please check the previous SQL tips: [Data Warehouse N Brother] (https://mp.weixin.qq.com/s ?_biz=mzi4mjk3nzgxoq=&mid=2247484458IDX=1&Snb9d205E0D6A 4589B68687E9C95 & CHKSM= EB90F75EDCE77E480D76A140289F4217C8DE8DE8DE8DA80C89B4CF09B1B07D87EF5F256831E & Token = 969028810 & Lang = zh_cn#RD) and [SQL imperfect practice Guide] (https://mp.weixin.qq.com/s ?__biz=mzi4mjk3ngxoq==&mid=2247484506&IDX=1&SN=c46E7BF8071FA6668F4CHKKKKSM=EB9072ED CE77E38C38FDFE685B1FF86590ed22AEA65B8C19F07FB7CE44B5B981929796873cc & Token = 969028810 & LANG = zh_cn#rd).I hope this sharing will help you!

<figure>
  <img src = "httts://cdn.jsdelivr.net/gh/bullettech2021/pics/2021-6-14/1623639526512-1080p%20hd)%20tail .png" widt "widt" widt "widt h = "500 " />
</Figure>