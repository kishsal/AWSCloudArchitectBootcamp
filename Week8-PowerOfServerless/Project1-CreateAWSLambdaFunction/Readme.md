# Create an AWS Lambda function

1. From AWS, search for Lambda
2. Click on Lambda
3. Select Create Function
4. Choose Author From Scratch
    - Provide name
    - Choose Python 3.8
    - Create new role with basic Lambda permissions
    - Create Function
5. From the code source
    - click on `lamdba_function.py`
    - Set the following code:
    ```
    import json

    def lambda_handler(event, context):
        print ('Hello Cloudskills')
    ```
    - Click deploy and then test
    - Provide `test` as name
    - click Create
    - Output should look like this:
    ```
    Response
    null

    Function Logs
    START RequestId: 640891e0-5b5a-487b-a198-900df183adec Version: $LATEST
    Hello Cloud
    END RequestId: 640891e0-5b5a-487b-a198-900df183adec
    REPORT RequestId: 640891e0-5b5a-487b-a198-900df183adec	Duration: 1.71 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 50 MB	Init Duration: 147.86 ms

    Request ID
    640891e0-5b5a-487b-a198-900df183adec
    ```
    - Delete Function

6. Create a new function, this time choose blueprint
    - Search for `python` and choose `hello-world-python`
    - Click configure
    - Name is `HelloPython`
    - For Execution role, choose existing and then select `service-role/hello-python-`
    - Click Create function
    - Choose the `lamdba_function.py` and code should look like this:
    ```
    import json

    print('Loading function')


    def lambda_handler(event, context):
        #print("Received event: " + json.dumps(event, indent=2))
        print("value1 = " + event['key1'])
        print("value2 = " + event['key2'])
        print("value3 = " + event['key3'])
        return event['key1']  # Echo back the first key value
        #raise Exception('Something went wrong')
    ```
    - click on Test
    - Configure Test event with name `test1`
    ```
    {
    "key1": "Cloudskills",
    "key2": "bootcamp",
    "key3": "value3"
    }
    ```
    - When the test is ran, the output should look like this:
    ```
    import json

    print('Loading function')


    def lambda_handler(event, context):
        #print("Received event: " + json.dumps(event, indent=2))
        print("value1 = " + event['key1'])
        print("value2 = " + event['key2'])
        print("value3 = " + event['key3'])
        return event['key1']  # Echo back the first key value
        #raise Exception('Something went wrong')
    ```
