import math
number = int(input("Enter an integer over 500"))
if number > 500:
    sqrt_number = (math.sqrt(number))
    print(round(sqrt_number, 2))
else: print("That integer is below 500. Try again!\n")