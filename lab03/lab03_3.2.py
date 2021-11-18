lista1 = []
lista2 = []
import random

z = 0
while z != 10:
    lista1.append((random.randint(0, 100)))
    z += 1

print(lista1)

for z in lista1:
    if z % 2 == 0:
        lista2.append(z)

print(lista2)