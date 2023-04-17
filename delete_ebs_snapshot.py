#how to delete ebs snap shot
import boto3
ec2_client=boto3.client("ec2")

respones=ec2_client.delete_snapshot(
    SnapshotId='')
    
print(respones)