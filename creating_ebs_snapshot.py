#how to create ebs snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_snapshot( Description='string',
    VolumeId='string',)
    