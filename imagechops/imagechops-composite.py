# Author:  Martin McBride
# Created: 2021-06-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Composite an image with a starburst background
# ImageChops.composite mixes the boat image and starburst image using a mask.
# Where the mask is white, the boat is visible, where the mask is black the starburst is
# visible, where the mask is grey the two are blended depending on the grey level.
# This allows the boat image to gradually fade out towards the edges.
# The mask image must be a single channel, so we convert the mode to `L` as we read it in.

from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops

image = Image.open('boat-small.jpg')
border_image = Image.open('border.png').convert('RGB')
mask_image = Image.open('vignette.png').convert('L')
composite_image = ImageChops.composite(image, border_image, mask_image)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 320), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "Border", font=font, fill=0)
output_image.paste(border_image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "Mask", font=font, fill=0)
output_image.paste(mask_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "Composite", font=font, fill=0)
output_image.paste(composite_image, (x, y))

output_image.save('imagechops-composite.jpg')
