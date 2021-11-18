def iloczyn_ciagu(a=1, b=4, ile=10):
    wynik = []
    for x in range(0,ile,1):
        a = a * b
        wynik.append(a)
    return wynik

print(iloczyn_ciagu())