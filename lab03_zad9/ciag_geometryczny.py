def wyraz_ciagu(a1,n,q):
    potega = n - 1
    an = a1 * q**potega
    return an

def suma_ciagu(a1,n,q):
    mnozenie = (1 - q**n) / (1 - q)
    suma = a1 * mnozenie
    return suma