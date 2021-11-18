import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10000)

def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

figura = plt.figure()
ax = figura.add_subplot(111, projection='3d')
n = 50
# wykres 1
# for c, m, zlow, zhigh in [('r', 'o', -60, -25), ('b', '^', -50, -5)]:
#     xs = randrange(n,23, 32)
#     ys = randrange(n, 0, 86)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

# wykres 2
# for c, m, zlow, zhigh in [('darkorange', 'p', -60, 25), ('springgreen', '1', -50, -5)]:
#     xs = randrange(n,23, 32)
#     ys = randrange(n, 0, 86)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

# wykres 3
# for c, m, zlow, zhigh in [('slategrey', 'X', -60, 25), ('darkblue', '$...$', -50, -5)]:
#     xs = randrange(n,23, 32)
#     ys = randrange(n, 0, 86)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

#  wykres 4
# for c, m, zlow, zhigh in [('gold', 'v', -98, -45), ('darkblue', '>', -70, -45)]:
#     xs = randrange(n,23, 32)
#     ys = randrange(n, 0, 86)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

# wykres 5
for c, m, zlow, zhigh in [('brown', '8', -98, -45), ('indigo', '*', -70, -45)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 86)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
