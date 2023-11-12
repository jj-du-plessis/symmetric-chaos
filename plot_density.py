"""Plot Histogram

This script uses the 2D histogram from compute_histogram.py and saves a density
plot. Colors are used to distinguish densities. Color palettes are imported
from modules.palettes and can be customised.

Variables:
    symmetry:       symmetry group of the attractor which arises from the
                    corresponding parameter list
    empty_color:    color used to represent pixels without any points
    palette:        parameter list whose name is the value of the symmetry
                    variable
    z:              random initial condition
    x,y:            1D arrays of the real and imaginary parts of the complex
                    iterates, respectively
"""

import numpy as np
import matplotlib.pyplot as plt
from modules.colormap import colormap
import modules.palettes as palettes

symmetry = "D19"
empty_color = [1.,1.,1.]
# color palette loaded from modules.palette, but feel free to create your own
palette = getattr(palettes,symmetry)
listed_ranks, colors_hex = zip(*sorted(palette.items()))
# load histogram, correct the (x,y) bin coordinates
freq_array = np.load("histogrammed_data/"+symmetry+".npy").T[::-1]

rgb_array = colormap(freq_array,colors_hex,listed_ranks,empty_color)
plt.imsave("figures/"+symmetry+"_density.png",rgb_array)