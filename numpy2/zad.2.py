import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[-1, -2, -3, -4], [7, 6, 2, 4], [4, -9, 6, 7], [-3, 6, 2, -1]])


print(a)
print(b)
print(a.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))


