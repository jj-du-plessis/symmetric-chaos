"""Parameter Lists

A number of parameter lists are defined which yield symmetric attractors. The
parameters in these lists are ordered as follows:
    lambda, alpha, beta, gamma, omega, n

Each variable is named according to the symmetry group of the attractor. The
symbol is D when the symmetry is dihedral and Z when it is only cyclic, while
the number is the parameter n.

These parameters can be customised, but you'll often find an exception is
raised or the generated figure is blank, perhaps because there is no attractor
or the attractor is a fixed point.
"""

D3  = [1.5, -1.0, 0.1, -0.83, 0.0, 3]
D6 = [-2.6, 3.8, -1.1, 0.9, -0.00, 6]
D19 = [2.429, -2.45, 0.0, 1.1, 0.0, 19]
D23 = [2.409, -2.5, 0.0, 0.9, 0.0, 23]
Z3 = [1.575, -1.03, 0.028, -0.79, 0.115, 3]
Z4 = [-1.88, 1.96, 0.03, 0.98, -0.14, 4]
Z5 = [2.60, -2.7, -0.29, 0.251, 0.21, 5]

# here are some additional parameter lists from the book Symmetry in Chaos

mayan_bracelet = [-2.08, 1.0, -0.1, 0.167, 0.0, 7]
emperors_cloak = [-1.806, 1.806, 0.0, 1.0, 0.0, 5]
ima_logo = [1.455, -1.0, 0.03, -0.8, 0.0, 3]
