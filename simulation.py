from gif_maker import *
from body import Body
import numpy as np



def simulate(n, plot_trails):
    body_list = []
    positions = np.random.multivariate_normal([0,0],[[1,0],[0,1]],n)
    velocities = 5*np.random.multivariate_normal([0,0],[[1,0],[0,1]],n)
    for i in range(n):
        body_list.append(Body(positions[i],velocities[i],1))
    make_gif(body_list, plot_trails)
    
simulate(20, False)