# Author:  Martin McBride
# Created: 2021-07-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Illustrate text anchor with Pillow

from PIL import Image, ImageDraw, ImageFont

# Text align
image = Image.new('RGB', (400, 350), 'lightgray')

font = ImageFont.truetype('arial.ttf', 30)

draw = ImageDraw.Draw(image)

x, y = 50, 75
draw.ellipse((x-5, y-5, x+5, y+5), fill='blue')
draw.text((x, y), 'Align la', anchor='la', font=font, fill='red')

x, y = 50, 150
draw.ellipse((x-5, y-5, x+5, y+5), fill='blue')
draw.text((x, y), 'Align ls', anchor='ls', font=font, fill='red')

x, y = 150, 225
draw.ellipse((x-5, y-5, x+5, y+5), fill='blue')
draw.text((x, y), 'Align mt', anchor='mt', font=font, fill='red')

x, y = 250, 300
draw.ellipse((x-5, y-5, x+5, y+5), fill='blue')
draw.text((x, y), 'Align rm', anchor='rm', font=font, fill='red')

image.save('imagedraw-textanchor.png')
