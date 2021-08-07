# Author:  Martin McBride
# Created: 2021-07-18
# Copyright (C) 2021, Martin McBride
# License: MIT

# Apply autocontrast to an image

from PIL import Image, ImageOps

image = Image.open('boat-small.jpg')
result_image = ImageOps.autocontrast(image)
result_image.save('imageops-autocontrast.jpg')
