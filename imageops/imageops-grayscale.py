# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Convert a colour image to greyscale

from PIL import Image, ImageOps

image = Image.open('boat-small.jpg')
result_image = ImageOps.grayscale(image)
result_image.save('imageops-grayscale.jpg')
