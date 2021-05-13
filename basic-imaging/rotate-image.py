# Author:  Martin McBride
# Created: 2021-05-09
# Copyright (C) 2021, Martin McBride
# License: MIT

# Rotate an image by 180 degrees

from PIL import Image

image = Image.open('boat.jpg')
rotated = image.rotate(180)
rotated.show()

rotated.save("rotated-boat.png")