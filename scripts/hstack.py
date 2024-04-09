import numpy as np

x = np.arange(10).reshape(5, 2)
y = np.arange(100, 120).reshape(5, 4)

print(np.hstack((x, y)))