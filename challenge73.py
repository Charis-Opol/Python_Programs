food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1] = food1
food2 = input("Enter another food you like: ")
food_dictionary[2] = food2
food3 = input("Enter another food you like: ")
food_dictionary[3] = food3
food4 = input("Enter another food you like: ")
food_dictionary[4] = food4
food5 = input("Enter another food you like: ")
food_dictionary[5] = food5
food6 = input("Enter one last food you like: ")
food_dictionary[6] = food6
print(food_dictionary)
dislike = int(input("Which food would you like to get rid off/\nEnter the number: "))
del food_dictionary[dislike]
print(food_dictionary)
print(sorted(food_dictionary.values()))
