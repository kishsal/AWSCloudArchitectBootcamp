# Running Python script in Lambda function

1. In AWS, search for Lambda
2. Create a new function
3. Choose Author from scratch
4. Provide a name
5. Create a new role
6. Create function
7. Copy/paste the following code to lambda_function.py
```
import boto3


ec2 = boto3.client('ec2')

def start_ec2instance(event, context):
    ec2.start_instances(InstanceIds= ['i-047432df5bd247f79'])
```
8. For InstanceIds, copy/paste an existing instanceId
9. Click on Test and Create
10. You should notice the response to be null and the instance has started again