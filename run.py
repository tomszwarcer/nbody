from accretion_disk import accretion_disk
from two_body import two_body
from solar_system import solar_system

# n bodies
n = 6

# gravitational constant
G = 1

# number of frames to be simulated
num_frames = 100

# time step between frames
dt = 0.01

# softening parameter
softening = 0.2

two_body(2,G,num_frames,dt,softening)
#accretion_disk(n,G,num_frames,dt,softening)
#solar_system(n,G,num_frames,dt,softening)
