import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
def make_images(path, num_frames, energy_history):
    filenames = []
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(16/2,9/2))
    plt.tight_layout()
    fig.patch.set_facecolor('k')
    ax.axis('off')
    limit = 40
    ax.set_xlim([-1*limit,limit])
    ax.set_ylim([(-9/16)*limit,(9/16)*limit])

   
    #lines = [ax.scatter([],[],s=[1], color='w', animated = True) for body in body_list]
    text = ax.text(limit - 2,(9/16)*limit-0.5,"test", color = "w",animated = True)

    for frame in range(num_frames):
        fig.canvas.draw_idle()
        print("Frame " + str(frame+1) + "/" + str(num_frames))
        s = ax.scatter(path.x[frame][:,0], path.y[frame][:,1], s=[1], color='w')

        text.set_text("p = "+str(round(energy_history[frame])))
        ax.draw_artist(text)

        filename = "./output/" + str(frame) + ".png"
        filenames.append(filename)
        fig.savefig(filename, dpi = 150)
        s.remove()

    return filenames