value = int(input("enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 5 == 0:
    print("buzz")
elif value % 3 == 0:
    print("fizz")
else:
    print(value)
    
