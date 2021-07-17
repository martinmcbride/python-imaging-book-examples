# Author:  Martin McBride
# Created: 2021-07-17
# Copyright (C) 2021, Martin McBride
# License: MIT

# Standard image generators

from PIL import Image

from PIL import Image

image = Image.effect_noise(size=(256, 256), sigma=32)
image.save('effect_noise.png')

image = Image.linear_gradient('L')
image.save('linear_gradient.png')

image = Image.radial_gradient('L')
image.save('radial_gradient.png')
