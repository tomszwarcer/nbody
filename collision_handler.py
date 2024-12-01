from get_distances import *

def collision_handler(mass_vector, velocities, positions, net_force, force_magnitudes, collision_distance):
    distances, distances_squared, distance_magnitudes = process_distances(positions)
    n = len(mass_vector)
    for i in range(n-1):
        for j in range(i+1,n):
            if distance_magnitudes[i][j] < collision_distance:

                #stop the effect of gravity at this distance
                force_magnitudes[i][j] = 0
                net_force[i] = np.array([0.,0.])
                net_force[j] = np.array([0.,0.])


                # update positions to move them outside the collision region. Broken, but maybe necessary for small dt.
                #position_correction(body_list,i,j,distances[i][j], distance_magnitudes[i][j],collision_distance)

                # room for optimisation as can calculate separation vector and denominator without having to get distances again
                #distances, distances_squared, distance_magnitudes = process_distances(body_list)

                # formula taken from wikipedia (https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional)
                velocity_list = np.array([velocities[i],velocities[j]])
                m1 = mass_vector[i]
                m2 = mass_vector[j]
                v1 = velocities[i]
                v2 = velocities[j]
                separation_vector = distances[i][j]
                denominator = distances_squared[i][j]
                dv = np.array([(2*m2/(m1+m2))*np.dot(v1-v2,-1*separation_vector)*-1*separation_vector/denominator,(2*m1/(m1+m2))*np.dot(v2-v1,separation_vector)*separation_vector/denominator])

                velocity_list = velocity_list - dv
                velocities[i] = velocity_list[0]
                velocities[j] = velocity_list[1]

def position_correction(body_list,i,j, separation_vector, magnitude, collision_distance):
    # broken, needs updating

    # sep. vect. is x2-x1

    tolerance = collision_distance/20

    # move 1st in direction of x1-x2
    k1 = (-1*separation_vector/magnitude)*((collision_distance/2)-magnitude+tolerance)
    body_list[i].position += k1

    # move 2nd in direction of x2-x1
    k2 = (separation_vector/magnitude)*((collision_distance/2)-magnitude+tolerance)
    body_list[j].position += k2