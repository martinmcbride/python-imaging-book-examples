# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Crop an image, removing a 20 pixel border

from PIL import Image, ImageOps, ImageDraw

image = Image.open('boat-small.jpg')
result_image = ImageOps.crop(image, 20)
result_image.save('imageops-crop-20.jpg')

# Show the crop outline on the original image

draw = ImageDraw.Draw(image)
draw.rectangle([20, 20, 400, 260], outline='red', width=2)
image.save('imageops-crop-outline.jpg')
