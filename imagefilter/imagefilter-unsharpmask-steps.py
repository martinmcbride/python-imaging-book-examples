# Author:  Martin McBride
# Created: 2021-05-23
# Copyright (C) 2021, Martin McBride
# License: MIT

# Use the ranking filters.
# Create a final image with all the filters.

from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops

image = Image.open('boat-small.jpg')
blur_image = image.filter(ImageFilter.GaussianBlur(4))
diff_image = ImageChops.subtract(image, blur_image)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 320), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "A - original", font=font, fill=0)
output_image.paste(image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "B - blurred", font=font, fill=0)
output_image.paste(blur_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "C - difference", font=font, fill=0)
output_image.paste(diff_image, (x, y))

output_image.save('imagefilter-unsharpmask-steps.jpg')
