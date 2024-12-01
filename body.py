import numpy as np

class Body:
    def __init__(self,position,velocity,mass):
        self.position = np.array(position,dtype='float64')
        self.velocity = np.array(velocity,dtype='float64')
        self.mass = mass
        self.acceleration = np.zeros(2)
        self.path = np.array(position,dtype='float64')

class Path:
    def __init__(self, num_frames, n):
        self.x = np.zeros((num_frames,n,2))
        self.y = np.zeros((num_frames,n,2))
        

    