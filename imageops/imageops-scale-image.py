# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Scale an image by 2 and by 0.5

from PIL import Image, ImageOps, ImageDraw

image = Image.open('boat-small.jpg')
result_image = ImageOps.scale(image, 2)
result_image.save('imageops-scale-2.jpg')

result_image = ImageOps.scale(image, 0.5)
result_image.save('imageops-scale-5.jpg')

