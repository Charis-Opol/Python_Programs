number = int(input("Enter a number between 1 and 10: "))
if number < 10 and number > 1:
    print("The number is below 10 but above 1")
elif number == 10:
    print("The number is ten")
else:
    print("The number is not within the range asked!")
