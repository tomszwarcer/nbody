import numpy as np

# The mass product between the ith and the jth body is stored as the i,j element of
# an nxn matrix
def get_mass_products(mass_vector):
    n = len(mass_vector)
    products = np.zeros((n,n))
    
    for i in range(n-1):
        for j in range(i+1,n):
            products[i][j] = mass_vector[i]*mass_vector[j]

    # populate rest of array
    products = products + np.transpose(products)
    return products

