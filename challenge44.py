response = int(input("Enter the number of people you want to invite for the party: "))
if response < 10:
    for i in range (0, response):
        name = input("Enter the name of the person you are inviting: ")
        print(f"You have invited {name}")
else: 
    print("Too many people!")