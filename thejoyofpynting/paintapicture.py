#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from io import BytesIO

from PIL import Image

from .bobtypes import bob_types


def paint_a_picture(file: BytesIO, bobtype: int = 0):
    image = Image.open(file)
    image = image.convert("RGBA")
    image = image.resize((bob_types[bobtype]["size_x"], bob_types[bobtype]["size_y"]))

    bob = Image.open(bob_types[bobtype]["image"])
    bob = bob.convert("RGBA")

    final = Image.new("RGBA", bob.size)
    final.paste(image, (bob_types[bobtype]["place_x"], bob_types[bobtype]["place_y"]), image)
    final.paste(bob, (0, 0), bob)

    # final.show()

    bio = BytesIO()
    final.save(bio, "PNG")

    return bio
