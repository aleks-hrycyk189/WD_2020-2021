# zadanie 1
# moje_filmy = ['Pamietnik', 'Nad zycie', 'Przelecz ocalonych', 'Skazani na Shawshank', 'Titanic', 'Krol Lew',
# 'Jeden dzien']
# print(moje_filmy)
# moje_filmy.reverse()
# print(moje_filmy)
# moje_filmy.insert(5,'Czas na milosc')
# moje_filmy.insert(5,'Harry Potter')
# moje_filmy.insert(5,'Forrest Gump')
# print(moje_filmy)

# zadanie 2
# jesli kazdy film, bedzie osobnym skladnikiem to kluczem moze byc nazwisko rezysera
#
# slownik_filmy = { "Cassavetes": "Pamietnik", "A.Plutecka": "Nad zycie", "Gibson": "Przelecz ocalonych",
#                  "Darabont": "Skazani na Shawshank", "Cameron": "Titanic", "Minkoff": "Król Lew",
#                  "Scherfig": "Jeden dzien", "Zemeckis": "Forrest Gump", "Yates": "Harry Potter",
#                  "Curtis": "Czas na milosc" }
# print(slownik_filmy)

# zadanie 3

# semestr_letni = {"CAD komputerowe wspomaganie projektowania": "CAD", "Programowanie struturalne": "PS",
#                  "Wiedza o tearze": "WOT", "Analiza matematyczna dla informatykow": "AM", "Wizualizacja danych": "WD",
#                  "Matematyka Dyskretna dla informatykow": "MD"}
# print(len(semestr_letni))

# zadanie 4

# liczba = input("Wprowadz liczbe na ktorej chcesz wykonac dzialanie: \n")
# liczba = int(liczba)
#
# potega = pow(liczba, liczba)
# print(potega)

# zadanie 5
# program policzy tylko male litery "a", tak jak bylo w zadaniu
# import sys as system
# system.stdout.write("Podaj napis: ")
# napis = system.stdin.readline()
# liczba_a = napis.count('a')
# liczba_a = str(liczba_a)
# system.stdout.write(liczba_a)

# program obliczy wystapienia liczby a jako malej oraz duzej litery
# import sys as system
# system.stdout.write("Podaj napis: ")
# napis = system.stdin.readline()
# liczba_a = napis.count('a')
# liczba_A = napis.count('A')
# liczba_wystapien = liczba_A + liczba_a
# liczba_wystapien = str(liczba_wystapien)
# system.stdout.write(liczba_wystapien)

# zadanie 6
#
# a = input("Wprowadz liczbe a: \n")
# a = int(a)
# b = input("Wprowadz liczbe b: \n")
# b = int(b)
# c = input("Wprowadz liczbe c: \n")
# c = int(c)
#
# if (a%2==0) & (b>c):
#     print("Spelnione warunki zadania")
# else:
#     print("Warunki nie spelnione")


# zadanie 7

# liczby = [1, 3, 5.5, 8, 6.7, 2, 4]
# suma = 0
# wynik= []
# l = len(liczby)
#
# for x in range(1,l,1):
#     suma = liczby[x]+ liczby[x-1]
#     wynik.append(suma)
#     print(wynik)

# zadanie 8
# lista = []
# a = 1
# print(type(a))
# while a <= 10:
#     x = float(input("Podaj liczbe: "))
#     a = a+1
#     if(x- int(x)==0):
#         lista.append(x)
#         print(lista)


# zadanie 9
# lista1 = [1, 2, 3, 4, 5, 6]
# for x in lista1:
#     if (x == 1) | (x == 6):
#         print("O"*6)
#     else:
#         print("O" + ' '* 4 + "O")


# zadanie 10
# print("Podaj liczbe: ")
# liczba = input()
# try:
#     if liczba != int(liczba) :
#         print("Spelnione warunki")
# except ValueError:
#     print("Podano litere")
