# zadanie 1
# a = []
# for x in range(1,11,1):
#     a.append(1-x)
# print(a)
#
# b = []
# for y in range(7):
#     b.append(4**y)
# print(b)
#
# c = []
# for z in b:
#     if z % 2 == 0:
#         c.append(z)
# print(c)

# zadanie 2
# lista1 = []
# lista2 = []
# import random
#
# z = 0
# while z != 10:
#     lista1.append((random.randint(0, 100)))
#     z += 1
#
# print(lista1)
#
# for z in lista1:
#     if z % 2 == 0:
#         lista2.append(z)
#
# print(lista2)

# zadanie 3
# prod_spoz={"maslo": "szt",
#            "mleko": "ml",
#            "chleb": "szt",
#            "banany": "kg",
#            "szynka": "dag",
#            "kukurydza": "puszka",
#            "jogurt": "szt"}
#
# prod_szt = {}
#
# for key, value in prod_spoz.items():
#     if value == "szt":
#         prod_szt = {key, value}
#
#         print(prod_szt)

# zadanie 4
# def trojkat_pros(bok1, bok2, bok3):
#     if (bok1**2 + bok2**2 == bok3**2) | (bok1**2 + bok3**2 == bok2**2) | (bok2**2 + bok3**2 == bok1**2):
#         print("Trojkat jest prostokatny ")
#         return 1
#     else:
#         print("Trojakt nie jest prostokatny ")
#         return 0
#
# bok1 = input("Podaj bok1: ")
# bok1 = int(bok1)
# bok2 = input("Podaj bok2: ")
# bok2 = int(bok2)
# bok3 = input("Podaj bok3: ")
# bok3 = int(bok3)
#
# print(trojkat_pros(bok1, bok2, bok3))

# zadanie 5
# def pole_trapezu(pod1 = 4, pod2 = 6, wys = 5):
#     pole = ((pod1 + pod2) * wys)/2
#     return pole
# print(pole_trapezu())

# zadanie 6
# def iloczyn_ciagu(a=1, b=4, ile=10):
#     wynik = []
#     for x in range(0,ile,1):
#         a = a * b
#         wynik.append(a)
#     return wynik
#
# print(iloczyn_ciagu())


# zadanie 7
# def iloczyn_ciagu(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for a in liczby:
#             iloczyn *= a
#         return iloczyn
# print(iloczyn_ciagu())
# print(iloczyn_ciagu(4,8,12,3))

# zadanie 8

# def zakupy(** lista):
#     koszt = 0
#     liczba_prod = 0
#     for a in lista:
#         liczba_prod = liczba_prod + 1
#         koszt += lista[a]
#     print("Wartosc produktow to: " + str(koszt) + " a liczba produktow wynosi: " + str(liczba_prod))
# zakupy(chleb = 4, nabial = 11.5, szynka = 12, banan = 4 )

