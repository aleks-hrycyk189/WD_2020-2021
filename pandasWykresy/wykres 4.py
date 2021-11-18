import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


zadanie4 = pd.read_csv('zamowienia.csv', delimiter=';')
wykres = zadanie4.groupby('Sprzedawca').size()
wykres.plot.bar()
plt.ylabel("liczba zamówień")
plt.show()