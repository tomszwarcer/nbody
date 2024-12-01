import numpy as np
from get_force import *
from get_energy import *
from get_distances import *
from collision_handler import *

def update_path(body_list):
    # updates path for orbit 'trail' in animation

    for body in body_list:
        body.path = np.vstack((body.path,body.position))

def update_accel(body_list, G,collision_distance):
    net_forces, force_magnitudes = get_force(body_list, G)
    collision_handler(body_list, collision_distance, net_forces, force_magnitudes)
    for body_index in range(len(body_list)):
        body_list[body_index].acceleration = net_forces[body_index]/body_list[body_index].mass

def update_velocity(body_list, dt):
    # updates velocity using acceleration

    for body in body_list:
        body.velocity += body.acceleration*dt


def update_position(body_list, dt, collision_distance):
    # updates position using velocity

    for body in body_list:
        body.position += body.velocity*dt



def euler(body_list, G, collision_distance):
    # timestep
    dt = 0.001

    update_path(body_list)
    update_accel(body_list,G, collision_distance)
    total_energy = get_energy(body_list,G)
    update_velocity(body_list, dt)
    update_position(body_list, dt, collision_distance)

    return total_energy
    








