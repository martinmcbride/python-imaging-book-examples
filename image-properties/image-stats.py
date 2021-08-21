# Author:  Martin McBride
# Created: 2021-08-21
# Copyright (C) 2021, Martin McBride
# License: MIT

# Print the statistics of an image
# matplotlib is only used to plot the histogram, comment it out of you don't want to use it.

from PIL import Image, ImageStat
import matplotlib.pyplot as plot

jpeg_image = Image.open('boat.jpg')

## Histogram
histogram = jpeg_image.histogram()
print("Histogram length:", len(histogram))  # 768
print("Histogram:", histogram[:256])        # [0, 0, 2, ... 1057]
print("Histogram:", histogram[256:512])     # [5, 2, 3, ... 91]
print("Histogram:", histogram[512:])        # [45, 12, 8, ... 129]

greyscale_image = jpeg_image.convert('L')
histogram = greyscale_image.histogram()
print("Histogram length:", len(histogram))  # 256
print("Histogram:", histogram)              # [0, 0, 0, ... 41]

plot.plot(histogram)
plot.savefig("histogram.png")

## Other image stats
print("Extrema:", jpeg_image.getextrema())  # ((2, 255), (0, 255), (0, 255))
print("Entropy:", jpeg_image.entropy())     # 9.21637999047619

## ImageStat module

stat = ImageStat.Stat(jpeg_image)
print("stat.extrema", stat.extrema) # [(2, 255), (0, 255), (0, 255)]
print("stat.count", stat.count)     # [240000, 240000, 240000]
print("stat.sum", stat.sum)         # [34365232.0, 34592832.0, 33760460.0]
print("stat.sum2", stat.sum2)       # [5623187660.0, 5659892442.0, 5688740626.0]
print("stat.mean", stat.mean)       # [143.18846666666667, 144.1368, 140.66858333333334]
print("stat.median", stat.median)   # [145, 148, 144]
print("stat.rms", stat.rms)         # [153.0684441135185, 153.56720084379998, 153.95806552976256]
print("stat.var", stat.var)         # [2927.011596982221, 2807.468060760001, 3915.4356046597204]
print("stat.stddev", stat.stddev)   # [54.101863156292694, 52.98554577203109, 62.57344168782568]
