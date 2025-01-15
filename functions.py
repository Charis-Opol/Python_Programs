def my_function():
    print("Hello from a function\n")

my_function()

def my_function_1(fname):
    print(fname + " Refsnes")

my_function_1("Emilly")
my_function_1("Tobias")
my_function_1("Linus")

def my_function_2(fname, lname):
    print(fname + " " + lname)

my_function_2("Charis", "Opol")
#my_function_2("Charis")

def my_function_3(*kids):
    print("The youngest kid is " + kids[4] )

my_function_3("Janice", "Fidel", "Charis", "Favour", "Treasure")

def my_function_4(child3, child2, child1):
    print("The youngest kid is " + child3)

my_function_4(child1 = "Janice", child2 = "Fidel", child3 = "Charis")

def my_function_5(**name):
    print("His last name is " + name["last"])

my_function_5(first = "Charis", last = "Opol")

def my_function_6(country = "Norway"):
    print("I am from " + country)

my_function_6("Sweden")
my_function_6()
my_function_6("Japan")

def my_function_7(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function_7(fruits)

def my_function_8(x):
    return 5 * x

print(my_function_8(4))
print(my_function_8(9))
print(my_function_8(2))
print(my_function_8(7))

def my_function_9():
    pass

def my_function_10(x , /):
    print(x)

my_function_10(3)

def my_function_11(x):
    print(x)

my_function_11(5)

def my_function_12(*, x):
    print(x)

my_function_12(x = 3)

def my_function_13(a, b, /, *, c, d):
    print(a + b + c + d)

my_function_13(5, 6, c = 7, d = 8)

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
        return result
    
print("Recursion Example results: ")
tri_recursion(6)