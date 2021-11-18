import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# cz1 = df[df['Plec'] == 'K'].agg({'Liczba': ['sum']})
# cz1 = cz1['Liczba'].values[0]
# cz2 = df[df['Plec'] == 'M'].agg({'Liczba': ['sum']})
# cz2 = cz2['Liczba'].values[0]
# dane = [cz1, cz2]
# etykiety = ['Kobiety', 'Mezczyzni']
# plt.title("Plec")
# wykres = plt.bar(etykiety, dane)

# a = df[df['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': ['sum']})
# b = df[df['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': ['sum']})
# plt.subplot(1, 3, 2)
# plt.xlabel('Rok')
# plt.ylabel('Liczba')
# plt.title("Liczba urodzonych osob według płci: ")
# plt.plot(a)
# plt.plot(b)

c = df.groupby(['Rok']).agg({'Liczba': ['sum']})
plt.subplot(1, 3, 3)
plt.xlabel('Rok')
plt.ylabel('Suma')
plt.title("Suma urodzonych dzieci w danym roku: ")
c.plot.bar(color=['black'])
plt.show()