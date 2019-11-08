import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint
import mpl_toolkits.mplot3d.axes3d as p3


########### Here come the Maths part #############

# set parameters
rho = 27.0
sigma = 10.0
beta = 8.0/3.0

# define set of ODEs
def f(state, t):
  x, y, z = state
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

# set initial conditions
t0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 100.0, 0.001)

# compute 10000 values
coords = odeint(f, t0, t).T



########### Here come the Graphics ############

#create figure
fig = plt.figure()
ax = p3.Axes3D(fig)
plot, = ax.plot([], [] ,[])


def init():
    plot.set_data([], [])
    return plot,

# define which data is used for the animation
def animate(i):
    plot.set_data(coords[0:2,:40*i])
    plot.set_3d_properties(coords[2, :40*i])
    return plot,

# start the animation
anim = animation.FuncAnimation(fig, animate, 
        frames=np.shape(coords)[1],
        interval=1, blit=False)

ax.set_ylim(-30,30)
ax.set_xlim(-20,20)
ax.set_zlim(-15,50)
plt.show()
