def insertion_sort(array):
    n = len(array)
    for i in range (1, n):
        insert_index = i
        current_value = array.pop(insert_index)
        for j in range (i-1, -1, -1):
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value) 
    return array


# Test with numbers
numbers = [12, 4, 5, 3, 8, 7]
print("Sorted Numbers:", insertion_sort(numbers))

# Test with words
words = ["banana", "apple", "grape", "cherry", "date"]
print("Sorted Words:", insertion_sort(words))
