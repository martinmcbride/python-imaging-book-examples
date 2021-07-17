# Author:  Martin McBride
# Created: 2021-07-17
# Copyright (C) 2021, Martin McBride
# License: MIT

# Open an image

from PIL import Image

# Open an image of any supported format
image = Image.open("boat-small.jpg")
image.close()

# Only open PNG or JPEG images
image = Image.open("boat-small.jpg", formats=['PNG', 'JPEG'])
image.close()

# Only open PNG images. This will fail, because it is a JPEG file
image = Image.open("boat-small.jpg", formats=['PNG'])
image.close()