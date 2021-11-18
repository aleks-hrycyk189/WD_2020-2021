import numpy as np

def zadanie(n):
    zad = [a*2 for a in range(1, n+1)]
    zm = []
    for a in range(0,n):
        for b in range(0,n):
            d = a-b
            zm.append(zad[d])
    wynik = np.array(zm)
    wynik = wynik.reshape((n,n))
    return wynik


n = input("Podaj liczbe n: ")
n = int(n)
print(zadanie(n))