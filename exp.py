# Code demonstrating the plotting of complex functions

import numpy
import sympy

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm, colors
from matplotlib import pyplot as plt

branching_number = 2

Nr = 16
Ntheta = 32

# Compute the theta,r domain
theta = numpy.linspace(0, 2 * numpy.pi * branching_number, Ntheta)
r = numpy.linspace(0, 1, Nr)
Theta, R = numpy.meshgrid(theta, r)

z = R * numpy.exp(1j * Theta)

# Compute z = w^2
w = numpy.sqrt(R) * numpy.exp(1j * Theta/2)

# Color by argument
arguments = numpy.angle(w)
norm = colors.Normalize(arguments.min(), arguments.max())
color = cm.jet(norm(arguments))

fig = plt.figure(figsize = (16,8))

# Plot the real part
ax_real = fig.add_subplot(1, 2, 1,
                          projection = '3d')
ax_real.plot_surface(z.real, z.imag, w.real,
                     rstride = 1, cstride = 1, alpha = 0.5,
                     facecolors = color)

# Plot the imaginary part
ax_imag = fig.add_subplot(1, 2, 2, projection = '3d')
ax_imag.plot_surface(z.real, z,imag, w.imag,
                     rstride = 1, cstride = 1, alpha = 0.5,
                     facecolors = color)
