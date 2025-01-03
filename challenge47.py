num1 = int(input("Enter a number: "))
total = num1
answer = 'y'
while answer == 'y':
    num2 = int(input("Enter another number: "))
    total = total + num2
    answer = input("Do you want to add another number: ")
print(f"The total is {total}")