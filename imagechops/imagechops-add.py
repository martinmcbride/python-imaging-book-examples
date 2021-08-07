# Author:  Martin McBride
# Created: 2021-06-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Add two images
# The boat is added to a gradient.
# The main (triple) features shows the boat, patches and added features.
# There is also an example using add with scaling and add modulo.

from PIL import Image, ImageDraw, ImageFont, ImageChops

image = Image.open('boat-small.jpg')
gradient_image = Image.open('greygradient.png').convert('RGB')
composite_image = ImageChops.add(image, gradient_image)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 320), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "Image", font=font, fill=0)
output_image.paste(image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "Gradient", font=font, fill=0)
output_image.paste(gradient_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "Composite", font=font, fill=0)
output_image.paste(composite_image, (x, y))

output_image.save('imagechops-add.jpg')

composite_image = ImageChops.add(image, gradient_image, 2)
composite_image.save('imagechops-add-scaled.jpg')

composite_image = ImageChops.add_modulo(image, gradient_image)
composite_image.save('imagechops-add-modulo.jpg')
