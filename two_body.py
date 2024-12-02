import numpy as np
from simulation import *

def two_body(n,G,num_frames,dt,softening):
    body_list = []
    initial_positions = np.array([[0,0],[1,0]])
    initial_velocities = np.array([[0,0],[0,-10]])
    body_list.append(Body(initial_positions[0],initial_velocities[0],100,10))
    body_list.append(Body(initial_positions[1],initial_velocities[1],1, 10))

    simulate(n,G,num_frames,dt,softening,body_list)