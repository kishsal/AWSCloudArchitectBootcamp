# Creating a public facing s3 bucket

1. In AWS Console
2. Search for S3
3. Create a bucket 
4. Then go to Permissions
    - Change the public access
    - Review changes
<br>
5. Go to Bucket Policy
    - Click on Edit
    - Select Policy example
    - Copy following policy json
    ```
        {
            "Version": "2012-10-17",
        "Id": "S3PolicyId1",
        "Statement": [
            {
            "Sid": "IPAllow",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
            ],
            "Condition": {
            "NotIpAddress": {"aws:SourceIp": "54.240.143.0/24"}
            }
            }
        ]
        }
    ```
    - Paste it into the policy
    - Update the DOC-EXAMPLE-BUCKET to `ks2021bucket`
    - Save Changes
    - You will notice a whole bunch of errors.  This is because of the sourceIp set.

6. Go to Access Control List
    - Allow you to change access control

7. CORS (Cross-Origin Resource Sharing)
    - HTTP mechanism
    - For example, allow you to specify source 