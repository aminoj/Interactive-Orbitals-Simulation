from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rstride = 15
cstride = 15
MaxBound = 3
MinBound = -3
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

#OUTSIDE -ALL DIRECTIONS

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



#-------------------------------------------------------------------------------

#INSIDE - ALL DIRECTIONS

#-------------------------------------------------------------------------------
#Right-Inner Outer                   

x6 = 0.5*np.outer(np.cos(u), np.sin(v))
z6 = 0.5*np.outer(np.sin(u), np.sin(v))
y6 = 0.2*np.cos(u) +1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Inner Outer

x7 = 0.5*np.outer(np.cos(u), np.sin(v))
z7 = 0.5*np.outer(np.sin(u), np.sin(v))
y7 = 0.2*np.cos(u) +1

ax.plot_surface(x7, -y7, z7, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------

#Right-Inner Inner

x8 = 0.5*np.outer(np.cos(u), np.sin(v))
z8 = 0.5*np.outer(np.sin(u), np.sin(v))
y8 = abs((x8)**2 + (z8)**2 - 5)**(0.5)-1.4

ax.plot_surface(x8, y8, z8, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Inner Inner

x8 = 0.5*np.outer(np.cos(u), np.sin(v))
z8 = 0.5*np.outer(np.sin(u), np.sin(v))
y8 = abs((x8)**2 + (z8)**2 - 5)**(0.5)-1.4

ax.plot_surface(x8, -y8, z8, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Right-Inner Outer                   

y6 = 0.5*np.outer(np.cos(u), np.sin(v))
z6 = 0.5*np.outer(np.sin(u), np.sin(v))
x6 = 0.2*np.cos(u) +1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Inner Outer

y7 = 0.5*np.outer(np.cos(u), np.sin(v))
z7 = 0.5*np.outer(np.sin(u), np.sin(v))
x7 = 0.2*np.cos(u) +1

ax.plot_surface(-x7, y7, z7, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------

#Right-Inner Inner

y8 = 0.5*np.outer(np.cos(u), np.sin(v))
z8 = 0.5*np.outer(np.sin(u), np.sin(v))
x8 = abs((y8)**2 + (z8)**2 - 5)**(0.5)-1.4

ax.plot_surface(x8, y8, z8, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Inner Inner

y9 = 0.5*np.outer(np.cos(u), np.sin(v))
z9 = 0.5*np.outer(np.sin(u), np.sin(v))
x9 = abs((y9)**2 + (z9)**2 - 5)**(0.5)-1.4

ax.plot_surface(-x9, y9, z9, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Right-Inner Outer                   

x6 = 0.5*np.outer(np.cos(u), np.sin(v))
y6 = 0.5*np.outer(np.sin(u), np.sin(v))
z6 = 0.2*np.cos(u) +1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Inner Outer

x7 = 0.5*np.outer(np.cos(u), np.sin(v))
y7 = 0.5*np.outer(np.sin(u), np.sin(v))
z7 = 0.2*np.cos(u) +1

ax.plot_surface(x7, y7, -z7, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------

#Right-Inner Inner

x8 = 0.5*np.outer(np.cos(u), np.sin(v))
y8 = 0.5*np.outer(np.sin(u), np.sin(v))
z8 = abs((x8)**2 + (y8)**2 - 5)**(0.5)-1.4

ax.plot_surface(x8, y8, z8, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)

#-------------------------------------------------------------------------------
#Left-Inner Inner

x8 = 0.5*np.outer(np.cos(u), np.sin(v))
y8 = 0.5*np.outer(np.sin(u), np.sin(v))
z8 = abs((x8)**2 + (y8)**2 - 5)**(0.5)-1.4

ax.plot_surface(x8, y8, -z8, rstride = rstride, cstride = cstride, color=(0,1,0.44), linewidth=0)


plt.show()
ax.set_xlim3d(MaxBound, MinBound)
ax.set_ylim3d(MaxBound, MinBound)
ax.set_zlim3d(MaxBound, MinBound)


e = 0
b = 0
for ii in xrange(0,120,1):
    ax.view_init(elev=e, azim=b*4)
    if(ii < 10) :
        plt.savefig("3p/movie00%s.png" %ii)
    elif(ii < 100):
        plt.savefig("3p/movie0%s.png" %ii)
    else : 
    	plt.savefig("3p/movie%s.png" %ii)
    if(ii  == 20 or ii  == 40 or ii  == 60 or ii  == 80 or ii  == 100):
    	e = e + 12
    	b = 0
    b = b + 1