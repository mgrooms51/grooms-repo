import boto3

client = boto3.client('ec2')
#describe all available

x = client.describe_vpcs()

no_of_vpcs = x['Vpcs']

len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc['VpcId'])
    
#how to describe one vpc based on vpc id

x = client.describe_vpcs(VpcIds=["vpc-0735b8ebd085771af"])
