# Bubble_sort algorithm

array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(array)

for i in range(n - 1):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("Sorted array: ", array)

# Selection Sort

S_array = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(n - 1):
    min_index = i
    for j in  range(i + 1, n):
        if S_array[i] > S_array[j]:
            min_index = j

    min_value = S_array.pop(min_index)
    S_array.insert(i, min_value)

print("Sorted array: ", S_array)