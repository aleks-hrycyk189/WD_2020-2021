class ciagArytmetyczny:
    """Obliczanie elementow ciagu"""
    def __init__(self, wyraz_a1, roznica_r, wyraz_an):
        self.wyraz_a1 = wyraz_a1
        self.roznica_r = roznica_r
        self.wyraz_an = wyraz_an
    def wyswietl_dane(self):
        info = "Dane to: pierwszy wyraz wynosi :" + self.wyraz_a1 + " ,a roznica wynosi : " + self.roznica_r
        return info
    def pobierz_parametry(self):
        an = int(self.wyraz_a1) + (int(self.wyraz_an) - 1) * int(self.roznica_r)
        info = "Wyraz " + self.wyraz_an + " wynosi: " + str(an)
        return info
    def policz_sume(self):
        suma = 0.5 * ((2 * int(self.wyraz_a1) + ((int(self.wyraz_an) -1 )) * int(self.roznica_r)) * int(self.wyraz_an))
        info = "Suma wynosi: " + str(suma)
        return info

a = input("Podaj pierwszy wyraz: ")
b = input("Podaj roznice: ")
c = input("Podaj, ktory wyraz chcesz obliczyc: ")
ciag = ciagArytmetyczny(a,b,c)
print(ciag.wyswietl_dane())
print(ciag.pobierz_parametry())
print(ciag.policz_sume())




