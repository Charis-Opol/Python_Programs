total = 0

for i in range (0, 5):
    number = int(input("Enter a number: "))
    choice = input("Do you want the number to be added to the total?\nEnter your choice: ")
    choice = str.lower(choice)
    if choice == "yes":
        total = total + number
    else: 
        total = total + 0

print(f"The total is {total}")