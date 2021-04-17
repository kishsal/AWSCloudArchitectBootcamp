# Automating the creation of RDS databases with Cloudformation

1. Create a folder called `Terraform`
2. Copy each file from `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/tree/main/Module-7-Cloud-Databases/Create-Terraform_database` to the folder
    - Set secret to secrets.tfvars file
3. Open terminal and change to Terraform directory
4. Enter `terraform init`
5. Enter `terraform plan --var-file=secrets.tfvars` (Since secrets are stored in a separate file)
6. Enter `terraform apply --var-file=secrets.tfvars` and enter `yes` to deploy

7. To destroy the DB,
    - In the terraform.tfstate file, set `"skip_final_snapshot": true,`
    - run `terraform destroy --var-file=secrets.tfvars`

8. Make sure to delete the following files before pushing changes to repo   
    - .terraform
    - terraform.tfstate
    - terraform.tfstate.backup
    - terraform.lock.hcl