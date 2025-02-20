my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array1)
for i in range (1, n):
    insert_index = i
    current_value = my_array1[i]
    for j in range (i-1, -1, -1):
        if current_value < my_array1[j]:
            my_array1[j+1] = my_array1[j] # In this step the value in the array is shifted
            insert_index = j
        else:
            break
    my_array1[insert_index] = current_value
print("Sorted array:", my_array1)