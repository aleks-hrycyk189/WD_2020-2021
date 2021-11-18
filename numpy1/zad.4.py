import numpy as np

def zadanie(podstawa, operacja):
    zad = [podstawa**x for x in range(1,operacja+1)]
    return zad


podstawa = input("Podaj liczbe jako podstawe: ")
podstawa = int(podstawa)
operacja = input("Podaj liczbe jak liczbe operacji: ")
operacja = int(operacja)
print(zadanie(podstawa,operacja))

