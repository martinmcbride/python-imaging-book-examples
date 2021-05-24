# Author:  Martin McBride
# Created: 2021-05-23
# Copyright (C) 2021, Martin McBride
# License: MIT

# Use the ranking filters.
# Create a final image with all the filters.

from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open('boat-small.jpg')
min_image = image.filter(ImageFilter.MinFilter())
max_image = image.filter(ImageFilter.MaxFilter())
median_image = image.filter(ImageFilter.MedianFilter())
mode_image = image.filter(ImageFilter.ModeFilter())
rank_image = image.filter(ImageFilter.RankFilter(3, 6))

# Place the images in a grid, with captions
output_image = Image.new('RGB', (1280, 640), 'white')
draw = ImageDraw.Draw(output_image)
font = ImageFont.truetype("Arial.ttf", 20)

x, y = 0, 0
draw.text((x+10, y+285), "Min", font=font, fill=0)
output_image.paste(min_image, (x, y))

x, y = 430, 0
draw.text((x+10, y+285), "Max", font=font, fill=0)
output_image.paste(max_image, (x, y))

x, y = 860, 0
draw.text((x+10, y+285), "Median", font=font, fill=0)
output_image.paste(median_image, (x, y))

x, y = 0, 320
draw.text((x+10, y+285), "Mode", font=font, fill=0)
output_image.paste(mode_image, (x, y))

x, y = 430, 320
draw.text((x+10, y+285), "Rank 10", font=font, fill=0)
output_image.paste(rank_image, (x, y))

output_image.save('imagefilter-rank.jpg')
