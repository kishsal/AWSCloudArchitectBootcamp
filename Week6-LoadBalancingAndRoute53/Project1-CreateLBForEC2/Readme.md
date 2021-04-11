# Creating a load balancer for an EC2 instance

1. In AWS, deploy an EC2 instance
    - Keep it a simply Amazon Linux deploy
    - For SG, add http and https rules
    - Deploy instance

2. While instance is deploying, click on Load Balancers
    - Create a new load balancer
    - Create app lb
    - keep everything default and choose availability zones
    - Choose the deploy SG in step 1
    - For target group, choose instance
    - Choose VM to register
    - Deploy LB
