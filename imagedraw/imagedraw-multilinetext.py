# Author:  Martin McBride
# Created: 2021-07-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Draw simple text with Pillow

from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (600, 150), 'lightgrey')

font = ImageFont.truetype('arial.ttf', 50)

draw = ImageDraw.Draw(image)

x, y = 100, 50
draw.ellipse((x-5, y-5, x+5, y+5), fill='blue')
draw.multiline_text((x, y), 'Multiline\nText', anchor='ls', font=font, fill='red')

box = draw.multiline_textbbox((x, y), 'Multiline\nText', anchor='ls', font=font)
draw.rectangle(box, outline='black', width=2)

x, y = 350, 50
draw.ellipse((x-5, y-5, x+5, y+5), fill='blue')
draw.multiline_text((x, y), 'Multiline\nText', anchor='ls', align='center', spacing=20, font=font, fill='red')

image.save('imagedraw-multilinetext.png')

