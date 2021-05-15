# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Mirror an image (reverse it horizontally)

from PIL import Image, ImageOps, ImageDraw

image = Image.open('boat-small.jpg')
result_image = ImageOps.mirror(image)
result_image.save('imageops-mirror.jpg')
