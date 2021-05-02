# Accessing and Deploying Apps to EKS

1. Run the command in `AWSCloudArchitectBootcamp/Week9-ContainerizationAndOrchestration/Project2-AccessingAndDeployingAppsToEKS/connect-to-eks.sh`
2. Output should look like this:
    ```
    jdoe-mn2:Cloudskills jdoe$ aws eks --region us-east-1 update-kubeconfig --name cloudskills-eks
    Added new context arn:aws:eks:us-east-1:727235799305:cluster/cloudskills-eks to /Users/jdoe/.kube/config
    ```
3. Change to directory where the nginx.yml is stored
    - Enter the following: `kubectl create -f .\nginx.yaml`

4. Now enter `kubectl get pods` to view the deployed pods