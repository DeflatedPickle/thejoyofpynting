#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import urllib.request

from PIL import Image
import thejoyofpynting

image_location = urllib.request.urlopen(urllib.request.Request("https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg"))
local_image_location = ""

image1 = thejoyofpynting.paint_a_picture(image_location, 0)
# Image.Image.show(image1)
image1.save("1-edit.png")

image2 = thejoyofpynting.paint_a_picture(image_location, 1)
# Image.Image.show(image2)
image2.save("2-edit.png")

image3 = thejoyofpynting.paint_a_picture(image_location, 2)
# Image.Image.show(image3)
image3.save("3-edit.png")
