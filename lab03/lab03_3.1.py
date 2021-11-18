a = []
for x in range(1,11,1):
    a.append(1-x)
print(a)

b = []
for y in range(7):
    b.append(4**y)
print(b)

c = []
for z in b:
    if z % 2 == 0:
        c.append(z)
print(c)