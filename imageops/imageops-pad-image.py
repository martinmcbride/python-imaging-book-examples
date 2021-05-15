# Author:  Martin McBride
# Created: 2021-05-14
# Copyright (C) 2021, Martin McBride
# License: MIT

# Pad an image. Original is 420 by 280

from PIL import Image, ImageOps, ImageDraw

# Pad to 450 by 400.
# The target shape has a taller aspect ratio than the image, so we first scale
# the image to be 450 wide, then add padding to make it 400 high.
# Since the y centre value is 0.2, we put 20% of the padding above the image
# and 80% of the padding below the image.
image = Image.open('boat-small.jpg')
result_image = ImageOps.pad(image, (450, 400), centering=(0.5, 0.2))
result_image.save('imageops-pad-450-400.jpg')

# Pad to 400 by 200.
# The target shape has a wider aspect ratio than the image, so we first scale
# the image to be 200 tall, then add padding to make it 400 wide.
# Since the x centre value is 1, we put 100% of the padding to the left
# of the image.
result_image = ImageOps.pad(image, (400, 200), color='tomato', centering=(1, 0.5))
result_image.save('imageops-pad-400-200.jpg')

