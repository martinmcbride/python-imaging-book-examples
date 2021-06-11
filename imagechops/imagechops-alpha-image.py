# Author:  Martin McBride
# Created: 2021-06-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Composite an image with a transparent frame
# This doesn't use ImageChops, it works because the frame image is transparent inside the frame.
# Note that we have to use the fram image as a mask when we call paste. This uses the A channel of the
# image as a mask.

from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops

image = Image.open('boat-small.jpg')
frame_image = Image.open('frame.png')
framed_image = image.copy()
framed_image.paste(frame_image, mask=frame_image)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 320), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "Image", font=font, fill=0)
output_image.paste(image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "Frame", font=font, fill=0)
output_image.paste(frame_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "Composite", font=font, fill=0)
output_image.paste(framed_image, (x, y))

output_image.save('imagechops-alpha-image.jpg')
