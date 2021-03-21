# Creating Volumes with Cloudformation

1. In AWS, choose Cloudformation
2. Create new Stack
3. Choose Create template in designer
4. Then create template in designer
    - Select EC2 and drag Volume
    - You can find properties for <b>AWS::EC2::Volume</b> by googling, then set JSON to reflect the following:
    ```
    {
        "Resources": {
            "EC2V30E2P": {
                "Type": "AWS::EC2::Volume",
                "Properties": {
                    "Availability Zone: "us-east1-1a",
                    "Size": 8
                }
            }
        }
    }
    ```
    - Click on the Deploy icon at the top
    - Click Next
    - Provide a name
    - Keep default and create stack