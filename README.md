### Visualizing the Complex Exponential Function

Simple code to visualize the real and imaginary components of the complex
exponential function:

![exp](https://github.com/betanot/plot-complex/blob/master/exp.png)

#### Issues with Elpy Execution

Elpy currently is having issues executing certain blocks of Python code in
Emacs when using the Python3 shell interpreter:
```
ax_imag.plot_surface(z.real, z,imag, w.imag,
                     rstride = 1, cstride = 1, alpha = 0.5,
                     facecolors = color)
```
When run, at first Elpy was not sending whole blocks to the interpreter,
which would return a parshing error at the comma on the first line.
Currently, it complains that there is no 'imag' object. When the code is run
directly in the interpreter, however, it works fine.