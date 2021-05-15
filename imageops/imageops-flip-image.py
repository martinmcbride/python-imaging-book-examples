# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Flip an image (reverse it vertically)

from PIL import Image, ImageOps, ImageDraw

image = Image.open('boat-small.jpg')
result_image = ImageOps.flip(image)
result_image.save('imageops-flip.jpg')
