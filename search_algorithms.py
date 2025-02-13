def linear_search(array,target):
    #n = len(array)-1
    n = len(array)
    for i in range (n):
        if array[i] == target:
            return i
        #else:
           # return -1  

array1 = [1,7,2,3,7,4,5,6,7,8]
target_num = 7
result = linear_search(array1,target_num)
print(result)
'''if result != -1:
    print(f"The target was found at index {result}")
else:
    print("Number not found") '''


def binary_search(array,target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        
        if array[mid] < target:
            return mid + 1
        elif array[mid] > target:
            right = mid - 1

    return -1