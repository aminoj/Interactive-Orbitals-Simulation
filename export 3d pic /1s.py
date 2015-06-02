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

x = (1)*np.outer(np.cos(u), np.sin(v))
y = (1)*np.outer(np.sin(u), np.sin(v))
z = (1)*np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, rstride = rstride, cstride = cstride, color=(0.8,0,0), linewidth=0)

plt.show()
ax.set_xlim3d(MinBound, MaxBound)
ax.set_ylim3d(MinBound, MaxBound)
ax.set_zlim3d(MinBound, MaxBound)


e = 0
b = 0
for ii in xrange(0,120,1):
    ax.view_init(elev=e, azim=b*4)
    if(ii < 10) :
        plt.savefig("1s/movie00%s.png" %ii)
    elif(ii < 100):
        plt.savefig("1s/movie0%s.png" %ii)
    else : 
    	plt.savefig("1s/movie%s.png" %ii)
    if(ii  == 20 or ii  == 40 or ii  == 60 or ii  == 80 or ii  == 100):
    	e = e + 12
    	b = 0
    b = b + 1