from image_maker import *
from image_combiner import *
from body import Body
import numpy as np
import time
from verlet2d import *

def simulate(n, G, num_frames, dt):

    # simulate the bodies
    t0 = time.process_time()
    body_list = []
    initial_positions = np.array([[0,0],[1,0]])
    initial_velocities = np.array([[0,0],[0,10]])
    body_list.append(Body(initial_positions[0],initial_velocities[0],100))
    body_list.append(Body(initial_positions[1],initial_velocities[1],1))

    #positions = np.random.multivariate_normal([0,0],[[9,0],[0,3]],n)
    #velocities = 2*np.random.multivariate_normal([0,0],[[3,0],[0,3]],n)
    #for i in range(n):
    #    body_list.append(Body(initial_positions[i],initial_velocities[i],10))

    positions, mass_vector, mass_products = setup_verlet(body_list,dt,G)
    for frame in range(num_frames):
        positions = update_position(positions, mass_vector, mass_products, dt, G)
        update_path(body_list,positions[2])
    t1 = time.process_time()
    print("Simulation time: "+ str(t1-t0) + "s")    

    # generate the images
    t0 = time.process_time()
    filenames = make_images(body_list, num_frames)
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


simulate(2, 1, 200, 0.01)