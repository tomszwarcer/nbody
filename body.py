import numpy as np

class Body:
    def __init__(self,position,velocity,mass,size):
        self.position = np.array(position,dtype='float64')
        self.velocity = np.array(velocity,dtype='float64')
        self.mass = mass
        self.acceleration = np.zeros(2)
        self.size = size
    