my_array = [7, 12, 9, 4, 11]
print(my_array)

for i in my_array:
    print(i)

#Finding the lowest value in an array algorithm
least_val = my_array[0]

for i in my_array:
    if i < least_val:
        least_val = i

print(f"The lowest value is {least_val}")

#Bubble sort algorithm
my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array1)
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array1[j] > my_array1[j + 1]:
            my_array1[j], my_array1[j + 1] = my_array1[j + 1], my_array1[j]

print("Sorted Array: ", my_array1)

#Improved Bubble Sort where the program automatically breaks out when the list is already sorted

my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]
swapped = False
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array1[j] > my_array1[j]:
            my_array1[j], my_array1[j + 1] = my_array1[j + 1], my_array1[j]
            swapped = True
    if not swapped:
        break

#Selection sort algorithm

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

#Improved selection sort algorithm

my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]
for i in range (n):
    min_index = i
    for j in range(i + 1, n):
        if my_array1[j] < my_array1[min_index]:
            my_array1[j], my_array1[min_index] = my_array1[min_index], my_array1[j]

print("Sorted array: ", my_array1)

#Insertion Sort algorithm
my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array1)
for i in range (1, n): #This is because the algorithm does not compare the fist value it only compares the second value and the rest
    insert_index = i
    current_value = my_array1.pop(i)
    for j in range (i-1, -1, -1):
        if current_value < my_array1[j]: #If  the current value being compared is smaller than the value in the sorted array then it is inserted in the place of that value
            insert_index = j
    my_array1.insert(insert_index, current_value)

print("Sorted array:", my_array1)

#Improved Insertion Sort Algorithm. Where we shift and make space for the value rather than poping
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

# Quick sort algorithm

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    left = []
    right = []
    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]
print("Sorted array:", quick_sort(my_array1))


#Merge sort algorithm

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    leftHalf = array[:mid]
    rightHalf = array[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

my_array1 = [64, 34, 25, 12, 22, 11, 90, 5]
print("Sorted array:", merge_sort(my_array1))

    