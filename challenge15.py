choice = input("Is it raining?\nEnter your response: ")
choice = str.lower(choice)
if choice == "yes":
    choice_2 = input("Is it windy? \nEnter the your response: ")
    choice_2 = str.lower(choice_2)
    if choice_2 == "yes":
        print("Its too windy for an umbrella!\n")
    else: print("Take an umbrella!")
else: print("Have a nice day!\n")

