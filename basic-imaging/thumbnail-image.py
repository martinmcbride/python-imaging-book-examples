# Author:  Martin McBride
# Created: 2021-05-09
# Copyright (C) 2021, Martin McBride
# License: MIT

# Create a thumbnail image

from PIL import Image

image = Image.open('boat.jpg')
image.thumbnail((200, 200))
image.show()

image.save("thumbnail-boat.png")