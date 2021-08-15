# Author:  Martin McBride
# Created: 2021-08-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Access individual pixels

from PIL import Image
import math

image = Image.open('boat.jpg')

pixels = image.load()
for x in range(image.size[0]-20):
    for y in range(image.size[1]):
        r, _, _ = pixels[x, y]
        _, g, _ = pixels[x+10, y]
        _, _, b = pixels[x+20, y]
        pixels[x, y] = (r, g, b)

image.close()
image.save('deregister.jpg')

image = Image.new('L', (256, 256), 'black')

pixels = image.load()
for x in range(256):
    for y in range(256):
        pixels[x, y] = 128+int(63*math.sin(x/10) + 63*math.sin(y/10))

image.close()
image.save('sine-pattern.jpg')