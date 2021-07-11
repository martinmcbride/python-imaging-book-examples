# Author:  Martin McBride
# Created: 2021-07-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Draw simple text with Pillow

from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (600, 200), 'lightgrey')

font = ImageFont.truetype('arial.ttf', 100)

draw = ImageDraw.Draw(image)

draw.ellipse((95, 45, 105, 55), fill='blue')
draw.text((100, 50), 'ABCdefg', font=font, fill='red')

image.save('imagedraw-text.png')

