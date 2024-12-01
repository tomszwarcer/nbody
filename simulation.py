from image_maker import *
from image_combiner import *
from body import Body
import numpy as np
import time
from vverlet2d import *

def simulate(n, G, num_frames, dt, softening):

    # simulate the bodies
    t0 = time.process_time()

    energy_history = np.zeros(num_frames)
    momentum_history = np.zeros(num_frames)

    body_list = []
    
    '''initial_positions = np.array([[0,0],[1,0]])
    initial_velocities = np.array([[0,0],[0,-10]])
    body_list.append(Body(initial_positions[0],initial_velocities[0],100))
    body_list.append(Body(initial_positions[1],initial_velocities[1],1))'''

    initial_positions = np.random.multivariate_normal([0,0],[[200,0],[0,200]],n)
    initial_velocities = np.zeros_like(initial_positions)
    for i in range(n):
        body_list.append(Body(initial_positions[i],initial_velocities[i],25))

    positions,velocities,accelerations,mass_vector, mass_products = setup_verlet(body_list)
    for frame in range(num_frames):
        total_energy, total_momentum, positions, velocities, accelerations = step(positions,velocities,accelerations,dt,G,mass_vector,mass_products, softening)
        update_path(body_list,positions)
        update_energy_history(energy_history,total_energy, frame)
        update_momentum_history(momentum_history,total_momentum, frame)
    t1 = time.process_time()
    print("Simulation time: "+ str(t1-t0) + "s")    

    # generate the images
    t0 = time.process_time()
    filenames = make_images(body_list, num_frames, momentum_history)
    t1 = time.process_time()
    print("Drawing time: "+ str(t1-t0) + "s")

    # combine the images
    t0 = time.process_time()
    image_combiner(filenames)
    t1 = time.process_time()
    print("Combining time: "+ str(t1-t0) + "s")
    
def update_path(body_list, body_positions):
    for body_index in range(len(body_list)):
        body_list[body_index].path = np.vstack((body_list[body_index].path, body_positions[body_index]))

def update_energy_history(energy_history,total_energy, frame):
    energy_history[frame] = total_energy

def update_momentum_history(momentum_history, total_momentum, frame):
    momentum_history[frame] = total_momentum


simulate(100, 1, 400, 0.01, 0.2)