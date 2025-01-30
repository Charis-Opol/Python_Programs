array = [10,20,30,40,50]
print("Original array:", array)
num_in = int(input("Enter a number to insert at the beginning: "))
array.insert(0, num_in)
num_out = int(input("Enter the number you want to remove from the array: "))

if num_out in array:
    array.remove(num_out)

print("Updated list:", array)
