from numba import jit
import numpy as np

@jit
def iterate_map(z,transient,iterations,l,a,b,g,w,n):
    def f(z):
        return (l+a*z*z.conjugate()+b*(z**n).real + w*1j)*z + g*z.conjugate()**(n-1)
    
    for i in range(transient):
        z = f(z)

    x = np.zeros(iterations)
    y = np.zeros(iterations)
    x[0] = z.real
    y[0] = z.imag
    for i in range(1,iterations):
        z = f(z)
        x[i] = z.real
        y[i] = z.imag
    return x,y