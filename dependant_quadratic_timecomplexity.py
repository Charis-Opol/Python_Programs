import pandas as pd

i = 1
n = int(input("Enter the number of iterations you want: "))
count = 0
array1 = []
array2 = []
while i <= n:
    j = 1
    while j <= i:
        print("God is good")
        j = j + 1
        count += 1
        array2.append(count)
    array1.append(i)
    i = i + 1

print(array1)
print(array2)
