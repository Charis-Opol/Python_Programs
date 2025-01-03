number = int(input("Enter a number between 10 and 20: "))
while number < 10 or number > 20:
    if number < 10:
        print("Too Low!")
        number = int(input("Try again: "))
    elif number > 20:
        print("Too High!")
        number = int(input("Try again: "))
print("Thank you")