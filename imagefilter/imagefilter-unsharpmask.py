# Author:  Martin McBride
# Created: 2021-05-24
# Copyright (C) 2021, Martin McBride
# License: MIT

# Apply box blur to an image

from PIL import Image, ImageFilter

image = Image.open('boat-small.jpg')
result_image = image.filter(ImageFilter.UnsharpMask(4))
result_image.save('imagefilter-unsharpmask.jpg')
