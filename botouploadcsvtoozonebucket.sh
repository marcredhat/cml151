#sudo python -m pip install boto3
import boto3
from botocore.client import Config
s3= boto3.resource('s3',endpoint_url='https://ip-10-10-72-69.us-west-2.compute.internal:9879',aws_access_key_id='mchisinevski@FEF0.LABS.CLDR.LINK',aws_secret_access_key='ebc4b34a95ed8d5a559991d10098f2c4fbdd58fa885d868f597e46039261e147',config=Config(signature_version='s3v4'),region_name='us-east-1',verify=False)

s3.create_bucket(Bucket='spark-bucket')

s3.Bucket('spark-bucket').upload_file('/home/ec2-user/imdbkaggle.csv','kaggledataset/imdbkaggle.csv')
