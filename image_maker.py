import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
def make_images(body_list, energy_history, num_frames, plot_trails):
    filenames = []
    fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(16/2,9/2))
    plt.tight_layout()
    fig.patch.set_facecolor('k')
    ax.axis('off')
    limit = 10
    ax.set_xlim([-1*limit,limit])
    ax.set_ylim([(-9/16)*limit,(9/16)*limit])
    fig.canvas.draw_idle()
    #bg = fig.canvas.copy_from_bbox(ax.bbox)

   
    lines = [ax.scatter([],[],s=[5], color='w', animated = True) for body in body_list]

    for frame in range(num_frames):
        print("Frame " + str(frame+1) + "/" + str(num_frames))
        

        for (line,body) in zip(lines,body_list):
            line.set_offsets([body.path[frame][0],body.path[frame][1]])
            ax.draw_artist(line)
            fig.canvas.blit(ax.bbox)

        '''for body in body_list:
            ax.scatter(body.path[frame][0],body.path[frame][1],s=[10], color='w')
            if plot_trails:
                ax.scatter(np.transpose(body.path)[0],np.transpose(body.path)[1],s=0.3*np.ones(len(np.transpose(body.path)[1])),marker='.', color='w')
        ax.text(limit - 2,(9/16)*limit-0.5,"E = " + str(round(energy)),color = 'w')'''

        filename = "./output/" + str(frame) + ".png"
        filenames.append(filename)
        fig.savefig(filename, dpi = 50)

    return filenames