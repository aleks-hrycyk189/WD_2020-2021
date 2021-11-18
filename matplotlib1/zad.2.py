import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

y = [1/y for y in range(1, 21)]
x = [x for x in range(1,21)]
plt.plot(x, y, 'g^--', label='f(x)=(1/x)')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title("Wykres funkcji")
plt.show()