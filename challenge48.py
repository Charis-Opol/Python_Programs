answer = "yes"
count = 0
while answer == "yes":
    name = input("Enter the name of the person you want to invite to the party: ")
    print(f"You have invited {name}")
    count = count + 1
    answer = input("Do you want to invite another person: ")
print(f"You have invited {count} people for the party.")
