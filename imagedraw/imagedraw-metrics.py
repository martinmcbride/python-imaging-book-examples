# Author:  Martin McBride
# Created: 2021-07-07
# Copyright (C) 2021, Martin McBride
# License: MIT

# Illustrate font and text metrics with Pillow
# Font metrics depend only on the font itself, including the font size.
# Text metrics depend on the specific text used, as well as the font and font size.

from PIL import Image, ImageDraw, ImageFont

# Font metrics
image = Image.new('RGB', (600, 250), 'lightgray')

font = ImageFont.truetype('arial.ttf', 100)
ascent, descent = font.getmetrics()

draw = ImageDraw.Draw(image)

text = 'ABCdefg'
x, y = 50, 150

draw.line((0, y, 600, y), fill='blue', width=2)
draw.line((0, y-ascent, 600, y-ascent), fill='blue', width=2)
draw.line((0, y+(descent-ascent)/2, 600, y+(descent-ascent)/2), fill='blue', width=2)
draw.line((0, y+descent, 600, y+descent), fill='blue', width=2)
draw.text((x, y), text, anchor='ls', font=font, fill='red')

labelfont = ImageFont.truetype('arial.ttf', 20)
draw.text((480, y-ascent-5), 'ascender', anchor='lb', font=labelfont, fill='blue')
draw.text((480, y-5), 'baseline', anchor='lb', font=labelfont, fill='blue')
draw.text((480, y+(descent-ascent)/2-5), 'middle', anchor='lb', font=labelfont, fill='blue')
draw.text((480, y+descent+5), 'descender', anchor='lt', font=labelfont, fill='blue')

image.save('imagedraw-fontmetrics.png')

# Text metrics
image = Image.new('RGB', (600, 300), 'lightgrey')

font = ImageFont.truetype('arial.ttf', 100)
ascent, descent = font.getmetrics()

draw = ImageDraw.Draw(image)

text = 'ABCdefg'
x, y = 50, 150
offsetx, offsety = font.getoffset(text)
width, height = font.getsize(text)

draw.line((0, y-ascent, 600, y-ascent), fill='grey', width=2)
draw.line((0, y-ascent+offsety, 600, y-ascent+offsety), fill='blue', width=2)
draw.line((0, y-ascent+height, 600, y-ascent+height), fill='blue', width=2)
draw.line((x+offsetx, 0, x, 300), fill='green', width=2)
draw.line((x+width/2, 0, x+width/2, 300), fill='green', width=2)
draw.line((x+width, 0, x+width, 300), fill='green', width=2)
draw.text((x, y), text, anchor='ls', font=font, fill='red')

labelfont = ImageFont.truetype('arial.ttf', 20)
draw.text((480, y-ascent-10), 'ascender', anchor='lb', font=labelfont, fill='grey')
draw.text((480, y-ascent+offsety+10), 'top', anchor='lt', font=labelfont, fill='blue')
draw.text((480, y-ascent+height+10), 'bottom', anchor='lt', font=labelfont, fill='blue')
draw.text((x+offsetx+5, 250), 'left', anchor='lt', font=labelfont, fill='green')
draw.text((x+width/2+5, 250), 'middle', anchor='lt', font=labelfont, fill='green')
draw.text((x+width+5, 250), 'right', anchor='lt', font=labelfont, fill='green')

image.save('imagedraw-textmetrics.png')

