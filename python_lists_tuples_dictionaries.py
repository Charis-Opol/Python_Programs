fruit_tuple = ("apple", "banana", "strawberry", "orange")
print(fruit_tuple.index("strawberry"))
print(fruit_tuple[2])

names_list = ["John", "Tim", "Sam"]
del names_list[1]
print(names_list)
names_list.append(input("Add a name: "))
print(names_list)
names_list.sort()
print(names_list)

colours = {1:"red", 2:"blue", 3:"green"}
print(colours)
colours[2] = "yellow"
print(colours)

x = [154, 634, 892, 345, 341, 43]
print(len(x))
print(x[1:4])

for i in x:
    print(i)

num = int(input("Enter number: "))
if num in x:
    print(f"{num} is the list")
else:
    print("Not in the list")

x.insert(2,420)
x.remove(892)
x.append(993)
print(x)