import numpy as np

class Body:
    def __init__(self,position,velocity,mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.acceleration = 0.0
        self.path = np.zeros((1,2))

def get_lists(body_list):
    # return a list of position vectors and masses of bodies

    position_list = np.zeros((len(body_list),2))
    mass_list = np.zeros((len(body_list)))
    for body_index in range(len(body_list)):
        position_list[body_index] = body_list[body_index].position
        mass_list[body_index] = body_list[body_index].mass
    return position_list, mass_list
    
def calculate_net_force(on_body, from_bodies):

    # number of bodies 
    n = len(from_bodies) + 1

    # Gravitational constant
    G = 1

    # list of force vectors, one per body pair (i.e. n-1)
    forces = np.zeros((n-1,2))
    force_magnitudes = np.zeros(n-1)

    distances = np.zeros((n-1,2))
    distances_squared = np.zeros(n-1)

    # create an array of equal size to from_bodies comprised of repeated copies of on_body's position
    on_body_psn_arr = on_body.position*np.ones(len(from_bodies))[:,np.newaxis]

    [position_list, mass_list] = get_lists(from_bodies)

    # list of position vectors between the body in question and other bodies
    distances = np.subtract(position_list,on_body_psn_arr)

    # compute element-wise dot products
    distances_squared = np.sum(distances*distances,axis = 1)
    distance_magnitude = np.sqrt(distances_squared)

    force_magnitudes = G*on_body.mass*(mass_list/distances_squared)

    # newaxis is needed to do the element wise operations properly
    forces = distances*force_magnitudes[:,np.newaxis]/distance_magnitude[:,np.newaxis]

    # add vectors to get net force
    net_force = np.sum(forces, axis=0)

    return net_force

def update_path(body_list):
    # updates path for orbit 'trail' in animation

    for body in body_list:
        body.path = np.vstack((body.path,body.position))

def update_accel(body_list):
    # updates acceleration using net force

    for body in body_list:
        body_list_temp = [i for i in body_list if i != body]
        net_force = calculate_net_force(body,body_list_temp)
        body.acceleration = net_force/body.mass

def update_velocity(body_list, dt):
    # updates velocity using acceleration

    for body in body_list:
        body.velocity += body.acceleration*dt

def update_position(body_list, dt):
    # updates position using velocity

    for body in body_list:
        body.position += body.velocity*dt

def update_all(body_list):

    # timestep
    dt = 0.005

    update_path(body_list)
    update_accel(body_list)
    update_velocity(body_list, dt)
    update_position(body_list, dt)

    








