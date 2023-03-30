message = input("Enter a message: ")

print("first character:", message[0])
print("last character:", message[-1])
print("middle character:", message[int(len(message) / 2)])
print("even index characters:", message[0::2])
print("odd index characters", message[1::2])
print("reversed", message[::-1])
