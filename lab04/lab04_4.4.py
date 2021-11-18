class NaZakupy:
    """Lista zakupow"""
    # nazwa_produktu = input("Podaj nazwe produktu: ")
    # ilosc = input("Podaj ilosc: ")
    # jednostka_miary = input("Podaj w jakiej jednostce miary kupowany jest produkt: ")
    # cena_jed = input("Podaj cene jednostkowa produktu: ")
    def __init__(self,nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        informacja = self.nazwa_produktu + "  ilosc: " + self.ilosc + " cena_jed: " + self.cena_jed
        return informacja
    def ile_produktu(self):
        return self.ilosc + " " + self.jednostka_miary
    def ile_kosztuje(self):
        koszt = int(self.ilosc) * float(self.cena_jed)
        return "Koszt za zakupy to : " + str(koszt) + " zl"

marchewka = NaZakupy("marchewka","3","szt","2.5")

print(marchewka.wyswietl_produkt())
print(marchewka.ile_produktu())
print(marchewka.ile_kosztuje())



