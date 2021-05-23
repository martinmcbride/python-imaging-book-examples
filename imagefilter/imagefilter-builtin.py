# Author:  Martin McBride
# Created: 2021-05-23
# Copyright (C) 2021, Martin McBride
# License: MIT

# Use the built in filters. These filters have no parameters
# Create

from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open('boat-small.jpg')
blur_image = image.filter(ImageFilter.BLUR)
contour_image = image.filter(ImageFilter.CONTOUR)
detail_image = image.filter(ImageFilter.DETAIL)
edge_enhance_image = image.filter(ImageFilter.EDGE_ENHANCE)
edge_enhance_more_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
emboss_image = image.filter(ImageFilter.EMBOSS)
find_edges_image = image.filter(ImageFilter.FIND_EDGES)
sharpen_image = image.filter(ImageFilter.SHARPEN)
smooth_image = image.filter(ImageFilter.SMOOTH)
smooth_more_image = image.filter(ImageFilter.SMOOTH_MORE)

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 1280), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "BLUR", font=font, fill=0)
output_image.paste(blur_image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "CONTOUR", font=font, fill=0)
output_image.paste(contour_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "DETAIL", font=font, fill=0)
output_image.paste(detail_image, (x, y))

x, y = 0, 320
draw.text((x+10, y+285), "EDGE_ENHANCE", font=font, fill=0)
output_image.paste(edge_enhance_image, (x, y))

x, y = 430, 320
draw.text((x+10, y+285), "EDGE_ENHANCE_MORE", font=font, fill=0)
output_image.paste(edge_enhance_more_image, (x, y))

x, y = 860, 320
draw.text((x+10, y+285), "EMBOSS", font=font, fill=0)
output_image.paste(emboss_image, (x, y))

x, y = 0, 640
draw.text((x+10, y+285), "FIND_EDGES", font=font, fill=0)
output_image.paste(find_edges_image, (x, y))

x, y = 430, 640
draw.text((x+10, y+285), "SHARPEN", font=font, fill=0)
output_image.paste(sharpen_image, (x, y))

x, y = 860, 640
draw.text((x+10, y+285), "SMOOTH", font=font, fill=0)
output_image.paste(smooth_image, (x, y))

x, y = 430, 960
draw.text((x+10, y+285), "SMOOTH_MORE", font=font, fill=0)
output_image.paste(smooth_more_image, (x, y))

output_image.save('imagefilter-builtin.jpg')
