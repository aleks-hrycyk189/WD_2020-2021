import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
zadanie2 = pd.read_excel(xlsx, header=0)
print(zadanie2)

grupa = zadanie2.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar(color="green")
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()