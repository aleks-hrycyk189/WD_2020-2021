import numpy as np


def zad(n):
    a = np.empty((n,n))
    a = a.astype('int')
    z = 0
    for i in range(n):
        for j in range(n):
            a[i,j] = (2**z)
            z += 1
    print(a)



n = input("Wprowadz liczbe n: ")
n = int(n)

print(zad(n))




