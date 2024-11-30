import numpy as np
from body import Body

def get_distances(body_list):
    n = len(body_list)
    distances = np.zeros((n,n,2))
    for i in range(n-1):
        comparisons = n-i-1

        # create an array comprised of repeated copies of current body's position
        single_arr = body_list[i].position*np.ones(comparisons)[:,np.newaxis]

        multiple_arr = [body_list[j].position for j in range(i+1,n)]

        # calculate distances
        distances[i][i+1:] = np.subtract(multiple_arr,single_arr) 

    # populate rest of array with the inverted distances
    distances = distances - np.transpose(distances, (1,0,2))
    return distances

