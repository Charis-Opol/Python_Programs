firstname = input("Enter your first name: ")
if len(firstname) > 5:
    surname = input("Enter your surname: ")
    fullname = firstname+surname
    fullname = str.upper(fullname)
    print(fullname)
else: print(str.lower(firstname))