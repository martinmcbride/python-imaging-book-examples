# Author:  Martin McBride
# Created: 2021-07-07
# Copyright (C) 2021, Martin McBride
# License: MIT

# Draw paths with Pillow

from PIL import Image, ImageDraw, ImagePath
import math
import random

count = 201

def curve(x):
    y = (x-100)**2/100
    return x, y

points = [curve(t) for t in range(0, count, 10)]

# Creating and drawing a path
image = Image.new('RGB', (400, 300), 'lightgrey')

draw = ImageDraw.Draw(image)

path = ImagePath.Path(points)
path.compact()

draw.line(path, fill='blue', width=4)

image.save('imagedraw-path.png')

# transforming a path translate and rotate
image = Image.new('RGB', (400, 300), 'lightgrey')

draw = ImageDraw.Draw(image)

c = math.cos(math.pi/6)
s = math.sin(math.pi/6)
path = ImagePath.Path(points)
path.transform([c, -s, 100, s, c, 100])
path.compact()

draw.line(path, fill='blue', width=4)

image.save('imagedraw-transformpath.png')

# Randomise a path
def sketch(x, y):
    return x + random.randrange(6), y + random.randrange(6)

image = Image.new('RGB', (400, 300), 'lightgrey')

draw = ImageDraw.Draw(image)

path = ImagePath.Path(points)
path.transform([c, -s, 100, s, c, 100])
path.compact()
path.map(sketch)

draw.line(path, fill='blue', width=4)

image.save('imagedraw-sketchpath.png')

