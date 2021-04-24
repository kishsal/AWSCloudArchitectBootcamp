# Implementing SNS and SQS wiht Lambda

1. In AWS, search for SNS
2. Choose `Simple Notification Service`
3. Create new SNS Topic and provide name `CloudskillsTopic`
4. Choose `standard` as type
5. Choose Access Policy, set to `Everyone`
6. Create Topic
7. Open a new duplicate tab and open Lambda
8. Create a new Function
9. Choose blueprint and search for `sns`
10. Choose `sns-message` and configure
11. Provide name `SNSPythonCloudskills`
12. Create new Role
13. For SNS trigger, choose the `CloudskillTopic` SNS topic
14. Create Functions
15. You will now notice the function is connected to the SNS topic.
16. Click on SNS and Enable
17. Click on Test and run
