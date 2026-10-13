Course: Udacity - AWS Cloud Fundamentals
Instructor - Kesha Williams

Cloud computing is the delivery of IT resources over the internet. The cloud is like a virtual data center accessible via the internet that allows you to manage:

- Storage Services like databases
- Servers, compute power, networking
- Analytics, artificial intelligence, augmented reality
- Security services for data and applications

**Benefits of Cloud Computing Include:**

- Pay as you go: you pay only for what you use (avoiding huge capital investments)
- Autoscaling: based on demand, active servers can grow or shrink
- Serverless: Allows you to write and deploy code without having to worry about the underlying infrastructure
- Failing fast and iteratively
- Scale globally to reduce latency with global servers and avaliablity zones
- Backup accessibility for disaster recovery

**Types of Cloud Computing:**

- Infrastructure-as-a-Service (IaaS): a provider supplies virtual server instances, storage, and mechanisms for you to manage servers
- Platform-as-a-Service (PaaS): a platform of development tools hosted on a provider's infrastructure.
- Software-as-a-Service (SaaS): a software application that runs over the internet and is managed by the service provider

**Types of Cloud Deployment Models:**

- Public Cloud: A public cloud makes compute, storage and application services avaliable over the internet for multiple customers. Public cloud providers operate shared, multi-tenant infrastructure. Examples: AWS, Azure, GCP (Google Cloud Platform)
- Private Cloud: A private cloud provides infrastructure and services exlusively for a single organization. It can be hosted-on premises at organizations. Private clouds are often chosen for stronger control over security, compliance, and data residency.
- Hybrid Cloud: A hybrid model combines public and private enviornments that allow data to move between them. For instance, a organization may keep sensitive customer Personally Identifiable Information (PII) on-premise and run a web application on the public cloud. These are common for regulated industries, gradual cloud migrations, burst capacity and disaster recovery.

**AWS** offers many services on it's product page.

- Compute Services include Amazon EC2, Amazon Elastic Container Service, AWS Lambda.
- Storage Services include Quick Sight, Athena, Redshift
- Application Integration includes Simple Queue Service (SQS), Simple Notification Service (SNS)
- And many many more...

**Shared Responsibility Model**

Just because we use AWS services doesn't our side of the job is done. We are responsible for managing identity and access managment, encrypting data in the cloud, and more. AWS secures the cloud, hardware and optimization across large networks. Below is the shared responsibiliy model we follow while using AWS:

![alt text](/images/awsSharedResponsibilityModel.png)
