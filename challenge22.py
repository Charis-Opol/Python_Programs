firstname = input("Enter your firstname in small letters: ")
surname = input("Enter your surname in small letters: ")
firstname = firstname.title()
surname = surname.title()
name = firstname+" "+surname
print(f"Your name is {name}")