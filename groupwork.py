def insertion_sort(array): # Function for insertion sort
    n = len(array)
    for i in range (1, n): # Loop through the array starting from the second element
        insert_index = i # Initialize the insert index to the current element's position
        current_value = array.pop(insert_index) # Remove the current element from the array and store it in a variable
        for j in range (i-1, -1, -1): # Loop through the elements before the current element in reverse order
            if array[j] > current_value: # If the current element is smaller than the element before it
                insert_index = j # Move the insert index to the position before the current element
        array.insert(insert_index, current_value) # Insert the current element at the correct position
    return array


# Test with numbers
numbers = [12, 4, 5, 3, 8, 7]
print("Sorted Numbers:", insertion_sort(numbers))

# Test with words
words = ["banana", "apple", "grape", "cherry", "date"]
print("Sorted Words:", insertion_sort(words))
