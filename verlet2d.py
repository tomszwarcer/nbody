import numpy as np
from get_mass_products import *
from get_force_at_position import *


def acceleration(position, mass_vector, mass_products, G):
    net_forces, force_magnitudes = get_force(position, G, mass_products)
    return net_forces/mass_vector[:,np.newaxis]
    
def reshuffle(current_vectors, new_vector):
    # [n-3,n-2,n-1] + n => [n-2,n-1,n] 
    current_vectors[0:2] = current_vectors[1:3]
    current_vectors[2] = new_vector

# store xn-2,xn-1,xn and update to xn+1, etc: a[0:2] = a[1:3]



# set up Verlet integration
def setup_verlet(body_list, dt, G):
    mass_vector = np.array([body.mass for body in body_list])
    mass_products = get_mass_products(mass_vector)

    n = len(body_list)  
    positions = np.zeros((3,n,2))
    positions[1] = [body.position for body in body_list]
    positions[2] = positions[1] + dt*np.array([body.velocity for body in body_list]) + 0.5*dt*dt*acceleration(positions[1], mass_vector, mass_products, G)
    return positions, mass_vector, mass_products

def update_position(positions, mass_vector, mass_products, dt, G):
    new_position = 2*positions[2]-positions[1]+dt*dt*acceleration(positions[2], mass_vector, mass_products, G)
    reshuffle(positions, new_position)
    return positions




