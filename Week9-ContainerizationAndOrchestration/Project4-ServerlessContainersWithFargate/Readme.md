# Serverless Container with ECS Fargate

1. In AWS, search for ECS
2. Click on Elastic Container Service
3. ECS and Fargate is pretty much the same services.  With Fargate it's a serverless container service.
4. Create Cluster
5. Choose `Powered by Fargate`
6. Provide name and create ECS
7. Once service is created, click on View Service
8. In the Service tab, click Create
    - Choose Fargate
    - Provide service name
    - Choose VPC, subnet
    - No autoscaling
    - 