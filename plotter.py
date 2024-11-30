import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('Agg')

def plotter(body_list, energy, plot_trails, frame):
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(16/2,9/2))
    plt.tight_layout()
    fig.patch.set_facecolor('k')
    ax.axis('off')
    limit = 10
    ax.set_xlim([-1*limit,limit])
    ax.set_ylim([(-9/16)*limit,(9/16)*limit])

    for body in body_list:
        ax.scatter(body.path[frame][0],body.path[frame][1],s=[30], color='w')
        if plot_trails:
            ax.scatter(np.transpose(body.path)[0],np.transpose(body.path)[1],s=0.3*np.ones(len(np.transpose(body.path)[1])),marker='.', color='w')
    ax.text(limit - 2,(9/16)*limit-0.5,"E = " + str(round(energy)),color = 'w')

    filename = "./output/" + str(frame) + ".png"
    fig.savefig(filename, dpi = 120)
    plt.close()
    return filename