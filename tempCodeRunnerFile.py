
def binary_search(array, target_value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target_value:
            return mid

        if array[mid] < target_value:
            left = mid + 1
        elif array[mid] > target_value:
            right = mid - 1
    return -1

my_array2 = [1,2,5,6,23,78,122]
print(my_array2)
number = int(input("Enter the target number you are searching for: "))
result_index = binary_search(my_array2, number)
if result_index != -1:
    print(f"{number} is found in index {result_index}")
else: 
    print(f"{number} is not found")