# array, search and return the biggest number
# use a for loop and a linear search algorithm to find and return all the numbers that missing
# store then in a array and then print the array

def find_largest_number(array):
    largest_number = array[0]
    for i in range (1, len(array)):
        if largest_number < array[i]:
            largest_number = array[i]
        else:
            continue
    return largest_number

array1 = [1,2,5,7,8,10]
largest = find_largest_number(array1)
print("The largest value is", largest)

missing_values = []

for i in range (0, largest + 1):
    if i not in array1:
        missing_values.append(i)
    
print(missing_values)

