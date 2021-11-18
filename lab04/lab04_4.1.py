import sys

plik1 = open('plik1.txt','w')
x = []
y = []
for a in range(31):
    x.append(a)

   # y.append(a)
for a in x:
    a = a * 2
    y.append(a)

print(y)


plik1.writelines(str(y))
plik1.close()