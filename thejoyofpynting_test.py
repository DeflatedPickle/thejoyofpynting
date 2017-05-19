#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from PIL import Image
import thejoyofpynting

local_image_location = ".png"  # Provide a local image

image1 = thejoyofpynting.paint_a_picture(local_image_location, 0)
Image.Image.show(image1)
# image1.save("1-edit.png")

image2 = thejoyofpynting.paint_a_picture(local_image_location, 1)
Image.Image.show(image2)
# image2.save("2-edit.png")

image3 = thejoyofpynting.paint_a_picture(local_image_location, 2)
Image.Image.show(image3)
# image3.save("3-edit.png")

image4 = thejoyofpynting.paint_a_picture(local_image_location, 3)
Image.Image.show(image4)
# image4.save("4-edit.png")

image5 = thejoyofpynting.paint_a_picture(local_image_location, 4)
Image.Image.show(image5)
# image5.save("5-edit.png")

image6 = thejoyofpynting.paint_a_picture(local_image_location, 5)
Image.Image.show(image6)
# image6.save("6-edit.png")
