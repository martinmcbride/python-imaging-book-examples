# Author:  Martin McBride
# Created: 2021-08-08
# Copyright (C) 2021, Martin McBride
# License: MIT

# Get an image palette

from PIL import Image

gif_image = Image.open('spinning-cube-ani.gif')

palette = gif_image.getpalette()
print(len(palette))              # 768
print(palette)                   # [255, 255, 255, 64, 64, 64 ... 127, 126, 24, 114, 24, 144]
