## Calculator with functions

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
        exit()
    else:
        return a / b
    
def multiplication(a, b):
    return a * b

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    answer = int(input("Enter your option: "))
    
    if answer == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The result is: ", addition(num1, num2))
    elif answer == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The result is: ", subtraction(num1, num2))
    elif answer == 3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The result is: ", division(num1, num2))
    elif answer == 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The result is: ", multiplication(num1, num2))
    elif answer == 5:
        print("Exiting the calculator")
        exit()
    else:
        print("Invalid response!")
if __name__ == "__main__":
    main()


        



