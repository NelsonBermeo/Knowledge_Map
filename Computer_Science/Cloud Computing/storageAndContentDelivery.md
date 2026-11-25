# Storage And Content Delivery

## Storage in the Cloud

Companies today need to collect, store and analyze data. Storage services in the cloud allow companies to store data. This provides durability, avaliability and scalability. This means no data will be lost in the cloud, data can be accessed fast and reliability, and applications in the enviornment can add or remove steadily.

- There is vertical, horizontal and diagonal scaling

## S3 & Glacier

**Amazon Simple Storage Server (S3)** is an object storage system in the cloud for text documents, images, HTML, and more.

All objects or files are stored in a bucket that can hold millions of objects. Buckets live in a region.

S3 is built for durability of 99.99+ and 99.99 avaliability %.

Use cases include static websites, content delivery, backup and recovery, archiving data, and more.

There are different S3 storage classes:

- **Glacier:** Data archiving for data you won't need to access too often. You'll want to use this for perhaps log files, audits, etc.
- **Standard:** General purpose, frequent access.
- and many more...

_Creating a S3 Bucket Ex:_ https://www.youtube.com/watch?v=52Xq4RLH_Aw&t=3s

## DynamoDB

**DynamoDB** is a NoSQL document database with large scale.

**NoSQL** databases are schemaless and means the database does not have a fixed structure which means it can be altered on the fly. Data is stored in JSON form. Each row is a record and these are called _documents_.

_Creating a DynamoDB Database Ex:_ https://www.youtube.com/watch?v=gXH7J3Vzz6M&t=21s

## Relational Database Service (RDS)

Relational databases need to persist data for later use. **Relational Database Service (RDS)** is a service that aids in the administration of management of database such as upgrades, patching, installs, etc. RDS simply sits on top of your database and helps manage. It can mangage engines such as oracle, postgres, mariadb and more.

_Features_ include:

- failover
- backups
- restorations
- encryptions
- etc...

_Creating a RDS Ex:_ https://www.youtube.com/watch?v=VZSmT8hLXwA

## RedShift

**Redshift** is a cloud data warehousing service to help companies manage big data or a large volume that needs to be analyzed.

It allows you to:

- execute fast queries
- SQL
- ETL
- Automates tasks
- etc...

Redshift is for **OLAP** databases for analysis.

## Content Delivery - Cloud Front

**Content Delivery (CDN)** speeds up delivery of web content, pages, css, images, etc.

Typically content is cached for a period of time. And when a client requests the cache retrieves the data. A CDN reduced latency and decreases load.

**Cloud Front** is the CDN and speeds up delivery through Amazon's worldwide network of **Points of Presense (PoPs)** called **Edge Locations**.
