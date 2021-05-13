# Author:  Martin McBride
# Created: 2021-05-11
# Copyright (C) 2021, Martin McBride
# License: MIT

# Create colours using the ImageColor module

from PIL import ImageColor

color = ImageColor.getrgb('#804020')
print(color)                         # (128, 64, 32)

color = ImageColor.getrgb('#812')
print(color)                         # (136, 17, 34)

color = ImageColor.getrgb('#00FF0040')
print(color)                         # (0, 255, 0, 64))

color = ImageColor.getrgb('rgb(128, 10, 50)')
print(color)                         # (128, 10, 50)

color = ImageColor.getrgb('rgb(10%, 50%, 0%)')
print(color)                         # (26, 128, 0)

color = ImageColor.getrgb('hsl(180, 100%, 50%)')
print(color)                         # (0, 255, 255)

color = ImageColor.getrgb('hsv(180, 100%, 100%)')
print(color)                         # (0, 255, 255)

color = ImageColor.getrgb('orange')
print(color)                         # (255, 165, 0)

