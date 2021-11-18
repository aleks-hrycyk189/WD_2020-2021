import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
zadanie1 = pd.read_excel(xlsx, header=0)
print(zadanie1)

grupa = zadanie1.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.legend(title='Legenda')
plt.title("Liczba dzieci dla poszczegolnego roku")
plt.show()