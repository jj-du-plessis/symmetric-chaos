"""Create a Colormap

Creating sensible colormaps for these attractors is a tricky business. The
approach here defines a color palette where each color corresponds to a
particular percentile rank (from 0 to 100) of the histogram frequencies. This
has the benefit of making it easy to choose how much of each color appears in
the figure.
"""

import numpy as np
from numba import jit

def colormap(freq_array,colors_hex,listed_ranks,empty_color):
    freq_sorted = np.sort(freq_array.flatten())
    freq_unique = np.unique(freq_sorted)
    rank_unique = np.zeros(len(freq_sorted))
    rank_array = np.zeros(freq_array.shape)
    rgb_array = np.zeros((freq_array.shape[0],freq_array.shape[1],3))
    listed_ranks = np.array(listed_ranks)/100

    # convert HEX to RGB
    colors_rgb = []
    for c in colors_hex:
        colors_rgb.append(list(int(c[i:i+2], 16)/255 for i in (0, 2, 4)))
    colors_rgb = np.array(colors_rgb)

    # determine the unique percentile rankings
    for i in range(len(freq_unique)):
        lower = np.searchsorted(freq_sorted,freq_unique[i],side="left")
        upper = np.searchsorted(freq_sorted,freq_unique[i],side="right")
        rank = 0
        for j in range(lower,upper):
            rank += j/(len(freq_sorted)-1)
        rank_unique[i] = rank/(upper-lower)

    # populate array of RGB values
    for i in range(freq_array.shape[0]):
        for j in range(freq_array.shape[1]):
            if freq_array[i,j] == 0.:
                rgb_array[i,j] = empty_color
            else:
                rank_array[i,j] = rank_unique[np.searchsorted(freq_unique,freq_array[i,j])]
                # determine between which listed ranks lies the rank of a particular bin
                for k in range(len(listed_ranks)-1,0,-1):
                    if rank_array[i,j] <= listed_ranks[k]:
                        K = k
                # linearly interpolate color from the colors of neighbouring listed ranks
                F = (rank_array[i,j]-listed_ranks[K-1])/(listed_ranks[K]-listed_ranks[K-1])
                # print(F)
                rgb_array[i,j] = F*colors_rgb[K] + (1-F)*colors_rgb[K-1]
    return rgb_array