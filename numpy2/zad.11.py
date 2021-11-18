import numpy as np

vec = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(vec.reshape(4, 3))
# print(vec.reshape(3, 4))
# print(vec.reshape(2, 6))
a = vec.reshape(4, 3)
print(a)
a1 = a.ravel()
print(a1)

b = vec.reshape(3, 4)
print(a)
b1 = b.ravel()
print(b1)

c = vec.reshape(2, 6)
print(a)
c1 = c.ravel()
print(c1)





