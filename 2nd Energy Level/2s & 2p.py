from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rstride = 15
cstride = 15
MinBound = -3
MaxBound = 3
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)


#-------------------------------------------------------------------------------
#Cone
x2 = np.outer(np.cos(u), np.sin(v))
y2 = np.outer(np.sin(u), np.sin(v))
z2 = ((1.5*x2)**2+(1.5*y2)**2+0.3)**(0.5)

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cone
x2 = np.outer(np.cos(u), np.sin(v))
y2 = np.outer(np.sin(u), np.sin(v))
z2 = -((1.5*x2)**2+(1.5*y2)**2+0.3)**(0.5)

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cone
y4 = np.outer(np.sin(u), np.sin(v))
z4 = np.outer(np.cos(u), np.sin(v))
x4 = ((1.5*z4)**2+(1.5*y4)**2+0.3)**(0.5)

ax.plot_surface(x4, y4, z4, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)


#-------------------------------------------------------------------------------
#Cone
y4 = np.outer(np.sin(u), np.sin(v))
z4 = np.outer(np.cos(u), np.sin(v))
x4 = -((1.5*z4)**2+(1.5*y4)**2+0.3)**(0.5)

ax.plot_surface(x4, y4, z4, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)


#-------------------------------------------------------------------------------
#Cone
z5 = np.outer(np.cos(u), np.sin(v))
x5 = np.outer(np.sin(u), np.sin(v))
y5 = ((1.5*z5)**2+(1.5*x5)**2+0.3)**(0.5)

ax.plot_surface(x5, y5, z5, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cone
z5 = np.outer(np.cos(u), np.sin(v))
x5 = np.outer(np.sin(u), np.sin(v))
y5 = -((1.5*z5)**2+(1.5*x5)**2+0.3)**(0.5)

ax.plot_surface(x5, y5, z5, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
x6 = np.outer(np.cos(u), np.sin(v))
y6 = np.outer(np.sin(u), np.sin(v))
z6 = (abs(((2*x6)**2)+((2*y6)**2)-15)**(0.5))-1.7

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
x6 = np.outer(np.cos(u), np.sin(v))
y6 = np.outer(np.sin(u), np.sin(v))
z6 = -(abs(((2*x6)**2)+((2*y6)**2)-15)**(0.5))+1.7

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)


#-------------------------------------------------------------------------------
#Cover
y7 = np.outer(np.sin(u), np.sin(v))
z7 = np.outer(np.cos(u), np.sin(v))
x7 = (abs(((2*x6)**2)+((2*y6)**2)-15)**(0.5))-1.7

ax.plot_surface(x7, y7, z7, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)


#-------------------------------------------------------------------------------
#Cover
z7 = np.outer(np.cos(u), np.sin(v))
y7 = np.outer(np.sin(u), np.sin(v))
x7 = -(abs(((2*z7)**2)+((2*y7)**2)-15)**(0.5))+1.7

ax.plot_surface(x7, y7, z7, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
x8 = np.outer(np.cos(u), np.sin(v))
z8 = np.outer(np.sin(u), np.sin(v))
y8 = (abs(((2*x8)**2)+((2*z8)**2)-15)**(0.5))-1.7

ax.plot_surface(x8, y8, z8, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)

#-------------------------------------------------------------------------------
#Cover

x8 = np.outer(np.cos(u), np.sin(v))
z8 = np.outer(np.sin(u), np.sin(v))
y8 = -(abs(((2*x8)**2)+((2*z8)**2)-15)**(0.5))+1.7

ax.plot_surface(x8, y8, z8, rstride = rstride, cstride = cstride, color=(0,0.44,1), linewidth=0)


#-------------------------------------------------------------------------------
#SPHERE

x = (0.8)*np.outer(np.cos(u), np.sin(v))
y = (0.8)*np.outer(np.sin(u), np.sin(v))
z = (0.8)*np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, rstride = rstride, cstride = cstride, color=(0,0,0.8), linewidth=0)

plt.show()
ax.set_xlim3d(MinBound, MaxBound)
ax.set_ylim3d(MinBound, MaxBound)
ax.set_zlim3d(MinBound, MaxBound)
