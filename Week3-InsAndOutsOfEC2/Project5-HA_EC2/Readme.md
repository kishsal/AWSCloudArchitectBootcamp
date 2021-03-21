# High Availability EC2 Instances

1. In AWS, go to EC2
2. Select Load balancers
3. Create new LB
4. App LB
    - Provide Name
    - Internet facing
    - ipv4
    - Listener = HTTP/80
    - VPC and Availability Zones
    - Accelerator improves availability
    - Choose SG
    - Target group is for EC2 instances
    - Register targets (Requires EC2 instances)