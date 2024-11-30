from plotter import *

def make_images(body_list, energy_history, num_frames, plot_trails):
    filenames = []

    for frame in range(num_frames):
        print("Frame " + str(frame+1) + "/" + str(num_frames))
        filenames.append(plotter(body_list, energy_history[frame], plot_trails, frame))
    return filenames