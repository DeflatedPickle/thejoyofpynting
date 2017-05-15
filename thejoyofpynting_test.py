#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import urllib.request

from PIL import Image
import thejoyofpynting

# image = thejoyofpynting.paint_a_picture(urllib.request.urlopen(urllib.request.Request("https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg")))
image = thejoyofpynting.paint_a_picture(urllib.request.urlopen(urllib.request.Request("https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg")), 1)
Image.Image.show(image)
