import numpy as np
from simulation import *

def two_body(n,G,num_frames,dt,softening,trail_length):
    body_list = []
    initial_positions = np.array([[1,0],[-1,0]])
    initial_velocities = np.array([[0,2],[0,-2]])
    body_list.append(Body(initial_positions[0],initial_velocities[0],25,20))
    body_list.append(Body(initial_positions[1],initial_velocities[1],25,20))

    simulate(n,G,num_frames,dt,softening,body_list, trail_length)