my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array1)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array1[j] < my_array1[min_index]:
            min_index = j
    min_value = my_array1.pop(min_index)
    my_array1.insert(i, min_value)
print("Sorted array: ", my_array1)
