import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from math import *

a = np.arange(0, 30, 0.1)
b = np.sin(a)
c = np.cos(a)
plt.plot(a, b, 'b', label='sin(x)')
plt.plot(a, c, 'g', label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x) i cos(x)')
plt.title("Wykres funkcji sin(x) i cos(x) dla x[0,30]")
plt.show()