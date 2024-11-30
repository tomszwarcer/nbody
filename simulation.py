from image_maker import *
from image_combiner import *
from body import Body
import numpy as np
import time
from euler2d import *

def simulate(n, plot_trails, num_frames):
    # simulate the bodies
    t0 = time.process_time()
    body_list = []
    positions = np.random.multivariate_normal([0,0],[[1,0],[0,1]],n)
    velocities = 5*np.random.multivariate_normal([0,0],[[1,0],[0,1]],n)
    for i in range(n):
        body_list.append(Body(positions[i],velocities[i],1))
    for frame in range(num_frames):
        update_all(body_list)
    t1 = time.process_time()
    print("Simulation time: "+ str(t1-t0) + "s")

    # generate the images
    t0 = time.process_time()
    filenames = make_images(body_list, num_frames, plot_trails)
    t1 = time.process_time()
    print("Drawing time: "+ str(t1-t0) + "s")

    # combine the images
    t0 = time.process_time()
    image_combiner(filenames)
    t1 = time.process_time()
    print("Combining time: "+ str(t1-t0) + "s")
    
simulate(20, False, 200)