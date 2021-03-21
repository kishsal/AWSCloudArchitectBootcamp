# Creating an EC2 instance with Terraform

1. Refer to `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/tree/main/Module-3-learning-the-ins-and-outs-of-ec2/ec2` when adding files to Terraform folder
2. Review the files
    - Updated subnet_id variable to something you find on `https://console.aws.amazon.com/vpc/home?region=us-east-1#subnets:`
    - Update IP_Address variable to reflect subnet range
    - Refer to existing key pair name on `https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:`
    <br>
3. Then run `terraform init`
4. Then run `terraform plan`
5. Then run `terraform apply`
6. Verify all of the resources have been deployed to AWS
7. To delete the resource, enter `terraform destroy`