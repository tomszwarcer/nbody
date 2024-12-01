import numpy as np
from get_distances import *
from get_mass_products import *

def get_force(position, G, mass_products):

    n = len(position)

    forces = np.zeros((n,n,2))
    force_magnitudes = np.zeros((n,n))

    distances, distances_squared, distance_magnitudes = process_distances(position)

    force_magnitudes = G*mass_products/distances_squared
    forces = force_magnitudes/distance_magnitudes
    forces = forces[:,:,np.newaxis]*distances
    
    net_force = np.zeros((n,2))
    for i in range(n):
        net_force[i] = np.sum(np.array([j for j in forces[i]]),axis=0)

    return net_force, force_magnitudes


