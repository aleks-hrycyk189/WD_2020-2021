import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from math import *

x = np.arange(0, 30, 0.1)
b = np.sin(x)
c = np.sin(x*(-1))-2
plt.plot(x, b, 'g', label='sin(x)')
plt.plot(x, c, 'r', label='sin(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x), sin(x)")
plt.show()

# x = np.arange(0, 30, 0.1)
# b = np.sin(x)
# c = np.sin(x*(-1))
# plt.plot(x, b, 'g', label='sin(x)')
# plt.plot(x, c, 'r', label='sin(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title("Wykres sin(x), sin(x)")
# plt.show()
#
# x = np.arange(0, 30, 0.1)
# b = np.sin(x)
# c = np.sin(x*(-1))-1
# plt.plot(x, b, 'g', label='sin(x)')
# plt.plot(x, c, 'r', label='sin(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title("Wykres sin(x), sin(x)")
# plt.show()