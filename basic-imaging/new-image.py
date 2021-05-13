# Author:  Martin McBride
# Created: 2021-05-09
# Copyright (C) 2021, Martin McBride
# License: MIT

# Create a new image

from PIL import Image, ImageColor

image = Image.new('RGB', (400, 300), ImageColor.getrgb('gold'))
image.show()

image.save("gold.png")