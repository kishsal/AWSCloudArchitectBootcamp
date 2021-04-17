# Creating an RDS Database

1. In AWS, search for RDS
2. Click on RDS
3. Click on Create Database
4. Choose Standard create
5. Choose MySQL
6. Choose MySQL community version 8.0.20
7. For Templates, choose free tier
8. For DB Instance Identifier, enter `cloudskills-mysql-db`
9. For credentials, set username as `admin` and to auto generate password
10. For DB instance class, choose `db.t2.micro` which is for free tier
11. Choose default VPC
12. Create a new subnet group and set public access to `yes` (easier to access)
13. Create new security group called `mysql-sg`
14. For AZ, choose `us-east-1a`
15. Keep everything else as default and create database
16. While DB is getting created, click on `View Credentials` and store password