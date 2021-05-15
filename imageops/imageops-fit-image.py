# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Fit an image. Original is 420 by 280

from PIL import Image, ImageOps, ImageDraw

# Fit to 450 by 400.
# The target shape has a taller aspect ratio than the image, so we first scale
# the image to be 400 tall, then crop the image to 450 wide.
image = Image.open('boat-small.jpg')
result_image = ImageOps.fit(image, (450, 400))
result_image.save('imageops-fit-450-400.jpg')

# Fit to 400 by 200.
# The target shape has a wider aspect ratio than the image, so we first scale
# the image to be 400 wide, then crop the image to 200 tall.
result_image = ImageOps.fit(image, (400, 200))
result_image.save('imageops-fit-400-200.jpg')

