import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
def make_images(path, num_frames, energy_history, size_list):
    filenames = []
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(8,8))
    plt.tight_layout()
    fig.patch.set_facecolor('k')
    ax.axis('off')
    limit = max(path.x[0][:,0])+5
    ax.set_xlim([-1*limit,limit])
    ax.set_ylim([-1*limit,limit])
   
    text = ax.text(limit - 10,limit-5,"test", color = "w",animated = True)

    for frame in range(num_frames):
        fig.canvas.draw_idle()
        print("Drawing frame " + str(frame+1) + "/" + str(num_frames))
        s = ax.scatter(path.x[frame][:,0], path.y[frame][:,1], s=size_list, color='w')

        text.set_text("p = "+str(round(energy_history[frame])))
        ax.draw_artist(text)

        filename = "./output/" + str(frame) + ".png"
        filenames.append(filename)
        fig.savefig(filename, dpi = 150)
        s.remove()

    return filenames