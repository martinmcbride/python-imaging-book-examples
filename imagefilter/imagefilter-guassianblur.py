# Author:  Martin McBride
# Created: 2021-05-23
# Copyright (C) 2021, Martin McBride
# License: MIT

# Apply gaussian blur to an image

from PIL import Image, ImageFilter

image = Image.open('boat-small.jpg')
result_image = image.filter(ImageFilter.GaussianBlur(4))
result_image.save('imagefilter-gaussianblur.jpg')
