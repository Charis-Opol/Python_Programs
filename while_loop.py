again = "yes"
while again == "yes":
    print("Hello")
    again = input("Do you want to loop again? Enter your response: ")


total = 0
while total < 100:
    num = int(input("Enter a number: "))
    total = total + num

print(f"The total is {total}")