from euler2d import *
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import imageio.v2 as iio
import time
matplotlib.use('Agg')


def plotter(body_list, plot_trails):
    filenames = []
    calc_time = 0
    max_frames = 250

    # calculate total mass and energy
    total_mass = 0
    
    for body in body_list:
        total_mass += body.mass
        
    for frame in range(max_frames):
        print("Frame " + str(frame+1) + "/" + str(max_frames))
        # actual calculation is done here
        calc_time += update_all(body_list)

        fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(16/2,9/2))
        plt.tight_layout()
        fig.patch.set_facecolor('k')
        ax.axis('off')
        limit = 10
        ax.set_xlim([-1*limit,limit])
        ax.set_ylim([(-9/16)*limit,(9/16)*limit])

        total_energy = 0

        for body in body_list:
            total_energy += body.energy
            ax.scatter(body.position[0],body.position[1],s=[(20+(100/len(body_list)))*np.sqrt(body.mass/total_mass)], color='w', animated=True)
            if plot_trails:
                ax.scatter(np.transpose(body.path)[0],np.transpose(body.path)[1],s=0.3*np.ones(len(np.transpose(body.path)[1])),marker='.', color='w')
        
        ax.text(1.2,0.85,"E = "+str(round(total_energy)),color='w')
        name = "./output/" + str(frame) + ".png"
        filenames.append(name)
        fig.savefig(name, dpi = 120)
        plt.close()
    print("Calculation time: " + str(calc_time) + "s")
    return filenames

def combiner(filenames):
    w = iio.get_writer("output/movies/plot.gif", format="gif", mode='I', fps=30)
    for frame in filenames:
        w.append_data(iio.imread(frame))
    w.close()

def make_gif(body_list, plot_trails):
    t0 = time.process_time()
    filenames = plotter(body_list, plot_trails)
    t1 = time.process_time()
    print("Plotting time: " + str(t1-t0) + "s")
    t0 = time.process_time()
    combiner(filenames)
    t1 = time.process_time()
    print("Combining time: " + str(t1-t0) + "s")
    
   

#body_list = [Body([0,0],[0,0],300),Body([3,-0.9],[-34,0],11),Body([1,0],[0,-14.6],0.5)]
#make_gif(body_list)
