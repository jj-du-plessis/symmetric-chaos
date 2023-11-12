"""Plot Iterated Points

This script iterates a complex map (defined in modules.map using parameters
from modules.parameters) a number of times and, after discarding the transient,
returns a 1D arrary for the real parts of the complex iterates and also for the
imaginary parts. These points are then plotted as (x,y) coordinate pairs and
saved as a figure in the figures directory.

Variables:
    symmetry:   symmetry group of the attractor which arises from the
                corresponding parameter list defined in the parameters module
    iterations: number of iterated points to save
    transient:  number of transient points to ignore
    parameters: parameter list whose name is the value of the symmetry variable
    z:          random initial condition
    x,y:        1D arrays of the real and imaginary parts of the complex
                iterates, respectively
"""

import numpy as np
import matplotlib.pyplot as plt
from modules.map import iterate_map
import modules.parameters as params

symmetry = "D19"
iterations = 10000000    # if you make this too large, you'll run out of RAM
transient  = 1000
parameters = getattr(params,symmetry)
z = (2*np.random.rand()-1 + (2*np.random.rand()-1)*1j)/3

x,y = iterate_map(z,transient,iterations,*parameters)

plt.figure(figsize=(4,4))
plt.plot(x[transient:],y[transient:],"k,",alpha=0.03)
plt.axis("off")
plt.margins(0)
plt.tight_layout(pad=0)
plt.savefig("figures/"+symmetry+"_points.png",dpi=150)
