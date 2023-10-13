import boto3

s3 = boto3.client('s3')
# s3.upload_file('text.txt','subbu1996','learnx.txt')
res = s3.delete_object(Bucket='subbu1996',Key='sbx.py')
print(res)

