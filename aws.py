import boto3

# Let's use Amazon S3
# s3 = boto3.resource('s3')
# for i in s3.buckets.all():
#     print(i.name) 
# Upload a new file in s3 bucket
# data = open('screenshot.png', 'rb')
# s3.Bucket('adilkhanbucckeyt').put_object(Key='screenshot.png', Body=data)

# Get the service resource
# sqs = boto3.resource('sqs')
# Create the queue. This returns an SQS.Queue instance
# queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})
# print(queue)
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))

#Using an existing queue
# Get the queue. This returns an SQS.Queue instance
# queue = sqs.get_queue_by_name(QueueName='test')
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))

# Print out each queue name, which is part of its ARN
# for queue in sqs.queues.all():
#     print(queue.url)


#Sending messages
# Get the queue
# queue = sqs.get_queue_by_name(QueueName='test')

# # Create a new message
# response = queue.send_message(MessageBody='hello world')
# ## The response is NOT a resource, but gives you a message ID and MD5
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

# queue.send_message(MessageBody='boto3', MessageAttributes={
#     'Author': {
#         'StringValue': 'Adil',
#         'DataType': 'String'
#     }
# })

# Process messages by printing out body and optional author name
# for message in queue.receive_messages(MessageAttributeNames=['Author']):
#     # Get the custom author message attribute if it was set
#     author_text = ''
#     if message.message_attributes is not None:
#         author_name = message.message_attributes.get('Author').get('StringValue')
#         if author_name:
#             author_text = ' ({0})'.format(author_name)

#     # Print out the body and author (if set)
#     print('Hello, {0}!{1}'.format(message.body, author_text))

#     # Let the queue know that the message is processed
#     message.delete()

##################################
#Amazon DynamoDB#

import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
#creating a table

# table = dynamodb.create_table(
#     TableName='users',
#     KeySchema=[
#         {
#             'AttributeName': 'username',
#             'KeyType': 'HASH'
#         },
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'username',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )
# # Wait until the table exists.
# table.wait_until_exists()

# # Print out some data about the table.
# print(table.item_count)
##############################
#table = dynamodb.Table('users')
# #Creating a new item
# # put the data in dyanmodb
#data = table.put_item(
#     Item={
#     'username': 'Adilnawaz47',
#     'first_name': 'Adil',
#     'last_name': 'khan',
#     'age': 25,
#     'account_type': 'standard_user',
#     }
# )

#############################
# Getting an item
# Getting the table
table = dynamodb.Table('users')
# get_data = table.get_item(
#     Key = {
#         "username":"Adilnawaz47"
#     }
# )
# print(get_data)
# item = get_data['Item']
# print(item)

#########################
# Update an Item

# table.update_item(
#     Key={
#         'username': 'Adilnawaz47'
#     },
#     UpdateExpression='SET age = :val1',
#     ExpressionAttributeValues={
#         ':val1': 23
#     }
# )
# response = table.get_item(
#     Key={
#         'username': 'Adilnawaz47'
#     }
# )
# item = response['Item']
# print(item)

# table.delete_item(Key={"username":"Adilnawaz47"})

#The batch writer is even able to handle a very large amount of writes to the table
# with table.batch_writer() as batch:
#     for i in range(50):
#         batch.put_item(
#             Item={
#                 'account_type': 'anonymous',
#                 'username': 'user' + str(i),
#                 'first_name': 'unknown',
#                 'last_name': 'unknown'
#             }
#         )
#table.delete_item(Key={"username":"Adilnawaz47"})



##########################
#Querying and scanning

# from boto3.dynamodb.conditions import Key, Attr
# response = table.query(
#     KeyConditionExpression=Key('username').eq('Adilnawaz47')
# )
# items = response['Items']

# similarly we can also used scan method to quering and scanning

# response = table.scan(
#     FilterExpression=Attr('age').lt(27)
# )
# items = response['Items']
# for i in items:
#     print(i["username"])


############
# data = []
# response = table.scan(
#     FilterExpression=Attr('first_name').begins_with('s') & Attr('last_name').eq('khan')
# )
# items = response['Items']
# for i in items:
#     name  = {}
#     name['name'] = i["username"]
#     name['account_type'] = i["account_type"]
#     name['last_name'] = i["last_name"]
#     name['age'] = i["age"]
#     name['first_name'] = i["first_name"]
#     data.append(name)
# print(data)


############

# response = table.scan(FilterExpression = Attr("first_name").eq('a'))
# items = response['Items']
# print(items)


#####################
##Deleting a table
table.delete()
