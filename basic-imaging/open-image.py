# Author:  Martin McBride
# Created: 2021-05-09
# Copyright (C) 2021, Martin McBride
# License: MIT

# Open an image from file.

from PIL import Image

image = Image.open('boat.jpg')
image.show()
