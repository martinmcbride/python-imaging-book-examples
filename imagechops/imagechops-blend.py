# Author:  Martin McBride
# Created: 2021-06-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Composite an image with a grid background
# ImageChops.blend mixes the boat image and grid image using a constant factor.
# In teh example, the factor is 0.2, which means the finale image is 80% boat blended
# with 20% grid.

from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops

image = Image.open('boat-small.jpg')
grid_image = Image.open('grid.png').convert('RGB')
print(grid_image.size)
print(image.mode)
composite_image = ImageChops.blend(image, grid_image, 0.2)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 320), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "Image", font=font, fill=0)
output_image.paste(image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "Grid", font=font, fill=0)
output_image.paste(grid_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "Composite", font=font, fill=0)
output_image.paste(composite_image, (x, y))

output_image.save('imagechops-blend.jpg')
