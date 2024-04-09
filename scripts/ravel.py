import numpy as np

array = np.arange(0, 6, 0.5)
array = array.reshape((2, 6))
array = np.ravel(array)
print(array)