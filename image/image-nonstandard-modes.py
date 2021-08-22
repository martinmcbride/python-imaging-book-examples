# Author:  Martin McBride
# Created: 2021-08-22
# Copyright (C) 2021, Martin McBride
# License: MIT

# Handle non-standard modes

from PIL import Image

# LA image
la_image = Image.new('LA', (200, 200), (64, 128))
print('LA bands', la_image.getbands())      # ('L', 'A')
print('Pixel', la_image.getpixel((0, 0)))   # (64, 128)

# Convert the image to RGBA
converted_image = la_image.convert(mode="RGBA")
print('Converted bands', converted_image.getbands())  # ('R', 'G', 'B', 'A')
print('Pixel', converted_image.getpixel((0, 0)))      # (64, 64, 64, 128)

# RGBa image
rgba_image = Image.new('RGBa', (200, 200), (64, 32, 0, 64))
print('RGBa bands', rgba_image.getbands())   # ('R', 'G', 'B', 'a')
print('Pixel', rgba_image.getpixel((0, 0)))  # (64, 32, 0, 64)

# Convert the image to RGBA
converted_image = rgba_image.convert(mode="RGBA")
print('Converted bands', converted_image.getbands())  # ('R', 'G', 'B', 'A')
print('Pixel', converted_image.getpixel((0, 0)))      # (255, 127, 0, 64)

