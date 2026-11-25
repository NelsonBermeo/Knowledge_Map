# AWS Security

We'll want to make sure our website and the servers our website runs on is protected

We need security because we need to keep data (especially PII) secure, our applications secure, and more.

## AWS Web Application Firewall (WAF)

Provides a firewall that protects our applications. It's a network security mechanism that monirots and controls traffic based on preset rules.

Can guard against SQL injection, cross-site scripting, reviewing data sent, and other well-known attacks.

## AWS Shield

A managed DDoS protection service that safe-guards AWS hosted applications. AWS shield is an out of the box free service that is always running.

## Identity and Access Management (IAM)

We need to ensure confidentiality. **IAM** allows us to configure who can access our AWS account, services and applications in our account.

We can create IAM polciies to create grandular level permissions and can be attached to users, groups and roles.

**EC2 Security Groups** are not part of IAM, and are not a IAM security group. EC2 security groups are for EC2 instances.

_IAM Ex:_ https://www.youtube.com/watch?v=4IJpy5yPE7w

_IAM Policy Ex:_ https://www.youtube.com/watch?v=c_ZcPs6OIbw&t=6s

_IAM Policy to User:_ https://www.youtube.com/watch?v=v5-7mehiKgY

The **IAM Identity Center** (successor to AWS SSO) provides a central place where you create or connect your workfoce identities in AWS once and manage access centrally to multiple AWS accounts and applications.

## Amazon Cognito

A service that offers authentication and authorizatoin features. It helps secure identity and access management for apps.

There are two main components: **User Pools** and **Identity Pools**.
