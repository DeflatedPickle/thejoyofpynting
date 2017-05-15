#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import urllib.request

from PIL import Image
import thejoyofpynting

image_location = urllib.request.urlopen(urllib.request.Request("https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg"))

# image = thejoyofpynting.paint_a_picture(image_location)
# image = thejoyofpynting.paint_a_picture(image_location, 1)
image = thejoyofpynting.paint_a_picture(image_location, 2)
Image.Image.show(image)
