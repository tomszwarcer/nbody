import numpy as np

class Body:
    def __init__(self,position,velocity,mass):
        self.position = np.array(position,dtype='float64')
        self.velocity = np.array(velocity,dtype='float64')
        self.mass = mass
        self.acceleration = np.zeros(2)
        self.path = np.zeros(2)
        self.energy = 0.0