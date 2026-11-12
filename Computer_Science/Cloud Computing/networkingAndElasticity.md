# AWS Networking & Elasticity

Now that our systems and data is protected. Now we need users to find our site and need to make sure that our site can handle the incoming traffic and give peak preformance to users.

A main benefit of the cloud is it allows you to stop guessing capacity without buying servers upfront. With elasticity, servers, databases, applications can be scaled up or down based on load. And as we know we can scale vertically, horizontally or diagonally.

#### Route 53

AWS's cloud domain name service that has DNS servers across the world to translate-human readable names like www.google.com into numeric iP addresses liek 74.125.21.147. Scales automatically, allows you to register a domain name, route internet traffic and lets you do health checks on your servers.

#### EC2 Auto Scaling

A service that monitors EC2 instances and automatically adjusts our instances to maintain avaliability.

_Autoscaling Group Ex:_ https://www.youtube.com/watch?v=jd_OCzw9iC4

#### Elastic Load Balancer

Automatically distributes incoming application traffic across multiple servers. It balances load between two+ servers, stands in front of a web server, provides redundancy and performance. Found in the EC2 dashboard.

_Creating a Network Load Balancer Ex:_ https://www.youtube.com/watch?v=-sHVqdftqoc
