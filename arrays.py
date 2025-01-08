from array import *
nums = array('i', [45, 324, 654, 45, 264])
print(nums)
for x in nums:
    print(x)
newValue = int(input("Enter number: "))
nums.append(newValue)
print(nums)
nums.reverse()
print(nums)
nums = sorted(nums)
print(nums)
nums.pop()
print(nums)

newArray = array('i', [])
more = int(input("How many times: "))
for i in range(0, more):
    newNum = int(input("Enter the number: "))
    newArray.append(newNum)
nums.extend(newArray)
print(nums)

getrid = int(input("Enter the index of a value you would like to get rid of: "))
nums.remove(getrid)
print(nums)
print(nums.count(45))