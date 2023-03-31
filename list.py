# 1) create an empty list 
services = []

# 2) populate list using append or insert

services.append('s3')
services.append('lambda')
services.append('ec2')
services.append('dynamodb')
services.append('cloudwatch')

# 3) print list and length of list

print(services)
print(len(services))

# 4) remove two services from the list by name or index

del services[0:2]

# 5) print new list and length of new list

print(services)
print(len(services))
 
# 6) push code to Github