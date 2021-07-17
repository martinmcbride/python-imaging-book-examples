# Author:  Martin McBride
# Created: 2021-07-17
# Copyright (C) 2021, Martin McBride
# License: MIT

# Handle image bands

from PIL import Image

# Find the bands of the boats image
image = Image.open("boat-small.jpg")
bands = image.getbands()
print(bands) # ('R', 'G', 'B')

# Get the R, G and B channels as separate greyscale images
# Bands canbe identiofied by name 'R', 'G', 'B' ot index 0, 1, 2
red_image = image.getchannel('R')
red_image.save('red_component.png')

green_image = image.getchannel(1)
green_image.save('green_component.png')

blue_image = image.getchannel(2)
blue_image.save('blue_component.png')

# Alternatively, split creates all 3 in one go (this is equivalent to all 3 getchannel calls above
red_image, green_image, blue_image = image.split()

# Merge takes a set of bands and creates a single file. This will recreate the original file
mixed_image = Image.merge('RGB', [red_image, green_image, blue_image])
mixed_image.save('mixed_component.png')

# Here we take the red band and merge it with blank green and blue bands to create a red separation
# This is the red band, shown as a red colour

blank = Image.new('L', image.size)
red_sep = Image.merge('RGB', [red_image, blank, blank])
red_sep.save('red_sep.png')