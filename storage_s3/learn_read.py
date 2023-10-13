import boto3
import botocore

from botocore.exceptions import ClientError


s3 = boto3.client('s3')
try:
    res = s3.get_object(Bucket='subbu1996', Key='learnrt.txt')
    obj = res.get('Body')
    data = obj.read()
    print(data)
except ClientError as e:
    if e.response['Error']['Code']=='NoSuchKey':
       print('File not found')

