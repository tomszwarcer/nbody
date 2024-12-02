import imageio.v2 as iio
import os

def image_combiner(filenames):
    w = iio.get_writer("output/movies/plot.gif", format="gif", mode='I', fps=30, loop=100)
    for frame in filenames:
        w.append_data(iio.imread(frame))
    w.close()
    print("Cleaning up...")
    for file in filenames:
        os.remove(file)