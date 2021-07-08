# Author:  Martin McBride
# Created: 2021-07-07
# Copyright (C) 2021, Martin McBride
# License: MIT

# Draw shapes with Pillow

from PIL import Image, ImageDraw

# Rectangles
image = Image.open('boat-small.jpg')

draw = ImageDraw.Draw(image)
draw.rectangle((20, 100, 80, 250), 'red')
draw.rectangle((150, 100, 250, 200), outline=(0, 128, 0), width=6)
draw.rectangle((300, 50, 350, 200), fill='white', outline='black', width=10)

image.save('imagedraw-rectangles.jpg')

# Other shapes
image = Image.new('RGB', (600, 400), 'lightgray')

draw = ImageDraw.Draw(image)
draw.line((50, 50, 100, 150), fill='red', width=6)
draw.line((50, 200, 75, 300, 100, 250, 75, 200), fill='blue', width=10, joint='curve')
draw.polygon((150, 50, 220, 150, 250, 50), fill='green')
draw.regular_polygon((200, 300, 75), n_sides=6, rotation=10, fill='orange')
draw.ellipse((300, 50, 450, 150), outline='black', width=4)
draw.arc((300, 200, 450, 350), start=90, end=200, fill='yellow', width=4)
draw.chord((400, 200, 550, 350), start=90, end=200, fill='cyan')
draw.pieslice((500, 200, 650, 350), start=90, end=200, fill='magenta')

image.save('imagedraw-shapes.png')
