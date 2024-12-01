import numpy as np
from get_mass_products import *
from get_force_at_position import *
from collision_handler import *




# set up Verlet integration
def setup_verlet(body_list):
    mass_vector = np.array([body.mass for body in body_list])
    mass_products = get_mass_products(mass_vector)

    n = len(body_list)  

    positions = np.zeros((n,2))
    velocities = np.zeros((n,2))
    accelerations = np.zeros((n,2))
    for i in range(n):
        positions[i] = body_list[i].position
        velocities[i] = body_list[i].velocity
        accelerations[i] = body_list[i].acceleration
       
    return positions, velocities, accelerations, mass_vector, mass_products

def update_position(positions, velocities, accelerations, dt):
    positions += dt*velocities + 0.5*dt*dt*accelerations

def update_acceleration(positions, velocities, accelerations, mass_vector, G, collision_distance):
    net_forces, force_magnitudes = get_force(positions, G, mass_vector)
    #collision_handler(mass_vector, velocities, positions, net_forces, force_magnitudes, collision_distance)
    avg_accel = 0.5*(accelerations + net_forces/mass_vector[:,np.newaxis])
    accelerations = net_forces/mass_vector[:,np.newaxis]
    return avg_accel, accelerations

def update_velocity(velocities, avg_accel, dt):
    velocities += dt*avg_accel

def update_energy(positions, velocities, mass_vector, mass_products, G):
    v_squared = np.sum(velocities*velocities, axis=1)
    KE = 0.5*mass_vector*v_squared

    distances, distances_squared, distance_magnitudes = process_distances(positions)
    PE = -1*G*(np.sum(mass_products/distance_magnitudes,axis=1))

    energy_vector = KE + PE
    total_energy = np.sum(energy_vector)

    return total_energy

def step(positions,velocities,accelerations,dt,G,collision_distance,mass_vector,mass_products):
    update_position(positions,velocities,accelerations,dt)
    avg_accel, accelerations = update_acceleration(positions, velocities, accelerations, mass_vector, G, collision_distance)
    update_velocity(velocities, avg_accel, dt)

    total_energy = update_energy(positions, velocities, mass_vector, mass_products, G)

    body_momenta = mass_vector[:,np.newaxis]*velocities
    total_momentum_vector = np.sum(body_momenta, axis=0)
    total_momentum = np.sqrt(np.dot(total_momentum_vector,total_momentum_vector))
    return total_energy, total_momentum, positions, velocities, accelerations


