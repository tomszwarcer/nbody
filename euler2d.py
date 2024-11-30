import numpy as np
from get_force import *
from get_energy import *
from get_distances import *

def update_path(body_list):
    # updates path for orbit 'trail' in animation

    for body in body_list:
        body.path = np.vstack((body.path,body.position))

def update_accel(body_list, G):
    net_forces = get_force(body_list, G)
    for body_index in range(len(body_list)):
        body_list[body_index].acceleration = net_forces[body_index]/body_list[body_index].mass

def update_velocity(body_list, dt):
    # updates velocity using acceleration

    for body in body_list:
        body.velocity += body.acceleration*dt

def update_position(body_list, dt):
    # updates position using velocity

    for body in body_list:
        body.position += body.velocity*dt



def euler(body_list, G):
    # timestep
    dt = 0.001

    update_path(body_list)
    update_accel(body_list,G)
    total_energy = get_energy(body_list,G)
    update_velocity(body_list, dt)
    update_position(body_list, dt)

    return total_energy
    








