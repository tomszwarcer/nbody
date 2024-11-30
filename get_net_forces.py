import numpy as np
from get_distances import get_distances
from get_mass_products import get_mass_products
from body import Body

def get_net_forces(body_list):

    n = len(body_list)
    G = 1

    forces = np.zeros((n,n,2))
    force_magnitudes = np.zeros((n,n))

    distances = get_distances(body_list)
    distances_squared = np.sum(distances*distances,axis=2)
    distance_magnitudes = np.sqrt(distances_squared)

    # add the identity to prevent nan (this won't affect anything)
    distances_squared = distances_squared + np.identity(n)
    distance_magnitudes = distance_magnitudes + np.identity(n)
    
    # create matrix of mass product combinations
    force_magnitudes = G*get_mass_products(body_list)/distances_squared
    forces = force_magnitudes/distance_magnitudes
    forces = forces[:,:,np.newaxis]*distances
    
    net_force = np.zeros((n,2))
    for i in range(n):
        net_force[i] = np.sum(np.array([j for j in forces[i]]),axis=0)

    return net_force
