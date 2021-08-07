# Author:  Martin McBride
# Created: 2021-07-19
# Copyright (C) 2021, Martin McBride
# License: MIT

# deform an image

from PIL import Image, ImageOps, ImageDraw
import math

class SingleDeformer:

    def getmesh(self, img):
        w, h = img.size

        #Map whole image rectangle onto whole image rectangle
        return [(
                # target rectangle (1)
                (200, 100, 300, 200),
                # corresponding source quadrilateral (1)
                # (NW, SW, SE, and NE. see method=QUAD)
                (0, 0, 0, 100, 100, 200, 100, 0)
                )]

class WaveDeformer:

    def transform(self, x, y):
        y = y + 10*math.sin(x/40)
        return x, y

    def transform_rectangle(self, x0, y0, x1, y1):
        return (*self.transform(x0, y0),
                *self.transform(x0, y1),
                *self.transform(x1, y1),
                *self.transform(x1, y0),
                )

    def getmesh(self, img):
        self.w, self.h = img.size
        gridspace = 20

        target_grid = []
        for x in range(0, self.w, gridspace):
            for y in range(0, self.h, gridspace):
                target_grid.append((x, y, x + gridspace, y + gridspace))

        source_grid = [self.transform_rectangle(*rect) for rect in target_grid]

        return [t for t in zip(target_grid, source_grid)]

image = Image.open('boat-small.jpg')
result_image = ImageOps.deform(image, SingleDeformer())
result_image.save('imageops-deform.jpg')
result_image = ImageOps.deform(image, WaveDeformer())
result_image.save('imageops-wavedeform.jpg')

grid = Image.new('RGB', image.size, 'grey')
mesh = WaveDeformer().getmesh(grid)
draw = ImageDraw.Draw(grid)
for target, source in mesh:
    x, y = source[0], source[1]
    draw.ellipse((x-2, y-2, x+2, y+2), fill='black')
grid.save('imageops-sourcegrid.png')

grid = Image.open('boat-small.jpg')
mesh = SingleDeformer().getmesh(grid)
draw = ImageDraw.Draw(grid)
for target, source in mesh:
    x, y = source[0], source[1]
    draw.ellipse((x-2, y-2, x+2, y+2), fill='black')
    x, y = source[2], source[3]
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill='black')
    x, y = source[4], source[5]
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill='black')
    x, y = source[6], source[7]
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill='black')
grid.save('imageops-boatsourcegrid.png')

