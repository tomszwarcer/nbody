import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors

class Body:
    def __init__(self,position,velocity,mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.acceleration = 0.0
        self.path = np.zeros((1,2))

def get_lists(body_list):
    #return a list of position vectors of bodies in a list

    position_list = np.zeros((len(body_list),2))
    mass_list = np.zeros((len(body_list)))
    for body_index in range(len(body_list)):
        position_list[body_index] = body_list[body_index].position
        mass_list[body_index] = body_list[body_index].mass
    return position_list, mass_list
    
def calculate_net_force(on_body, from_bodies):
    # on_body is a Body object
    # from_bodies is a list of Body objects

    # Gravitational constant
    G = 1

    # list of force vectors, one per body pair (i.e. n-1)
    forces = np.zeros((n-1,2))

    # list of distance vectors, one per body pair
    distances = np.zeros((n-1,2))

    distances_squared = np.zeros(n-1)
    force_magnitudes = np.zeros(n-1)


    # create an array of equal size to from_bodies of repeated copies of on_body's position
    on_body_psn_arr = on_body.position*np.ones(len(from_bodies))[:,np.newaxis]

    [position_list, mass_list] = get_lists(from_bodies)

    distances = np.subtract(position_list,on_body_psn_arr)

    # compute element-wise dot products
    distances_squared = np.sum(distances*distances,axis = 1)
    distance_magnitude = np.sqrt(distances_squared)

    force_magnitudes = G*on_body.mass*(mass_list/distances_squared)

    # newaxis is needed to do the element wise operations properly
    forces = distances*force_magnitudes[:,np.newaxis]/distance_magnitude[:,np.newaxis]

    net_force = np.sum(forces, axis=0)

    return net_force

def update_path(body_list):
    for body in body_list:
        body.path = np.vstack((body.path,body.position))

def update_accel(body_list):
    for body in body_list:
        body_list_temp = [i for i in body_list if i != body]
        net_force = calculate_net_force(body,body_list_temp)
        body.acceleration = net_force/body.mass

def update_velocity(body_list, dt):
    for body in body_list:
        body.velocity += body.acceleration*dt

def update_position(body_list, dt):
    for body in body_list:
        body.position += body.velocity*dt

def new_frame(body_list):
    dt = 0.01
    update_path(body_list)
    update_accel(body_list)
    update_velocity(body_list, dt)
    update_position(body_list, dt)

def update_frame(frame):
    colour_index = 0
    new_frame(body_list)
    ax.clear()
    for body in body_list:
        ax.set_xlim([-5,5])
        ax.set_ylim([-5,5])
        ax.scatter(body.position[0],body.position[1],s=[50], c=colours[colour_index % 8])
        ax.scatter(np.transpose(body.path)[0],np.transpose(body.path)[1],s=0.5*np.ones(len(np.transpose(body.path)[1])),marker='.', c=colours[colour_index % 8])
        colour_index += 1
    
body_list = [Body([0,0],[0,-1],1),Body([1,0],[0,1],1),Body([-1,2],[1,0],1)]
n = len(body_list)
fig, ax = plt.subplots()
colours = np.array(list(mcolors.BASE_COLORS.values()))

ani = FuncAnimation(fig, update_frame, frames=200, interval=1)

plt.show()


