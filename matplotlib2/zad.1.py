import numpy as np
import matplotlib
import matplotlib.pyplot as plt

figura = plt.figure()
ax = figura.gca(projection='3d')

z = np.linspace(0, 2*np.pi, 100)
x = np.sin(z)
y = np.cos(z) * 2

ax.plot(x, y, z, label='zadanie 1')
ax.legend()
plt.show()

