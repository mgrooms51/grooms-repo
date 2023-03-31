# 1) Take in message from user

message = input("enter a message: ")

# 2) print out lowercase, uppercase, capitalized, and title case versions of user message

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

# 3) split the users message and print list of words 

words = message.split()
print("Words:", words)

# 4) sort words in message alphabetically using first and last words. print sorted words

sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic last Word:", sorted_words[-1])
