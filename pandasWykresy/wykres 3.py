import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
zadanie3 = pd.read_excel(xlsx, header=0)
print(zadanie3)

grupa = zadanie3[zadanie3['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.show()