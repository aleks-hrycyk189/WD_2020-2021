def trojkat_pros(bok1, bok2, bok3):
    if (bok1**2 + bok2**2 == bok3**2) | (bok1**2 + bok3**2 == bok2**2) | (bok2**2 + bok3**2 == bok1**2):
        print("Trojkat jest prostokatny ")
        return 1
    else:
        print("Trojakt nie jest prostokatny ")
        return 0

bok1 = input("Podaj bok1: ")
bok1 = int(bok1)
bok2 = input("Podaj bok2: ")
bok2 = int(bok2)
bok3 = input("Podaj bok3: ")
bok3 = int(bok3)

print(trojkat_pros(bok1, bok2, bok3))
