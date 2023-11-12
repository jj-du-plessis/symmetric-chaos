# Symmetric Chaos
This is based on the book _Symmetry in Chaos_ by Michael Field and Martin Golubitsky. By iterating the complex map
$$f(z) = (\lambda+\alpha z\bar{z}+\beta\thinspace\mathrm{Re}(z^n) + \omega i)z + \gamma\bar{z}^{n-1},$$
where $\lambda,\alpha,\beta,\omega,\gamma$ are real parameters and $n$ is a positive integer, these points often sample a chaotic attractor. The symmetry group of this attractor is the dihedral group $\boldsymbol{\mathrm{D}}_n$ if $\omega=0$, else it is the cyclic group $\boldsymbol{\mathrm{Z}}_n$.

## Scripts
Run the following scripts to generate the appropriate figures:
- The script `plot_points.py` iterates the map $f$ many times and plots the real and imaginary parts of these points as (x,y) coordinate pairs and saves the figure.
- The script `compute_histogram.py` iterates $f$ and saves a 2D histogram of the computed points.
- The script `plot_density.py` uses the 2D histogram from `compute_histogram.py` and plots the density of points in each bin using color to distinguish to densities.

## Parameters and Palettes
- Several variations of the parameters used to define $f$ are given in `modules/parameters.py`. You can come up with your own parameters, but this may involve much trial and error. The book _Symmetry in Chaos_ has a table of usable parameters in the appendix.
- Several colour palettes used in the density plots for these attractors are given in `modules/palettes.py`. You can customise these.

## Software Versions
This code was written using the following Python and package versions:
- Python 3.10.12
- NumPy 1.23.4
- Numba 0.56.3
- Matplotlib 3.6.1
