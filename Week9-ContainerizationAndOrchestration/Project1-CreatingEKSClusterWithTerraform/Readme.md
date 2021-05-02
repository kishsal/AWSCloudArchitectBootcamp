# Creating an EKS Cluster in AWS

1. In AWS, search for EKS
2. Click on `Elastic Kubernetes Service`
3. Provide a cluster name (For example: `cloudskills-eks`) and click next step
4. Choose Kubernetes version `1.19`
5. Either use existing role `cloudskillseks` or create a new role with `AmazonEKSClusterPolicy` policy
6. Click Next
7. Create a new VPC or use default
8. Create a new security group or use existing security group
    - Refer to `https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html` when setting up security group
    - To create a new SG,
        - Click on SG and create new SG
        - Provide name and description
        - Choose VPC from above
        - Choose `All Traffic` for outbound
9. Keep everything else as default and Create

10. Once the cluster deployment is completed, we will need to create node groups
    - Click on the Compute tab
    - Click Add Node Groups
    - Provide Name (`cloudskills-nodegroup`)
    - Choose IAM role, if you don't have an existing role, create a new role with the following policies
        - AmazonEKSClusterPolicy
        - AmazonEKSCWorkerNodePolicy
        - AmazonEKSContainerRegisterReadOnlyPolicy
        - AdministratorAccess
        - AmazonEKSServicePolicy
    - Click Next and Choose type of EC2 instance to run
        - Choose minimum number of nodes `1` since it's dev
    - Click Next
        - Choose SSH keypair
    - Create NODE group

11. If you go to EC2 instance, you will see the created EC2 instance