import numpy as np

class Body:
    def __init__(self,position,velocity,mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.acceleration = 0.0
        self.path = np.zeros((1,2))
        self.energy = 0.0