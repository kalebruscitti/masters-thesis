import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def f(r,t):
    z = t/r
    return z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = np.linspace(-5, 5, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r,p)

Z = f(R,1)

X,Y = R*np.cos(P), R*np.sin(P)

ax.plot_surface(X,Y,Z)

ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

plt.show()
