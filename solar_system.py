import numpy as np
from simulation import *

def solar_system(n,G,num_frames,dt,softening):
    body_list = []
 
    # n body setup
    r = np.random.uniform(2,39,n)
    theta = np.random.uniform(0,2*np.pi,n)

    initial_positions = np.zeros((n,2))
    initial_velocities = np.zeros_like(initial_positions)

    # rotation of cloud
    for i in range(n): 
        initial_positions[i] = r[i]*np.array([np.cos(theta[i]), np.sin(theta[i])])
        if np.pi/2 > theta[i] > 0:
            initial_velocities[i] = (150/np.sqrt(r[i]))*np.array([-1*np.sin(theta[i]),np.cos(theta[i])])
        elif np.pi > theta[i] > np.pi/2:
            initial_velocities[i] = (150/np.sqrt(r[i]))*np.array([-1*np.cos(theta[i]-np.pi/2),-1*np.sin(theta[i]-np.pi/2)])
        elif 1.5*np.pi > theta[i] > np.pi:
            initial_velocities[i] = (150/np.sqrt(r[i]))*np.array([np.sin(theta[i]-np.pi),-1*np.cos(theta[i]-np.pi)])
        else:
            initial_velocities[i] = (150/np.sqrt(r[i]))*np.array([np.cos(theta[i]-1.5*np.pi),np.sin(theta[i]-1.5*np.pi)])

    # creates bodies from initial positions
    for i in range(n):
        body_list.append(Body(initial_positions[i],initial_velocities[i],1,1))

    #Central body
    body_list.append(Body([0,0],[0,0],22500,50))

    simulate(n,G,num_frames,dt,softening,body_list)