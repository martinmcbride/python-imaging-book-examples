# Author:  Martin McBride
# Created: 2021-05-21
# Copyright (C) 2021, Martin McBride
# License: MIT

# Posterize an image
# Reduces the bits per colour to a low value (2 in this case)

from PIL import Image, ImageOps

image = Image.open('boat-small.jpg')
result_image = ImageOps.posterize(image, 2)
result_image.save('imageops-posterize.jpg')
