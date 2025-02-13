def linear_sort(array, target_value):
    n = len(array) - 1
    for i in range(n):
        if array[i] == target_value:
            return i
        else: 
            return -1

my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]
num = int(input("Enter the number you are searching for: "))
result = linear_sort(my_array1, num)
if result != -1:
    print(f"{num} is found in index {result}")
else:
    print(f"{num} is not found")