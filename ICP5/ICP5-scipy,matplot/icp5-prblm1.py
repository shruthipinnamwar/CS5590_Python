import numpy as np
import matplotlib.pyplot as mpl

# Create 2 arraysas given in the problem
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
mpl.plot(x, y, 'bo')
mpl.show()  #initial values

# y = mx + b
# Find m (slope)
meanx = np.mean(x)  # mean of x
meany = np.mean(y)  # Mean of y
i = 0  
n = 0  
d = 0
while i < len(x):  #looping x array
    # using formula from the ppt
    n += (x[i] - meanx) * (y[i] - meany)
    d += (x[i] - meanx) * (x[i] - meany)
    i += 1
m = round(n/d, 2)

b = 1 #y intercept

print(len(y))
y2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
j = 0  

while j < len(y):
    y2[j] = (m * x[j]) + b
    j += 1

mpl.plot(x, y, 'bo')
mpl.plot(x, y2)
mpl.show()
print(x, y2) #printing the final values using matplot
