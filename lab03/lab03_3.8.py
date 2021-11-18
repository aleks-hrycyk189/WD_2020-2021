def zakupy(** lista):
    koszt = 0
    liczba_prod = 0
    for a in lista:
        liczba_prod = liczba_prod + 1
        koszt += lista[a]
    print("Wartosc produktow to: " + str(koszt) + " a liczba produktow wynosi: " + str(liczba_prod))
zakupy(chleb = 4, nabial = 11.5, szynka = 12, banan = 4 )