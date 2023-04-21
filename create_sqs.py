#import boto3 
#use boto3 client('sqs')

import boto3

my_sqs = boto3.client('sqs', region_name = 'us-east-1')

#Create a new sqs_queue

response = my_sqs.create_queue(
    QueueName='first_sqs')
#print response to get information about your queue

print(response)    