# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Colorize a greyscale image

from PIL import Image, ImageOps

image = Image.open('boat-small-grayscale.jpg')

# Colorise blue to white
result_image = ImageOps.colorize(image, 'darkblue', 'white')
result_image.save('imageops-colorize-blue.jpg')

# Colorise blue to yellow
result_image = ImageOps.colorize(image, 'darkblue', 'yellow')
result_image.save('imageops-colorize-yellow.jpg')

# Colorise purple to white with blue mid tones
result_image = ImageOps.colorize(image, 'purple', 'white', mid='mediumslateblue')
result_image.save('imageops-colorize-purple.jpg')

# Colorise blue to white with black point and white point
result_image = ImageOps.colorize(image, 'darkblue', 'white', blackpoint=64, whitepoint=192)
result_image.save('imageops-colorize-blue-bp.jpg')
