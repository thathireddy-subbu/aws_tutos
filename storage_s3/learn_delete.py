import boto3

s3 = boto3.client('s3')
res = s3.delete_object(Bucket='subbu1996',Key='sbx.py')
print(res)