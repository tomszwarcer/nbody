import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
def make_images(body_list, num_frames, energy_history):
    filenames = []
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(16/2,9/2))
    plt.tight_layout()
    fig.patch.set_facecolor('k')
    ax.axis('off')
    limit = 10
    ax.set_xlim([-1*limit,limit])
    ax.set_ylim([(-9/16)*limit,(9/16)*limit])
    fig.canvas.draw_idle()

   
    lines = [ax.scatter([],[],s=[5], color='w', animated = True) for body in body_list]
    text = ax.text(limit - 2,(9/16)*limit-0.5,"test", color = "w",animated = True)

    for frame in range(num_frames):
        print("Frame " + str(frame+1) + "/" + str(num_frames))

        text.set_text("E = "+str(round(energy_history[frame])))
        ax.draw_artist(text)
        
        for (line,body) in zip(lines,body_list):
            line.set_offsets([body.path[frame][0],body.path[frame][1]])
            ax.draw_artist(line)

        filename = "./output/" + str(frame) + ".png"
        filenames.append(filename)
        fig.savefig(filename, dpi = 50)

    return filenames