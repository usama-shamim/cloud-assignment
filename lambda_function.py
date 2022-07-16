import os
import json
import boto3
s3client = boto3.client('s3')
dynamodb = boto3.client('dynamodb')
def handler(event, context):
  bucketName = event['queryStringParameters'].get('bucket_name')
  objName = event['queryStringParameters'].get('object_key')
  IP = str(event['headers'].get('X-Forwarded-For'))
  epochtime = str(event['requestContext'].get('requestTimeEpoch'))  
  headAction = s3client.head_object(Bucket= bucketName ,Key= objName)
  status = str(headAction['ResponseMetadata'].get('HTTPStatusCode'))
  dynamodbput = dynamodb.put_item(TableName='requeststable' , Item = {'IP-Adress':{'S':IP},'Epoch':{'S':epochtime},'HTTPCode':{'S':status}})
  response = {
    'isBase64Encoded': False,
    'statusCode': 200,
    'headers': {},
    'multiValueHeaders': {},
    'body': json.dumps({'Epoch Time =>':epochtime,'IP Address =>':IP, 'BucketName =>':bucketName, 'ObjectName =>':objName,'Object Found with status code':status})
  }
  return response
