from euler2d import *
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import imageio
import time
matplotlib.use('Agg')


def plotter(body_list):
    calc_time = 0
    filenames = []
    colours = np.array(list(mcolors.BASE_COLORS.values()))
    max_frames = 500
    for frame in range(max_frames):
            plt.axis("off")
            plt.xlim([-2,2])
            plt.ylim([-2,2])
            colour_index = 0
            for body in body_list:
                plt.scatter(body.position[0],body.position[1],s=[50], c=colours[colour_index % 8])
                plt.scatter(np.transpose(body.path)[0],np.transpose(body.path)[1],s=0.3*np.ones(len(np.transpose(body.path)[1])),marker='.', c=colours[colour_index % 8])
                colour_index += 1
            name = "./output/" + str(frame) + ".png"
            filenames.append(name)
            plt.savefig(name)
            plt.close()
            calc_time += update_all(body_list)
    print("Calculation time: " + str(calc_time) + "s\n")
    return filenames

def combiner(filenames):
    with imageio.get_writer('./output/movies/plot.gif', mode='I', loop = 100) as writer:
        for file_num in range(len(filenames)):
            if file_num % 1 == 0:
                image = imageio.imread(filenames[file_num])
                writer.append_data(image)

def make_gif(body_list):
    t0 = time.process_time()
    filenames = plotter(body_list)
    combiner(filenames)
    t1 = time.process_time()
    print("Total time: " + str(t1-t0) + "s\n")

body_list = [Body([0,0],[0,0],300),Body([5,-1],[-24,0],1),Body([-1,0],[0,13],1)]
make_gif(body_list)
