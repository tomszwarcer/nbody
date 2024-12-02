from accretion_disk import accretion_disk
from two_body import two_body

# n bodies
n = 20

# gravitational constant
G = 1

# number of frames to be simulated
num_frames = 50

# time step between frames
dt = 0.01

# softening parameter
softening = 0.2

#two_body(n,G,num_frames,dt,softening)
accretion_disk(n,G,num_frames,dt,softening)
