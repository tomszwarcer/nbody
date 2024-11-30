import numpy as np
from get_distances import get_distances
from get_mass_products import get_mass_products
from body import Body

def get_force_energy(body_list):

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
    mass_products = get_mass_products(body_list)

    force_magnitudes = G*mass_products/distances_squared
    forces = force_magnitudes/distance_magnitudes
    forces = forces[:,:,np.newaxis]*distances
    
    net_force = np.zeros((n,2))
    for i in range(n):
        net_force[i] = np.sum(np.array([j for j in forces[i]]),axis=0)

    # energy calculation (room for optimisation)

    

    v_squared = np.array([np.sqrt(np.dot(j.velocity,j.velocity)) for j in body_list])
    mass_list = np.array([j.mass for j in body_list])

    KE = 0.5*v_squared*mass_list
    PE = -1*G*(np.sum(mass_products/distance_magnitudes,axis=1))
    total_energy = KE+PE
    
    

    return net_force, total_energy
