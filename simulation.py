from image_maker import *
from image_combiner import *
from body import Body
from path import Path
import numpy as np
import time
from vverlet2d import *

def simulate(n, G, num_frames, dt, softening, body_list, trail_length):

    # simulate the bodies
    t0 = time.process_time()

    # E/p tracking
    energy_history = np.zeros(num_frames)
    momentum_history = np.zeros(num_frames)

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
    filenames = make_images(path, num_frames, momentum_history, size_list, trail_length)
    t1 = time.process_time()
    print("Drawing time: "+ str(t1-t0) + "s")

    # combine the images
    t0 = time.process_time()
    image_combiner(filenames)
    t1 = time.process_time()
    print("Combining time: "+ str(t1-t0) + "s")
    

def update_path(path, body_positions, frame):
    path.x[frame] = body_positions[:,0]
    path.y[frame] = body_positions[:,1]


def update_energy_history(energy_history,total_energy, frame):
    energy_history[frame] = total_energy

def update_momentum_history(momentum_history, total_momentum, frame):
    momentum_history[frame] = total_momentum

def create_size_list(body_list):
    size_list = np.array([body.size for body in body_list])
    return size_list
