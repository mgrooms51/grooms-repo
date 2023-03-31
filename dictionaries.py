# 1) set the emails variable to be an empty dictionary

emails = {}

# 2) Add 'chris', 'eric', and 'taylor', to the emails dictionary without reassigning the variable.

emails['chris'] = 'chris@yahoo.com'
emails['eric'] = 'eric@yahoo.com'
emails['taylor'] = 'taylor@yahoo.com'

print(emails)

# 3) remove eric from the emails dictionary without reassigning the variable.

del emails['eric']

print(emails)

# 4) add rudy to the emails dictionary with out reassigning the variable.

emails['rudy'] = 'rudy@yahoo.com'

print(emails)

# 5) return a list of keys from the emails dictionary as 'users'

users = list(emails.keys())

print(users)

# 6) return a list of values from the emails dictionary as 'emails_list'

email_list = list(emails.values())

print(email_list)

# 7) return a list of tuples called 'pairs' representing the key/value pairs in 'emails'

pairs = list(emails.items())

print(pairs)

