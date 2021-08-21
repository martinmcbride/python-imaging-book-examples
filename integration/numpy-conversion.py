# Author:  Martin McBride
# Created: 2021-08-16
# Copyright (C) 2021, Martin McBride
# License: MIT

# Exchange data with numpy

from PIL import Image
import numpy as np

image = Image.open('boat-small.jpg')

image_array = np.array(image)
print('shape', image_array.shape)

image_array = 255 - image_array
image_array[100:200, 150:350] = np.array([255, 128, 0])

out_image = Image.fromarray(image_array)
out_image.save('numpy-image.jpg')