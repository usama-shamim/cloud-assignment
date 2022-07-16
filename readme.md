**Cloudformation Implementation of AWS ApiGW , Lambda and Dynamodb**

> **Purpose of Repo**

We need a microservice which takes a POST or GET request from client on to an AWS API Gateway and passes on to Lambda Function. The Lambda Function then process that request, performs S3 HEAD action, retrieves metadata from an object without returning the object itself and returns the response either object exists or not.

This transaction is recorded in AWS Dynamo DB as well. Specifically, where the request was generated from (IP Address(X-Forwarded-For)), Epoch timestamp(requestTimeEpoch), and return http status code.

> ****Instructions to test****

**1.** Clone the repo.

**2.** Go to the directory of repo.

**3.** Type 
    
    "aws cloudformation deploy --region us-east-1 --template-file stack.yaml --stack-name lambda-api --capabilities CAPABILITY_IAM"
    
    Where --region can be any region where you want to deploy the stack. 
    
**4.** Once it is deployed use below mentioned POST api in postman or by using httpie. I have used httpie :

    "http -v POST "https://{$apigatewayid}.execute-api.{AWS::Region}.amazonaws.com/v0/lambda/?bucket_name=BUCKETNAME&object_key=OBJECTKEY""
    
  Replace {$apigatewayid}, {AWS::Region}, BUCKETNAME and OBJECTKEY  with your apigw id , AWS region, S3-bucketname and S3 Object name respectively.
    
  You will be able to see the POST api end point in the Cloudformation outputs as well.
    
  Output of API:
    
    
   ![image](https://user-images.githubusercontent.com/54571862/179373473-679bd28b-b2da-4ce3-b5fa-7751ae64e688.png)

   Records added in Dynamodb are like:

   ![image](https://user-images.githubusercontent.com/54571862/179373553-22928f66-2098-42a8-be96-12862fcf3e04.png)

>**Pending Tasks**

**1.** Error / Exception Handling

**2.** Nested SAM Template

**3.** Few Wildcard IAM roles needs to be changed to specific roles

**Please feel free to reach out to me in case of any improvements / suggestions.**




    

