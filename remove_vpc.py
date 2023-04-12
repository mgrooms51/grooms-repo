#how to remove vpc

import boto3

client = boto3.client('ec2')

response = client.delete_vpc(
    VpcId='string'
    )
#you must detach any services attched to the vpc you wish to delete