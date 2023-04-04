upper_number = int(input("how many values should we process: "))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("all good")
    elif number % 3 == 0:
        print("all")
    elif number % 5 == 0:
        print("good")
    else:
        print(number)
        
        

    
    
