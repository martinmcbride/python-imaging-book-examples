# Author:  Martin McBride
# Created: 2021-05-21
# Copyright (C) 2021, Martin McBride
# License: MIT

# Invert an image

from PIL import Image, ImageOps

image = Image.open('boat-small.jpg')
result_image = ImageOps.invert(image)
result_image.save('imageops-invert.jpg')
