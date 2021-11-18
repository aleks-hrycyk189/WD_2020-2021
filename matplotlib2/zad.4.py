import numpy as np
import matplotlib.pyplot as plt

figura = plt.figure(figsize=(8, 3))
ax1 = figura.add_subplot(121, projection='3d')
ax2 = figura.add_subplot(122, projection='3d')

# wykres 1
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y =_xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax1.set_title('Wykres nie zacieniony')

# wykres 2
# _x = np.arange(7)
# _y = np.arange(8)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y =_xx.ravel(), _yy.ravel()
# top = x - y
# bottom = np.zeros_like(top)
# width = depth = 2
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax1.set_title('Wykres nie zacieniony')

# wykres 3

# _x = np.arange(5)
# _y = np.arange(10)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y =_xx.ravel(), _yy.ravel()
# top = x * y
# bottom = np.zeros_like(top)
# width = depth = 0.5
# ax1.bar3d(x, y, bottom, width, depth, top, color='indianred', shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax1.set_title('Wykres nie zacieniony')

# wykres 4
# _x = np.arange(2)
# _y = np.arange(10)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y =_xx.ravel(), _yy.ravel()
# top = x * y
# bottom = x - y
# width = depth = 0.5
# ax1.bar3d(x, y, bottom, width, depth, top, color='moccasin', shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, color='moccasin', shade=False)
# ax1.set_title('Wykres nie zacieniony')

# wykres 5

_x = np.arange(10)
_y = np.arange(10)
_xx, _yy = np.meshgrid(_x, _y)
x, y =_xx.ravel(), _yy.ravel()
top = x * y
bottom = x + y
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, color='moccasin', shade=True)
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, color='moccasin', shade=False)
ax1.set_title('Wykres nie zacieniony')

plt.show()