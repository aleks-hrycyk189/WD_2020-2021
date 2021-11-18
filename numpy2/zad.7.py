import numpy as np

zm = np.array([[1, 4, 6], [2.3, 0.5, 3.6]])
a = np.sin(zm)


zm1 = np.array([[1, 4, 6], [2.3, 0.5, 3.6]])
b = np.cos(zm1)


c = a + b
print(c)