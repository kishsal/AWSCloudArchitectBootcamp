# Host a website in S3

1. Go to AWS console
2. Search for S3
3. Create a new bucket
    - Uncheck Block All Public access
    - Create bucket
4. Go to permissions
    - Edit Bucket Policy
    - Insert the following:
    ```
    {
    "Version":"2012-10-17",
        "Statement":[
            {
            "Sid":"PublicReadGetObject",
            "Effect":"Allow",
            "Principal": "*",
            "Action":["s3:GetObject"],
            "Resource":["arn:aws:s3:::example.com"]
            }
        ]
    }
    ```
    - Change example.com to S3 bucket name: `kscsbucket2021/*`

6. Go to Objects and upload files
    - Grab files from `https://github.com/CloudSkills/AWS-Cloud-Architect-BootCamp/tree/main/Module-5-Cloud-Storage-With-S3/Python-Web-App-S3`
    - And upload index.html

7. Go to bucket and properties
    - Go down to Static Website hosting
    - Click Edit
    - Enter `index.html` for Index Document
    - Save changes

8. Go to bucket and properties
    - Go down to Static Website hosting
    - Click on the pubic URL
