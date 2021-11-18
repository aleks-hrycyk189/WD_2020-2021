import sys
plik1 = open("plik1.txt","r")
odczyt = []

odczyt = plik1.readlines()

plik1.close()

print(odczyt)