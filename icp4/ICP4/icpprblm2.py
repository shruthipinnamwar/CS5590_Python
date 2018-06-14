import numpy as np

a = np.random.random((10, 10))  # Create random array

print("The maximum is " + str(a.max(axis=1)))
print("The minimum is " + str(a.min(axis=1)))   