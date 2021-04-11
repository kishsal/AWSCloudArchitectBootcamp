# High availability Load balancers

1. In AWS, deploy two EC2 instances
    - Keep it a simply Amazon Linux deploy
    - Use existing SG from project1
    - Deploy instances

2. Add VMs to target groups
    - Click on Target Groups
    - Click on `cloudskills-tg`
    - In the targets tab, click on Register targets
    - Select the two new deployed VM and click add to pending
    - Register pending targets
    