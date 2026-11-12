# AWS Management

AWS has tools that allows support for troubleshooting and reviewing activity.

It's important to have visibility into our cloud applications to check:

- How the server is performing?
- What is the current load on the server?
- What is the root cause of an error a user is seeing and the path?

We'll need access to logging and auditing.

#### AWS CloudTrail

Records AWS API activity so that we can audit and investigate actions on our account. CloudTrail captures API calls in S3 buckets or CloudWatch logs from the AWS Management Console, AWS SDKs, and other AWS services and delivers logs for analysis and monitoring.

CloudTrail also have support for event types to know when things occur.

_CloudTrail Ex:_ https://www.youtube.com/watch?v=YhjHUJ8Aq8Y

#### AWS Cloud Watch

A service that monitors resources and applications that run on AWS by collecting data in the form of logs, metrics and events. It helps us observe, troubleshoot, and automate responses to operational issues.

_CloudWatch and Amaazon EventBridge Ex:_ https://www.youtube.com/watch?v=nvqyem5IW2c

#### Infrastructure as Code & CloudFormation

Allows us to describe and provision all the infrastructure resources in our cloud environment.

We can stand up servers, databases, runtime parameters, resources, etc. based on scripts that we write.

IaC is a time-saving feature because it allows us to provision resources in a reproducible way.

**AWS CloudFormation** is AWS's IaC service and allows us to model our entire infrastructure in a text file template, allowing us to provision AWS resources based on the tempaltes we write. We can write scripts from scratch or reuse blueprints from AWS.
