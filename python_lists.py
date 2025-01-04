shopping_list = ["tomatoes", "onions", "garlic", "green pepper", "watermelon", "rice", "oil", "meat", "chicken", "soda"]
quantities_list = [20, 10, 5, 10, 2, 5, 2, 4, 3, 3]

me = shopping_list[-2]

print(me)

shopping_list.append("Spagetti")
print(shopping_list)
shopping_list.extend(["Cheese", "potatoes", "5 pinapples"])
print(shopping_list)
shopping_list = shopping_list + ["vinager", "wheat flour"]
print(shopping_list)
shopping_list.insert(0, "Sweets")
print(shopping_list)
shopping_list.remove("Cheese")
print(shopping_list)
shopping_list.pop(4)
print(shopping_list)
print(shopping_list.pop(4))
quantities_list.clear