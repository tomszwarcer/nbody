import numpy as np
from body import Body

def get_mass_products(body_list):
    n = len(body_list)
    products = np.zeros((n,n))
    for i in range(n-1):
        for j in range(i+1,n):
            products[i][j] = body_list[i].mass*body_list[j].mass

    # populate rest of array with the inverted distances
    products = products + np.transpose(products)
    return products

