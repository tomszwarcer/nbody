import numpy as np
import time
from body import Body
from get_force_energy import *

def update_path(body_list):
    # updates path for orbit 'trail' in animation

    for body in body_list:
        body.path = np.vstack((body.path,body.position))

def update_accel_energy(body_list):
    # updates acceleration using net force
    net_forces, total_energy = get_force_energy(body_list)
    for body_index in range(len(body_list)):
        body_list[body_index].acceleration = net_forces[body_index]/body_list[body_index].mass
        body_list[body_index].energy = total_energy[body_index]


def update_velocity(body_list, dt):
    # updates velocity using acceleration

    for body in body_list:
        body.velocity += body.acceleration*dt

def update_position(body_list, dt):
    # updates position using velocity

    for body in body_list:
        body.position += body.velocity*dt

def update_all(body_list):
    t0 = time.process_time()

    # timestep
    dt = 0.001

    update_path(body_list)
    update_accel_energy(body_list)
    update_velocity(body_list, dt)
    update_position(body_list, dt)

    t1 = time.process_time()
    return t1-t0

    








