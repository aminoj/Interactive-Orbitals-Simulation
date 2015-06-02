from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rstride = 15
cstride = 15
MinBound = -5
MaxBound = 5
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)


#-------------------------------------------------------------------------------

#Cone
x2 = 1.5*np.outer(np.cos(u), np.sin(v))
z2 = 1.5*np.outer(np.sin(u), np.sin(v))
y2 = 1.5*((1.5*x2)**2+(1.5*z2)**2+0.3)**(0.5)

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, linewidth=0, color=(0.8,1,0.8))

#-------------------------------------------------------------------------------
#Cone
x2 = 1.5*np.outer(np.cos(u), np.sin(v))
z2 = 1.5*np.outer(np.sin(u), np.sin(v))
y2 = -1.5*((1.5*x2)**2+(1.5*z2)**2+0.3)**(0.5)

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color= (0.8,1,0.8), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
x6 = 1.5*np.outer(np.cos(u), np.sin(v))
z6 = 1.5*np.outer(np.sin(u), np.sin(v))
y6 = (abs(((2*x6)**2)+((2*z6)**2)-15)**(0.5))+1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0.8,1,0.8), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
x6 = 1.5*np.outer(np.cos(u), np.sin(v))
z6 = 1.5*np.outer(np.sin(u), np.sin(v))
y6 = -(abs(((2*x6)**2)+((2*z6)**2)-15)**(0.5))-1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0.8,1,0.8), linewidth=0)

'--------------------------------------------------------------------------------------------------------------------'

#-------------------------------------------------------------------------------

#Cone
y2 = 1.5*np.outer(np.cos(u), np.sin(v))
z2 = 1.5*np.outer(np.sin(u), np.sin(v))
x2 = 1.5*((1.5*y2)**2+(1.5*z2)**2+0.3)**(0.5)

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, linewidth=0, color=(0.8,1,0.8))

#-------------------------------------------------------------------------------
#Cone
y2 = 1.5*np.outer(np.cos(u), np.sin(v))
z2 = 1.5*np.outer(np.sin(u), np.sin(v))
x2 = -1.5*((1.5*y2)**2+(1.5*z2)**2+0.3)**(0.5)

ax.plot_surface(x2, y2, z2, rstride = rstride, cstride = cstride, color= (0.8,1,0.8), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
y6 = 1.5*np.outer(np.cos(u), np.sin(v))
z6 = 1.5*np.outer(np.sin(u), np.sin(v))
x6 = (abs(((2*y6)**2)+((2*z6)**2)-15)**(0.5))+1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0.8,1,0.8), linewidth=0)

#-------------------------------------------------------------------------------
#Cover
y6 = 1.5*np.outer(np.cos(u), np.sin(v))
z6 = 1.5*np.outer(np.sin(u), np.sin(v))
x6 = -(abs(((2*y6)**2)+((2*z6)**2)-15)**(0.5))-1

ax.plot_surface(x6, y6, z6, rstride = rstride, cstride = cstride, color=(0.8,1,0.8), linewidth=0)

plt.show()
ax.set_xlim3d(MaxBound, MinBound)
ax.set_ylim3d(MaxBound, MinBound)
ax.set_zlim3d(MaxBound, MinBound)

e = 0
b = 0
for ii in xrange(0,120,1):
    ax.view_init(elev=e, azim=b*4)
    if(ii < 10) :
        plt.savefig("3dPart2/movie00%s.png" %ii)
    elif(ii < 100):
        plt.savefig("3dPart2/movie0%s.png" %ii)
    else : 
    	plt.savefig("3dPart2/movie%s.png" %ii)
    if(ii  == 20 or ii  == 40 or ii  == 60 or ii  == 80 or ii  == 100):
    	e = e + 12
    	b = 0
    b = b + 1