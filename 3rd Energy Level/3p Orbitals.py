from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rstride = 14
cstride = 14
MaxBound = 3
MinBound = -3
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)


#-------------------------------------------------------------------------------
#Left-Outer Outer

x2 = np.outer(np.cos(u), np.sin(v))
z2 = np.outer(np.sin(u), np.sin(v))
y2 = -0.4*np.cos(u)-2.05

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Outer Inner

x3 = np.outer(np.cos(u), np.sin(v))
z3 = np.outer(np.sin(u), np.sin(v))
y3 = abs((x3)**2 + (z3)**2 + 5)**(0.5)-4.1

ax.plot_surface(x3, y3, z3, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)


#-------------------------------------------------------------------------------
#Right-Outer Outer

x4 = np.outer(np.cos(u), np.sin(v))
z4 = np.outer(np.sin(u), np.sin(v))
y4 = 0.4*np.cos(u)+2.05

ax.plot_surface(x4, y4, z4, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Right-Outer  Inner

x5 = np.outer(np.cos(u), np.sin(v))
z5 = np.outer(np.sin(u), np.sin(v))
y5 = abs((x5)**2 + (z5)**2 - 5)**(0.5)-0.35

ax.plot_surface(x5, y5, z5, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)



#-------------------------------------------------------------------------------
#DIFFERENT DIRECTION
#-------------------------------------------------------------------------------
#Left-Outer Outer

y2 = np.outer(np.cos(u), np.sin(v))
z2 = np.outer(np.sin(u), np.sin(v))
x2 = -0.4*np.cos(u)-2.07

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Outer Inner

y3 = np.outer(np.cos(u), np.sin(v))
z3 = np.outer(np.sin(u), np.sin(v))
x3 = abs((y3)**2 + (z3)**2 + 5)**(0.5)-4.1

ax.plot_surface(x3, y3, z3, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)


#-------------------------------------------------------------------------------
#Right-Outer Outer

y4 = np.outer(np.cos(u), np.sin(v))
z4 = np.outer(np.sin(u), np.sin(v))
x4 = 0.4*np.cos(u)+2.07

ax.plot_surface(x4, y4, z4, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Right-Outer  Inner

y5 = np.outer(np.cos(u), np.sin(v))
z5 = np.outer(np.sin(u), np.sin(v))
x5 = abs((y5)**2 + (z5)**2 - 5)**(0.5)-0.35

ax.plot_surface(x5, y5, z5, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)




#-------------------------------------------------------------------------------
#DIFFERENT DIRECTION
#-------------------------------------------------------------------------------
#Left-Outer Outer

y2 = np.outer(np.cos(u), np.sin(v))
x2 = np.outer(np.sin(u), np.sin(v))
z2 = -0.4*np.cos(u)-2.07

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Outer Inner

y3 = np.outer(np.cos(u), np.sin(v))
x3 = np.outer(np.sin(u), np.sin(v))
z3 = abs((x3)**2 + (y3)**2 + 5)**(0.5)-4.1

ax.plot_surface(x3, y3, z3, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)


#-------------------------------------------------------------------------------
#Right-Outer Outer

x4 = np.outer(np.cos(u), np.sin(v))
y4 = np.outer(np.sin(u), np.sin(v))
z4 = 0.4*np.cos(u)+2.07

ax.plot_surface(x4, y4, z4, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Right-Outer  Inner

x5 = np.outer(np.cos(u), np.sin(v))
y5 = np.outer(np.sin(u), np.sin(v))
z5 = abs((x5)**2 + (y5)**2 - 5)**(0.5)-0.35

ax.plot_surface(x5, y5, z5, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)




plt.show()
ax.set_xlim3d(MaxBound, MinBound)
ax.set_ylim3d(MaxBound, MinBound)
ax.set_zlim3d(MaxBound, MinBound)
