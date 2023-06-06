#in a CML terminal session
#sudo python -m pip install boto3
#https://ozone.apache.org/docs/1.1.0/recipe/botoclient.html
#[root@ip-10-10-72-69 ec2-user]
#aws --endpoint-url http://ip-10-10-72-69.us-west-2.compute.internal:9002 s3 ls  marc
#2023-05-16 23:52:59      37874 airlines.csv
#2023-05-16 23:52:49 7970265521 flights.csv
import boto3
from botocore.client import Config
s3= boto3.resource('s3',endpoint_url='http://ip-10-10-72-69.us-west-2.compute.internal:9002',aws_access_key_id='marc',aws_secret_access_key='Cloudera#123',config=Config(signature_version='s3v4'),region_name='us-east-1',verify=False)

#s3.create_bucket(Bucket='marc')

s3.Bucket('atlastest').upload_file('/home/cdsw/imdbkaggle.csv','imdbkaggle.csv')

session = boto3.session.Session()

s3_client = session.client(service_name='s3',aws_access_key_id='marc',
        aws_secret_access_key='Cloudera#123',
        endpoint_url='http://ip-10-10-72-69.us-west-2.compute.internal:9002',verify=False
    )
response = s3_client.head_bucket(Bucket='atlastest')
print(response)


response = s3.Bucket('atlastest').download_file('imdbkaggle.csv', 'fromminio.csv')
print(response)
