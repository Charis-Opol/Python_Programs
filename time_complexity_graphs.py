import math 
import matplotlib.pyplot as plt
import numpy as np

time_complexities = []
inputs = []
for i in range (1, 101):
    answer = i * math.log10(i)
    time_complexities.append(answer)
    inputs.append(i)


print(time_complexities)
print(inputs)

x = np.array(inputs)
y = np.array(time_complexities)
plt.plot(x , y, marker = 'o', linestyle = '-', color = 'b', label = 'Data')

plt.xlabel("Input size")
plt.ylabel("Time complexity")
plt.title("Line graph showing the nature of the quarsi-logarithmic time complexity")
plt.legend

plt.show