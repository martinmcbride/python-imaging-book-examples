# Author:  Martin McBride
# Created: 2021-05-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Create colours using the ImageColor module

from PIL import ImageColor

color = ImageColor.getrgb('#804020')
print(color)                         # (128, 64, 32)

color = ImageColor.getrgb('#800')
print(color)                         # (136, 0, 0)

color = ImageColor.getrgb('#00FF0040')
print(color)                         # (0, 255, 0, 64))

