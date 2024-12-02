import numpy as np
from get_distances import *
from get_mass_products import *

# The force between the ith and the jth body is stored as the i,j element of
# an nxn matrix
def get_force(position, G, mass_vector, softening):

    mass_products = get_mass_products(mass_vector)

    n = len(position)

    forces = np.zeros((n,n,2))
    force_magnitudes = np.zeros((n,n))

    distances, distances_squared, distance_magnitudes = process_distances(position)

    force_magnitudes = G*mass_products/(distances_squared + (softening*np.ones((len(position),len(position)))))
    forces = force_magnitudes/distance_magnitudes
    forces = forces[:,:,np.newaxis]*distances
    
    net_force = np.zeros((n,2))
    for i in range(n):
        net_force[i] = np.sum(np.array([j for j in forces[i]]),axis=0)

    return net_force, force_magnitudes


