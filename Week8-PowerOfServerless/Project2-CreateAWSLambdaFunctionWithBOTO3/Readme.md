# Create an AWS Lambda Function with Boto3

1. Create a file called `lambda.py`
2. Copy content from `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/blob/main/Module-8-The-Power-Of-Serverless/lambda.py` to `lambda.py` file
3. Download `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/blob/main/Module-8-The-Power-Of-Serverless/pythonscript.zip` and paste into folder
4. Copy content from `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/blob/main/Module-8-The-Power-Of-Serverless/pythonscript.py` and to new file called `pythonscript.py`
<br/>
5. Then run the following command:
    ```
    python ./lambda.py hellopythonlambda arn:aws:iam::727235799305:role/service-role/hello-python-role-qh1livvg
    ```
    Note: arn:aws property is from the existing role
<br/>
6. Then go to AWS and find the deployed Lambda function