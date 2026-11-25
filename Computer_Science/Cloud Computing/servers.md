# **Servers** in the Cloud:

- Servers have allowed us to scale capacity
- Added storage, more memory, and computing power
- No need for onsite hardware or capital expenses

## **Elastic Cloud Compute (EC2):**

- A service that provides servers for rent in the cloud
- There are different pricing options for EC2:
  - On Demand: Pay as you go, no contract.
  - Dedicated Hosts: You have your own dedicated hardware and don't share it with others.
  - Spot: You pay the current Spot price, which fluctuates based on supply and demand. If the Spot price exceeds your maximum price or capacity is no longer available, your instance is interrupted.
  - Reserved Instances: You earn huge discounts if you pay up front and sign a 1-year or 3-year contract.

_Example of EC2 DashBoard Information:_

![alt text](../../images/ec2Dashboard.png)

1. Resources: A summary of all the EC2 resources running in a particular region such as instances, elastic IPs, placement groups, ...
2. Instances: Shows the list and details of the instances running in a given region
3. Images aka AMIs: Images are pre-configured templates containing an OS, application server, and software required to launch a virtual server. We can create custom AMIs, or we can use images owned by Amazon or others. We can use EC2 Image Builder for custom jobs.
4. Elastic Block Store (EBS): Simply put, EBS is an external hard drive that we can attach to the server for additional storage. In the section we have **volumes**, **snapshots**, and the **lifescycle manager**.
5. Network and Security:
   - **Security Groups** - acts as firewall rules that control traffic for EC2 instances or VPCs.
   - **Elastic IP Addresses** - static IPv4 address. In case you have a EC2 server instance failure the backup instance will spin up.
   - **Placement Group** - The EC2 instances are like VMs running on real servers in a data cetner and you can place them with different strategies like _clustered_, _partitioned_, and _spread evenly_.
   - **Key Pairs** - Our instances have public and private keys.
   - **Network Interfaces** - A network interface represents a virtual network card in a VPC

6. **Load Balancing** - Distributes incoming traffic across multiple servers (or targets such as EC2 instances). There are 3 types of load balancers: _Application Load Balancers_, _Network Load Balancers_, _Classic Load Balancers_.
7. **EC2 Auto Scaling**: A service that automatically launches/terminates EC2 instances based on user-defined scaling policies.

## AWS Command Line Interface

Allows you to access and control services running in your AWS account from the command line.

- You could install it and configure it on your own shell
- Or you could use the browser version: AWS CloudShell

## Creating a EC2 Instance

You simply can launch the instance wizard and configure all the settings you need. Then you can connect to the instance.

## Elastic Block Store (EBS)

EBS is a block-level storage service for EC2 instances that provides storage volumes that are attached to the EC2 instance to increase storage.

Simply put, EBS is an external hard drive that we can attach to the server for additional storage.

Benefits of using EBS are:

- Data persists after instances are terminated
- Automatically replicated within its avaliablity zone

## Creating a EBS Volume

We can simply navigate to the EC2 dashboard and then on the left-hand side click Volumes under the EBS section and create with specific settings.

## Security for Cloud Servers

Security in the cloud allows us to have complete control over our virtual networking enviornment. We can configure our virtual network with public or private facing subsets and launch servers in the selected netwrok to secure access.

**VPC** allows us create our own private network in the cloud and we can launch our services inside it. This is done as a security measure.

When we create an instance with EC2, a default VPC gets created for us. Alternatively we create our own custome VPC with user-defined subnets, route tables, internset gateways, and many other desirable configurations.

Creating VPC & Internet Gateway Ex: https://www.youtube.com/watch?v=tIlcy1WYIRw&t=108s

**Network Access Control Lists (ACLs)** define a set of firewall rules for controlling traffic coming in and out of subnets in the VPC.

## Compute Power in the Cloud & Lambda Functions

Being able to run application code in the cloud without having to manage servers make development easier.

**AWS Lambda** provides us with computing power in the cloud by allowing us to execute code without standing up or managing servers.

Notes:

- Lambdas have a time limit of 15 minutes
- Lambda code can be triggered by other AWS services
  - Like when things happen in the code base this lambda could run (I think). Examples include a file upload to AWS S3, DynamoDB inserts, or a reciept of an alert message from SNS.
- AWS Lambda supports Java, PowerShell, Node.js, and others. For other languages, we can use custom runtimes.

Creating a Lambda Function Ex: https://www.youtube.com/watch?v=MwykJta66l0

Creating a Lambda Function with Triggers: https://www.youtube.com/watch?v=pGo3swI8-Vo&t=7s

## Elastic Beanstalk

**Elastic Beanstalk** is an orchestration service that allows us to deploy web applications by provisioning all of the services that we need. It can set up an EC2 instance, auto-scaling, and an elastic load balancer and many more for you.

Ex Setup: https://www.youtube.com/watch?v=bvVQsnBby-c&t=2s

- I am not sure how the code that we write is connected to anything here.
