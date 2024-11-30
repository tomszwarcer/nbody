from get_distances import *
from get_mass_products import *

def get_energy(body_list, G):
    v_squared = np.array([np.sqrt(np.dot(j.velocity,j.velocity)) for j in body_list])
    mass_list = np.array([j.mass for j in body_list])

    mass_products = get_mass_products(body_list)

    # room for optimisation here as we calculate all this in get force step
    distances, distances_squared, distance_magnitudes = process_distances(body_list)

    KE = 0.5*v_squared*mass_list
    PE = -1*G*(np.sum(mass_products/distance_magnitudes,axis=1))
    total_energy_per_body = KE+PE

    total_energy = np.sum(total_energy_per_body)

    return total_energy