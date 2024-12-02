import numpy as np
class Path:
    def __init__(self, num_frames, n):
        self.x = np.zeros((num_frames,n,2))
        self.y = np.zeros((num_frames,n,2))