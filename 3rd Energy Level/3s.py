from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rstride = 5
cstride = 5
MinBound = -3
MaxBound = 3
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)


#SPHERE

x = (1.5)*np.outer(np.cos(u), np.sin(v))
y = (1.5)*np.outer(np.sin(u), np.sin(v))
z = (1.5)*np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, rstride = rstride, cstride = cstride, color=(0,0.8,0), linewidth=0)

plt.show()
ax.set_xlim3d(MinBound, MaxBound)
ax.set_ylim3d(MinBound, MaxBound)
ax.set_zlim3d(MinBound, MaxBound)