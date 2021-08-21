# Author:  Martin McBride
# Created: 2021-08-08
# Copyright (C) 2021, Martin McBride
# License: MIT

# Get image exif information

from PIL import Image, ExifTags

jpeg_image = Image.open('boat.jpg')
exif = jpeg_image.getexif()
for tag in exif:
    tagname = ExifTags.TAGS[tag]
    value = exif[tag]
    print('{}: {}'.format(tagname, value))

'''
ImageWidth: 600
ImageLength: 400
ResolutionUnit: 2
ExifOffset: 170
Make: Canon
Model: Canon EOS 300D DIGITAL
Software: PaintShop Pro 20.00                    
Orientation: 1
YCbCrSubSampling: 1
DateTime: 2007:05:31 14:04:43
InterColorProfile: b'...'
XResolution: 180.0
YResolution: 180.0
'''