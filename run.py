from accretion_disk import accretion_disk
from two_body import two_body
from solar_system import solar_system

# n bodies
n = 7

# gravitational constant
G = 1

# number of frames to be simulated
num_frames = 400

# time step between frames
dt = 0.01

# softening parameter
softening = 0.0

# length of trail in frames, set 0 for no trail. Recommended to disble for many bodies.
trail_length = 50

#two_body(2,G,num_frames,dt,softening,trail_length)
#accretion_disk(n,G,num_frames,dt,softening,trail,0)
solar_system(n,G,num_frames,dt,softening,trail_length)
