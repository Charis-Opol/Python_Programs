number = int(input("Enter a number between 1 and 12: "))
if number > 12 and number < 1:
    print("Invalid entry, Try again!")
else: 
    for i in range (0, 12):
       print(i * number)