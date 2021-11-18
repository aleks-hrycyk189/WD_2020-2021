import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import xlrd
import openpyxl

zadanie = pd.read_csv('zamowienia.csv', delimiter=';')
wykres = zadanie.groupby(['Sprzedawca']).size()
wykres2 = wykres.plot.pie(subplots=True, autopct='%.f %%', fontsize=18, explode=[0, 0.1, 0, 0.3, 0.2, 0, 0, 0, 0], shadow=True)
plt.show()