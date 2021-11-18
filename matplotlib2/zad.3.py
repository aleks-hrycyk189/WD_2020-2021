import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

figura = plt.figure()
ax = figura.gca(projection='3d')

# wykres 1
# X = np.arange(-9, 9, 0.5)
# Y = np.arange(-9, 9, 0.5)
# X, Y = np.meshgrid(X,Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 2
# X = np.arange(-10, 10, 0.5)
# Y = np.arange(-8, 8, 0.5)
# X, Y = np.meshgrid(X,Y)
# R = np.sqrt(X**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.summer, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 3
# X = np.arange(-10, 10, 0.5)
# Y = np.arange(-2, 28, 0.25)
# X, Y = np.meshgrid(X,Y)
# R = np.sqrt(Y**2)
# Z = np.cos(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.YlGnBu, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 4
# X = np.arange(-10, 10, 0.25)
# Y = np.arange(-8, 8, 0.25)
# X, Y = np.meshgrid(X,Y)
# R = np.sqrt(X**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.Pastel1, linewidth=0, antialiased=False)
#
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 5
X = np.arange(-10, 10, 0.25)
Y = np.arange(-8, 8, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap=cm.Wistia, linewidth=0, antialiased=False)

ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figura.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
