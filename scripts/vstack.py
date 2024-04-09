import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.zeros(5)
c = np.vstack((a, b))
c = c.T
print(c.ravel())