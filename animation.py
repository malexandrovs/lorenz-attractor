import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint
import mpl_toolkits.mplot3d.axes3d as p3


rho = 28.0
sigma = 10.0
beta = 8.0/3.0

def f(state, t):
  x, y, z = state
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

t0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 100.0, 0.01)

coords = odeint(f, t0, t)
print(np.shape(coords))



########### Here come the Graphics ############
fig = plt.figure()
ax = p3.Axes3D(fig)
#ax = fig.gca(projection='3d')
plot, = ax.plot([], [] ,[])


ax.set_xlim3d([0.0, 60.0])
ax.set_ylim3d([0.0, 60.0])
ax.set_zlim3d([0.0, 60.0])


def init():
    plot.set_data([], [], [])
    return plot,

def animate(i):
    plot.set_data(coords[0:2,:i])
    plot.set_3d_properties(coords[2, :i])
    return plot,

anim = animation.FuncAnimation(fig, animate, init_func=init,
        frames=np.shape(coords)[0],
        interval=5, blit=True)
'''
fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot(coords[:,0], coords[:,1], coords[:,2])
ax = plt.axes()
ax.plot(states[:,0],states[:,2])
'''
plt.show()
