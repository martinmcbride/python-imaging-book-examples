# Author:  Martin McBride
# Created: 2021-08-08
# Copyright (C) 2021, Martin McBride
# License: MIT

# Combine images using logical operators
# Logical operations only work with 1-bit images. In these examples we convert
# black and white images to 1 bit images


from PIL import Image, ImageDraw, ImageFont, ImageChops

# Open images as 1 bit
mask1 = Image.open('circle1.png').convert('1')
mask2 = Image.open('circle2.png').convert('1')
composite_image = ImageChops.logical_or(mask1, mask2)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 320), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "Mask 1", font=font, fill=0)
output_image.paste(mask1, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "Mask 2", font=font, fill=0)
output_image.paste(mask2, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "OR", font=font, fill=0)
output_image.paste(composite_image, (x, y))

output_image.save('imagechops-logical-or.png')

composite_image = ImageChops.logical_and(mask1, mask2)
composite_image.save('imagechops-logical-and.png')

composite_image = ImageChops.logical_xor(mask1, mask2)
composite_image.save('imagechops-logical-xor.png')
