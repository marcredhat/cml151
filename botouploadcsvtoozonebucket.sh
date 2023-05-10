
#sudo python -m pip install boto3
import boto3
from botocore.client import Config
s3= boto3.resource('s3',endpoint_url='https://ip-10-10-72-69.us-west-2.compute.internal:9879',aws_access_key_id='mchisinevski@FEF0.LABS.CLDR.LINK',aws_secret_access_key='ebc4b34a95ed8d5a559991d10098f2c4fbdd58fa885d868f597e46039261e147',config=Config(signature_version='s3v4'),region_name='us-east-1',verify=False)

s3.create_bucket(Bucket='spark-bucket')

s3.Bucket('spark-bucket').upload_file('/home/ec2-user/imdbkaggle.csv','kaggledataset/imdbkaggle.csv')

###CHECK
#[root@ip-10-10-72-69 ec2-user]# ozone sh key info /s3v/spark-bucket/kaggledataset/imdbkaggle.csv
#{
#  "volumeName" : "s3v",
#  "bucketName" : "spark-bucket",
#  "name" : "kaggledataset/imdbkaggle.csv",
#  "dataSize" : 11421938,
#  "creationTime" : "2023-05-10T06:01:48.404Z",
#  "modificationTime" : "2023-05-10T06:01:48.404Z",
#  "replicationConfig" : {
#    "replicationFactor" : "THREE",
#    "requiredNodes" : 3,
#    "replicationType" : "RATIS"
#  },
#  "ozoneKeyLocations" : [ {
#    "containerID" : 2003,
#    "localID" : 111677748019208560,
#    "length" : 8388608,
#    "offset" : 0,
#    "keyOffset" : 0
#  }, {
#    "containerID" : 2004,
#    "localID" : 111677748019208559,
#    "length" : 3033330,
#    "offset" : 0,
#    "keyOffset" : 8388608
#  } ],
#  "metadata" : { }
#}
