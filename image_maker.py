import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
def make_images(path, num_frames, energy_history, size_list, trail_length):
    n =len(energy_history)
    filenames = []
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(8,8))
    plt.tight_layout()
    fig.patch.set_facecolor('k')
    ax.axis('off')
    limit = 1.75*max(path.x[0][:])
    ax.set_xlim([-1*limit,limit])
    ax.set_ylim([-1*limit,limit])
   
    text = ax.text(0.7*limit,0.8*limit,"test", color = "w",animated = True)

    for frame in range(num_frames):
        fig.canvas.draw_idle()
        print("Drawing frame " + str(frame+1) + "/" + str(num_frames))
        plot_bodies = ax.scatter(path.x[frame][:], path.y[frame][:], s=size_list, color='w')
        
        if trail_length > 0:
            trail_first_frame = int(np.heaviside(frame-trail_length,1))*(frame-trail_length)            
            plot_trails = ax.scatter(path.x[trail_first_frame:frame].reshape(-1),path.y[trail_first_frame:frame].reshape(-1), marker=".", color = "w", s=0.5)

        text.set_text("p = "+str(round(energy_history[frame])))
        ax.draw_artist(text)

        filename = "./output/" + str(frame) + ".png"
        filenames.append(filename)
        fig.savefig(filename, dpi = 150)
        plot_bodies.remove()
        plot_trails.remove()

    return filenames