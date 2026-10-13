**Servers** in the Cloud:

- Servers have allowed us to scale capacity
- Added storage, more memory, and computing power
- No need for onsite hardware or capital expenses

**Elastic Cloud Compute (EC2):**

- A service that provides servers for rent in the cloud
- There are different pricing options for EC2:
  - On Demand: Pay as you go, no contract.
  - Dedicated Hosts: You have your own dedicated hardware and don't share it with others.
  - Spot: You pay the current Spot price, which fluctuates based on supply and demand. If the Spot price exceeds your maximum price or capacity is no longer available, your instance is interrupted.
  - Reserved Instances: You earn huge discounts if you pay up front and sign a 1-year or 3-year contract.

_Example of EC2 DashBoard Information:_

![alt text](/images/ec2Dashboard.png)

1. Resources: A summary of all the EC2 resources running in a particular region such as instances, elastic IPs, placement groups, ...
2. Instances: Shows the list and details of the instances running in a given region
3. Images aka AMIs: Images are pre-configured templates containing an OS, application server, and software required to launch a virtual server. We can create custom AMIs, or we can use images owned by Amazon or others. We can use EC2 Image Builder for custom jobs.
