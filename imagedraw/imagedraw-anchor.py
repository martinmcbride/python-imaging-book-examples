# Author:  Martin McBride
# Created: 2021-07-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Illustrate text anchor with Pillow

from PIL import Image, ImageDraw, ImageFont

# Text align
image = Image.new('RGB', (600, 400), 'lightgray')

font = ImageFont.truetype('arial.ttf', 30)

draw = ImageDraw.Draw(image)

draw.line((0, 75, 600, 75), fill='blue', width=2)
draw.text((50, 75), 'Align a', anchor='la', font=font, fill='red')
draw.text((150, 75), 'Align t', anchor='lt', font=font, fill='red')
draw.text((250, 75), 'Align m', anchor='lm', font=font, fill='red')

image.save('imagedraw-textanchor.png')
