#import jason and boto3
import json
import boto3

#import datetime module
from datetime import datetime

#use lambda_handler to process events
def lambda_handler(event, context):

    now = datetime.now()    #current date and time                                    
    date = "%m/%d/%Y"     #get date in months/days/year                                      
    time = "%H:%M"       #time hours/min                                   
   
   
    current_time = now.strftime(date+" "+time) #returns date and time as string
    
    message = "late nights early mornings: " + current_time #message+time

    my_sqs = boto3.client('sqs') #boto3 sqs
    
    #sedn message to sqs

    my_sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/645619684184/first_sqs",
        MessageBody=current_time
    )

    return {
        'statusCode': 200,      # succsessful completion
        'body': json.dumps(message) #python object to json object
    } 
