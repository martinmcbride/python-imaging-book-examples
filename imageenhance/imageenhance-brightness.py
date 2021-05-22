# Author:  Martin McBride
# Created: 2021-05-22
# Copyright (C) 2021, Martin McBride
# License: MIT

# Enhance brightness of an image
# Create images with more and less brightness, and create a single
# output image showing less, original and more.

from PIL import Image, ImageEnhance

image = Image.open('boat-small.jpg')
enhancer = ImageEnhance.Brightness(image)
less_image = enhancer.enhance(0.5)

more_image = enhancer.enhance(1.5)

# Place the less image, original image, and more image
# side by side into a single output image
output_image = Image.new('RGB', (1280, 280), 'white')
output_image.paste(less_image, (0, 0))
output_image.paste(image, (430, 0))
output_image.paste(more_image, (860, 0))

output_image.save('imageenhance-brightness.jpg')
