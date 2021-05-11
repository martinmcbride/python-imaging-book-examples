# Author:  Martin McBride
# Created: 2021-05-09
# Copyright (C) 2021, Martin McBride
# License: MIT

# Create a mandelbrot image using the Image factory function effect_mandelbrot.
# Show the image in a window.

from PIL import Image

image = Image.effect_mandelbrot((520, 440), (-2, -1.1, 0.6, 1.1), 256)
image.show()
