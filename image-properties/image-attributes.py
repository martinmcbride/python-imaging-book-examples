# Author:  Martin McBride
# Created: 2021-05-09
# Copyright (C) 2021, Martin McBride
# License: MIT

# Print the attributes of different types of images

from PIL import Image

new_image = Image.new('L', (400, 300), 'darkgrey')
jpeg_image = Image.open('boat.jpg')
gif_image = Image.open('spinning-cube-ani.gif')

print("File name:")
print(" new_image", getattr(new_image, "filename", None))    # None
print(" jpeg_image", getattr(jpeg_image, "filename", None))  # 'boat.jpg'
print(" gif_image", getattr(gif_image, "filename", None))    # 'spinning-cube-ani.gif'

print("File format:")
print(" new_image", getattr(new_image, "format", None))      # None
print(" jpeg_image", getattr(jpeg_image, "format", None))    # 'JPEG'
print(" gif_image", getattr(gif_image, "format", None))      # 'GIF'

print("Mode:")
print(" new_image", new_image.mode)                          # 'L'
print(" jpeg_image", jpeg_image.mode)                        # 'RGB'
print(" file_image", jpeg_image.mode)                        # 'RGB'

print("Bands:")
print(" new_image", new_image.getbands())                    # ('L',)
print(" jpeg_image", jpeg_image.getbands())                  # ('R', 'G', 'B')
print(" file_image", jpeg_image.getbands())                  # ('R', 'G', 'B')

print("Size:")
print(" new_image", new_image.size)                          # (400, 300)
print(" jpeg_image", jpeg_image.size)                        # (600, 400)
print(" gif_image", gif_image.size)                          # (400, 400)

print("Width:")
print(" new_image", new_image.width)                         # 400
print(" jpeg_image", jpeg_image.width)                       # 600
print(" gif_image", gif_image.width)                         # 400

print("Height:")
print(" new_image", new_image.height)                        # 300
print(" jpeg_image", jpeg_image.height)                      # 400
print(" gif_image", gif_image.height)                        # 400

print("Palette:")
print(" new_image", new_image.palette)                       # None
print(" jpeg_image", jpeg_image.palette)                     # None
print(" gif_image", gif_image.palette)                       # <ImagePalette>

print("Info:")
print(" new_image", new_image.info)                          # None
print(" jpeg_image", jpeg_image.info)                        # {various}
print(" gif_image", gif_image.info)                          # {various}

print("Frames:")
print(" new_image", getattr(new_image, "n_frames", None))    # None
print(" jpeg_image", getattr(jpeg_image, "n_frames", None))  # None
print(" gif_image", getattr(gif_image, "n_frames", None))    # 80

print("Animation:")
print(" new_image", getattr(new_image, "is_animated", None))    # None
print(" jpeg_image", getattr(jpeg_image, "is_animated", None))  # None
print(" gif_image", getattr(gif_image, "is_animated", None))    # True

