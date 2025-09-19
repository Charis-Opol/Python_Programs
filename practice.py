def linear_search(array, key):
    n = len(array)
    for i in range(n):
        if array[i] == key:
            return i
    return -1

array = [2, 6, 4, 7, 9, 10, 23]
print(array)
num = int(input("Enter a number to search for: "))
answer = linear_search(array, num)
if answer != -1:
    print(f"{num} was found at index {answer}")
else:
    print("Not found!")


def binary_search(array, key):
    right = len(array) - 1
    left = 0

    while left <= right:
        mid = (left + right)//2
        
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            left = mid + 1
        elif array[mid] > key:
            right = mid - 1
    return -1

arraylist = [2, 4, 7, 8, 12, 15, 24]
print(arraylist)
input = int(input("Enter the value you want to search for: "))
answer = binary_search(arraylist, input)
if answer != -1:
    print(f"{input} was found at index {answer}")
else:
    print("Not found")  
    

def insertion_sort(array):
    n = len(array)
    for i in range (1, n):
        current_index = i
        current_value = array.pop(i)
        for j in range(i - 1, -1, -1):
            if array[j] > current_value:
                current_index = j
        array.insert(current_index, current_value)
    return array

array = [15, 6, 92, 9, 24, 1]
sorted_array = insertion_sort(array) 
print("Sorted array: ", sorted_array)

def bubble_sort(array):
    n = len(array)
    for i in range (n - 1):
        for j in range (n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = [15, 6, 92, 9, 24, 1]
sorted_array = bubble_sort(array) 
print("Sorted array: ", sorted_array)


def selection_sort(array):
    n = len(array)
    for i in range (n - 1):
        min_index = i
        for j in range (i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        min_value = array.pop(min_index)
        array.insert(i, min_value)
    return array

array = [15, 6, 92, 9, 24, 1]
sorted_array = selection_sort(array) 
print("Sorted array: ", sorted_array)


def quick_sort(array):
    if len(array) <= 1:
        return array
     
    pivot = array[-1]
    left = []
    right = []

    for i in range (len(array) - 1):
        if array[i] <= pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
        
array = [15, 6, 92, 9, 24, 1]
sorted_array = quick_sort(array) 
print("Sorted array: ", sorted_array)


def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    i = 0
    j = 0
    merged_array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i = i + 1
        elif right[j] < left[i]:
            merged_array.append(right[j])
            j = j + 1
        
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array

array = [15, 6, 92, 9, 24, 1]
sorted_array = merge_sort(array) 
print("Sorted array: ", sorted_array)


linkedlists = {0:[5,1],1:[3,2],2:[8,3],3:[10,4],4:[3,5],5:[6,-1]}

def display_linkedList(linkedlist):
    index = 0
    while index != -1:
        element, next_index = linkedlist[index]
        print(element, end= " -> ")
        index = next_index
    print("None")

display_linkedList(linkedlists)

linkedlists[5] = [6,6]
linkedlists[6] = [5,7]
linkedlists[7] = [24,-1]
display_linkedList(linkedlists)

del linkedlists[6]
linkedlists[5] = [6,7]
display_linkedList(linkedlists)

array = [0, 20 ,30 ,40, 50]
print(array)

number = int(input("Enter a value you want to add: "))
array.append(number)
print(array)
array.insert(-1, number)
print(array)
number_remove = int(input("Enter a number you want to remove: "))
array.remove(number_remove)
print(array)

from collections import deque

queue = deque()

queue.append(3)
queue.append(6)
queue.append(65)
queue.append(12)
queue.append(34)
queue.append(43)
queue.append(1)
queue.append(4)
print("Queue", list(queue))

dequed = queue.popleft()
print("This is the element that was dequeued: ", dequed)
print(queue)
dequed1 = queue.pop()
print("This the dequeued element: ", dequed1)

stack = []

def push(value):
    stack.append(value)
    return stack

def peek():
    return print("This the top element: ",stack[-1])

def pop():
    poped = stack.pop(-1)
    return print("This is the poped element: ", poped)

push(3)
push(5)
push(8)
push(3)

print(stack)
peek()
pop()

node1 = {'Data': 20,'Pointer':None}
node2 = {'Data': 30,'Pointer':None}
node3 = {'Data': 40,'Pointer':None}
node4 = {'Data': 50,'Pointer':None}
node5 = {'Data': 60,'Pointer':None}


node1 = {'data':10, 'pointer': None}
node2 = {'data':20, 'pointer': None}
node3 = {'data':30, 'pointer': None}

node1['pointer'] = node2
node2['pointer']=node3

head = node1

current = head
while current:
    print(current['data'])
    current = current['pointer']