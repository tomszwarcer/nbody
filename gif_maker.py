from euler2d import *
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import imageio.v2 as iio
import time
matplotlib.use('Agg')


def plotter(body_list):
    filenames = []
    calc_time = 0
    colours = np.array(list(mcolors.BASE_COLORS.values()))
    max_frames = 250
    for frame in range(max_frames):
        plt.axis("off")
        plt.xlim([-2,2])
        plt.ylim([-2,2])
        colour_index = 0
        for body in body_list:
            plt.scatter(body.position[0],body.position[1],s=[50], color=colours[colour_index % 8])
            plt.scatter(np.transpose(body.path)[0],np.transpose(body.path)[1],s=0.3*np.ones(len(np.transpose(body.path)[1])),marker='.', color=colours[colour_index % 8])
            colour_index += 1
        name = "./output/" + str(frame) + ".png"
        filenames.append(name)
        plt.savefig(name)
        plt.close()
        calc_time += update_all(body_list)
    print("Calculation time: " + str(calc_time) + "s\n")
    return filenames

def combiner(filenames):
    w = iio.get_writer("output/movies/plot.gif", format="gif", mode='I', fps=30)
    for frame in filenames:
        w.append_data(iio.imread(frame))
    w.close()

def make_gif(body_list):
    t0 = time.process_time()
    filenames = plotter(body_list)
    combiner(filenames)
    t1 = time.process_time()
    print("Total time: " + str(t1-t0) + "s\n")

body_list = [Body([0,0],[0,0],300),Body([3,-0.9],[-34,0],11),Body([1,0],[0,-14.6],0.5)]
make_gif(body_list)
