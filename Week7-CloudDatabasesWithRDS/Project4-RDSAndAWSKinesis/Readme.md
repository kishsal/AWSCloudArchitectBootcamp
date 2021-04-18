# RDS and AWS Kinesis

- Kinesis allows you to collect, process and analyze data

1. In AWS, go to the existing RDS DB
2. Click on the Configuration tab
3. Click on the existing parameter group (default.mysql8.0)
4. Search for `binlog_format`
    - User with replication slave permission is required

5. Set up Kinesis stream
    - Search for Kinesis
    - Select Kinesis
    - Create a data stream
    - Provide name `rds-cloudskills`
    - Enter `1` for shard
    - Create data stream

6. Ensure user has atleast admin privs
    - GO to IAM
    - Users
    - Search for User
    - Attach Kinesis policy (FullAccess)

7. Deploy using Terraform
    - Copy the files from `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/tree/main/Module-7-Cloud-Databases/AWS-Kinesis` into the folder
    - Install required libraries as mentioned in main.tf
    - Change to directory and run `python main.py cloudskills-mysql-db.cgmyv9zj836w.us-east-1.rds.amazonaws.com admin <pw> rds-cloudskills`