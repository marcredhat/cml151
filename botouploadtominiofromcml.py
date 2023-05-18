#sudo python -m pip install boto3
#https://ozone.apache.org/docs/1.1.0/recipe/botoclient.html
import boto3
from botocore.client import Config
s3= boto3.resource('s3',endpoint_url='http://ip-10-10-72-69.us-west-2.compute.internal:9002',aws_access_key_id='marc',aws_secret_access_key='Cloudera#123',config=Config(signature_version='s3v4'),region_name='us-east-1',verify=False)

#s3.create_bucket(Bucket='spark-bucket')

#s3.Bucket('spark-bucket').upload_file('/home/ec2-user/imdbkaggle.csv','kaggledataset/imdbkaggle.csv')

session = boto3.session.Session()

s3_client = session.client(service_name='s3',aws_access_key_id='marc',
        aws_secret_access_key='Cloudera#123',
        endpoint_url='http://ip-10-10-72-69.us-west-2.compute.internal:9002',verify=False
    )


s3.create_bucket(Bucket='cml-bucket4')

s3.Bucket('cml-bucket4').upload_file('/home/cdsw/data/imdb_kaggle.csv','cml-bucket4/imdbkaggle.csv')

#[root@ip-10-10-72-69 ec2-user]# aws --endpoint-url http://ip-10-10-72-69.us-west-2.compute.internal:9002 s3 ls cml-bucket4/cml-bucket4/
#2023-05-18 04:36:11   66212309 imdbkaggle.csv
