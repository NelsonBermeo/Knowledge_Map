# AWS Messages and Containers

Now that we know how to route users to our website and handle incoming traffic. We'd like the ability to notify/alert users when things happen like large withdrawls from a user's bank account.

We may consider adopting a container technology, like docker, to bunlde our app to move from os to os.

#### Simple Nofitcation Service (SNS)

Allows you to send notifcations to the users of the application. We can decouple notification logic and allows published notifications to reach many subscripters.

SNS uses a publish/subscribe model where users who want notifications should sign up.

_Sending Alerts Ex:_ https://www.youtube.com/watch?v=V0u1rcRuDCU

**AWS EventBridge** is a service to create rules that match specific events (such as a state change in an AWS resource) and route them to targets like AWS Lambda or Amazon SNS for automated response. Use cases include increasing developer agility, monitoring and auditing applications, extending functionality with SaaS integrations, and cuztomizing SaaS with AI.

_AWS EventBridge Ex:_ https://www.youtube.com/watch?v=eLEk90aUv2A&t=26s

#### Simple Queue Servce (SQS)

A fully managed message queuing service that helps decouple and scale distributed systems and microservices. With SQS we can send, store and recieve messages between application components, and SQS will duranly store messages until they are processed.

_Ex Scenario:_

Imagine a course registration system where account creation must happen before course registration. If ordering matters, use a FIFO queue and group messages by student (message group ID) so account creation messages are processed before registration messages for the same student.

_Creating a Queue Ex:_ https://www.youtube.com/watch?v=cFn3wrrXOT0

#### Containers

A container is an OS level virtualization that allows us to run multiple isolated processes in parrallel. A container is an isolated process that consists of the following items, all bundled into one package:

- the application code
- the required dependencies
- the necessary runtime env to run the application
  Each container is an indepdendent component that can run on its own and be moved from enviornment to environment.

Containers make it easier for devs to create, deploy and run applications on different hardware and platforms quickly and easily.

**Docker** is the leading container technology. And there are several container orchestration serices that allow us to manage our docker clusters such as **Kubernetes**.

**Docker** is a platform that helps to build, test and run containers. We can build containers locally using the Docker CLI, which is included with Docker Desktop. If there are multiple containers running individual services of an application we can use the Docker Compose utility to define and run multi-container applications.

A **docker image** is a portable, read-only template that contains a set of instructions to create a container. An image can be instantiated multiple times to create multiple containers.

A **dockerfile** is a textfile containing commands to create an image. In other words, Docker builds images by reading the commands from a Dockerfile.

**AWS Elastic Container Sercice (ECS)** is an orchestration service used for automating deployment, scaling and manging containerized applications.

Use cases could follow:

We have a multi-container application that you want to run on the cloud. we may also need to scale the containers automatically based on the incoming traffic in such a case.

Amazon ECS deploys, manages, and scales containers based on your resource needs and supports other AWS services like Elastic Load Balancing, EC2 security groups, EBS volumes, and IAM roles.

_ECS Cluster Ex_: https://www.youtube.com/watch?v=x2pGS41s9uA&t=2s
