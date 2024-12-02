from image_maker import *
from image_combiner import *
from body import Body
from path import Path
import numpy as np
import time
from vverlet2d import *

def simulate(n, G, num_frames, dt, softening):

    # simulate the bodies
    t0 = time.process_time()

    # E/p tracking
    energy_history = np.zeros(num_frames)
    momentum_history = np.zeros(num_frames)

    body_list = []
    
    # 2 body setup
    '''initial_positions = np.array([[0,0],[1,0]])
    initial_velocities = np.array([[0,0],[0,-10]])
    body_list.append(Body(initial_positions[0],initial_velocities[0],100))
    body_list.append(Body(initial_positions[1],initial_velocities[1],1))'''

    # n body setup
    r = np.random.uniform(9,29,n)
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

    # used to track positions for plotting
    path = Path(num_frames, len(body_list))

    # actual simulation done here
    positions,velocities,accelerations,mass_vector, mass_products = setup_verlet(body_list)
    for frame in range(num_frames):
        print("Simulating frame " + str(frame) + "/" + str(num_frames))
        total_energy, total_momentum, positions, velocities, accelerations = step(positions,velocities,accelerations,dt,G,mass_vector,mass_products, softening)
        update_path(path,positions, frame)
        update_energy_history(energy_history,total_energy, frame)
        update_momentum_history(momentum_history,total_momentum, frame)
    t1 = time.process_time()
    print("Simulation time: "+ str(t1-t0) + "s")    

    # generate the images
    t0 = time.process_time()
    size_list = create_size_list(body_list)
    filenames = make_images(path, num_frames, momentum_history, size_list)
    t1 = time.process_time()
    print("Drawing time: "+ str(t1-t0) + "s")

    # combine the images
    t0 = time.process_time()
    image_combiner(filenames)
    t1 = time.process_time()
    print("Combining time: "+ str(t1-t0) + "s")
    

def update_path(path, body_positions, frame):
    path.x[frame] = body_positions
    path.y[frame] = body_positions


def update_energy_history(energy_history,total_energy, frame):
    energy_history[frame] = total_energy

def update_momentum_history(momentum_history, total_momentum, frame):
    momentum_history[frame] = total_momentum

def create_size_list(body_list):
    size_list = np.array([body.size for body in body_list])
    return size_list

# n orbiters, G, num_frames, dt, softening
simulate(300, 1, 200, 0.01, 0.2)