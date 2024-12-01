import numpy as np
from body import Body

def get_mass_products(mass_vector):
    n = len(mass_vector)
    products = np.zeros((n,n))
    for i in range(n-1):
        for j in range(i+1,n):
            products[i][j] = mass_vector[i]*mass_vector[j]

    # populate rest of array
    products = products + np.transpose(products)
    return products

