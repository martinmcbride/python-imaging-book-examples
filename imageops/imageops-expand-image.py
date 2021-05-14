# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Expand an image, adding a 40 pixel border

from PIL import Image, ImageOps

image = Image.open('boat-small.jpg')
result_image = ImageOps.expand(image, 40, 'yellow')
result_image.save('imageops-expand-40.jpg')
