#Create a comparison value in one of the arrays
#Compare the values in the opposite array using the comparison value one at a time
#Append the least value of the comparison to the merged array
# if the comparison value is the least append it and move to  the next index and compare again.

def array_merging(array1, array2):
    merged_array = []
    ptr1 = 0 # pointer in array1
    ptr2 = 0 #pointer in array2

    while ptr1 < len(array1) and ptr2 < len(array2): #Runs until one of the array has no elements
        if array1[ptr1] < array2[ptr2]:
            merged_array.append(array1[ptr1])
            ptr1 += 1
        else:
            merged_array.append(array2[ptr2])
            ptr2 += 1
    
    while ptr1 < len(array1):
        merged_array.append(array1[ptr1])
        ptr1 += 1
    
    while ptr2 < len(array1): #Add the elements if there areany left overs from the arrays
        merged_array.append(array1[ptr2])
        ptr2 += 1
    
    return merged_array

a = [1, 12, 15, 26, 38] 
b = [2, 13, 17, 30, 45]
merged_array = array_merging(a,b)
print("Merged array:", merged_array)


# Median of both arrays
n = len(merged_array)
print(len(merged_array))
if n % 2 == 0:
    median1 = n//2
    print(median1)
    median2 = (n+2)//2
    print(median2)
    print("The median of the merged array is ",(merged_array[median1 - 1] + merged_array[median2 - 1])/2)
else:
    print("The median of the merged array is ", merged_array[((n+1)//2)])
