#how to describe a single snapshot

import boto3
ec2_boto3=boto3.client("ec2")

respones=ec2_boto3.describe_snapshots(SnapshotIds=[
        'snap-053cb85ffd3a2c362',]) 
print(respones)

