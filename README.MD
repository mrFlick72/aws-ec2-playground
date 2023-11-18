#  Simple Apache On EC2

The Cloud Formation Stack is intended to provision a EC2 instance with a simpel apache installed 
with a custom page. 

The interesting thing in this playground is about how to provision an EC2 instance 
that avails on CFN Init together to CFN Signal to configure the instance in a declarative fashion, take in account 
the instance provisioning and the instance configuration as criteria to mark the instance completed from 
Cloud Formation point of view, and keep in sync the cfn-init across multiple cloud formation template updates.

## Architecture

![img.png](simple-apache-on-ec2%2Fimg.png)