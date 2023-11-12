"""Compute and Save 2D Histogram

This script iterates a complex map (defined in modules.map using parameters
from modules.parameters) a number of times and, after discarding the transient,
returns a 1D arrary for the real parts of the complex iterates and also for the
imaginary parts. A 2D histogram is computed from the iterates, and this array
is saved to a file in the histogrammed_data directory.

Variables:
    symmetry:   symmetry group of the attractor which arises from the
                corresponding parameter list defined in the parameters module
    iterations: number of iterated points to save
    transient:  number of transient points to ignore
    bins:       number of bins in each dimension of the 2D histogram, so the
                histogram array will have shape (bins,bins)
    parameters: parameter list imported from the parameters module
    z:          random initial condition
    x,y:        1D arrays of the real and imaginary parts of the complex
                iterates, respectively
    histogram:  2D array with shape (bins,bins) where each entry is the number
                of iterated points (ignoring the transient) which fall in that
                particular 2D bin
"""

import numpy as np
from modules.map import iterate_map
import modules.parameters as params

symmetry = "D3"
iterations = 10000000    # if you make this too large, you'll run out of RAM
transient  = 1000
bins = 1000
parameters = getattr(params,symmetry)
z = (2*np.random.rand()-1 + (2*np.random.rand()-1)*1j)/3

x,y = iterate_map(z,transient,iterations,*parameters)
histogram = np.histogram2d(x,y,bins=bins)[0]
np.save("histogrammed_data/"+symmetry+".npy",histogram)