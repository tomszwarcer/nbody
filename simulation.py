from image_maker import *
from image_combiner import *
from body import Body
import numpy as np
import time
from euler2d import *

def simulate(n, G, plot_trails, num_frames):
    energy_history = np.zeros(num_frames)

    # simulate the bodies
    t0 = time.process_time()
    body_list = []
    positions = np.random.multivariate_normal([0,0],[[1,0],[0,1]],n)
    velocities = 0*np.random.multivariate_normal([0,0],[[1,0],[0,1]],n)
    for i in range(n):
        body_list.append(Body(positions[i],velocities[i],1))
    for frame in range(num_frames):
        energy_history[frame] = euler(body_list, G)
    t1 = time.process_time()
    print("Simulation time: "+ str(t1-t0) + "s")

    # generate the images
    t0 = time.process_time()
    filenames = make_images(body_list, energy_history, num_frames, plot_trails)
    t1 = time.process_time()
    print("Drawing time: "+ str(t1-t0) + "s")

    # combine the images
    t0 = time.process_time()
    image_combiner(filenames)
    t1 = time.process_time()
    print("Combining time: "+ str(t1-t0) + "s")
    
simulate(20, 10, False, 200)