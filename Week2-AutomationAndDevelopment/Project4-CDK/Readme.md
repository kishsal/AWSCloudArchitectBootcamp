# Instructions to set up CDK

1. Install CDK - 'sudo npm install -g aws-cdk'
2. Install the S3 CDK package - 'sudo pip3 install aws-cdk.aws-s3'
3. Ensure CDK was installed - 'cdk --version'
4. Create a folder called "cdk" and cd into folder
5. Initialize an environment - 'cdk init app --language python'
6. install requirements needed for the environment
    - You will notice various files being added to the folder
    - File you need to work is app.py
    - Copy code from https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/blob/main/Module-2-automation-and-development/CDK/creates3-cdk.py into app.py
7. From the cdk folder path, enter 'cdk deploy'
    - Error:


## Helpful Docs
https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html
https://github.com/aws/aws-cdk/tree/master/packages/aws-cdk
https://github.com/aws-samples/aws-cdk-examples