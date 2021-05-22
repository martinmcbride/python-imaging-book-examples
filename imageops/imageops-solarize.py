# Author:  Martin McBride
# Created: 2021-05-21
# Copyright (C) 2021, Martin McBride
# License: MIT

# solarize an image
# Inverts any colour value that is over 128

from PIL import Image, ImageOps

image = Image.open('boat-small.jpg')
result_image = ImageOps.solarize(image)
result_image.save('imageops-solarize.jpg')
