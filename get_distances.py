import numpy as np


def get_distances(positions):
    # position is an array of position vectors, one for each body. I.e. array of all positions of bodies.

    n = len(positions)

    # distance vectors between each body
    distances = np.zeros((n,n,2))
    for i in range(n-1):
        comparisons = n-i-1

        # create an array comprised of repeated copies of current body's position
        single_arr = positions[i]*np.ones(comparisons)[:,np.newaxis]

        # rest of the positions
        multiple_arr = [positions[j] for j in range(i+1,n)]

        # calculate distances
        distances[i][i+1:] = np.subtract(multiple_arr,single_arr) 

    # populate rest of array with the inverted distances
    distances = distances - np.transpose(distances, (1,0,2))
    return distances

def process_distances(positions):
    distances = get_distances(positions)
    distances_squared = np.sum(distances*distances,axis=2)
    distance_magnitudes = np.sqrt(distances_squared)

    # add the identity to prevent nan (this won't affect anything)
    distances_squared = distances_squared + np.identity(len(positions))
    distance_magnitudes = distance_magnitudes + np.identity(len(positions))

    return distances, distances_squared, distance_magnitudes