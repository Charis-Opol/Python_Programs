choice = input("Enter a direction: ")
choice = str.upper(choice)
if choice == "UP":
    number1 = int(input("Enter an number above 1: "))
    for i in range (1, number1 + 1):
        print(i)
elif choice == "DOWN":
    number2 = int(input("Enter a number below 20: "))
    for i in range (20, number2 - 1, -1):
        print(i)
else: 
    print("I don't understand!")
