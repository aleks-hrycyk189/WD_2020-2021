import sys

zapis = "\nInformatyka, inzynieria systemow informatycznych, semestr II"

with open("plik2.txt","a+") as plik2:
    plik2.write(zapis)
    for linia in plik2:
        print(linia, end="")


with open("plik2.txt","r") as plik2:
    for linia in plik2:
        print(linia, end="")