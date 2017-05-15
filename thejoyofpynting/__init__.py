#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import urllib.request

from PIL import Image

__title__ = "thejoyofpynting"

__author__ = "DeflatedPickle/Dibbo"
__copyright__ = "Copyright (c) 2017 Dibbo"
__credits__ = ["DeflatedPickle/Dibbo"]

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "DeflatedPickle/Dibbo"
__email__ = "DeflatedPickle@gmail.com"
__status__ = "Development"

bob_types = {
    0: {
        "image": urllib.request.urlopen(urllib.request.Request("http://i.imgur.com/nVMsfWs.png")),
        "place_x": 20,
        "place_y": 60
    }
}


def paint_a_picture(file: str="", bobtype: int=0):
    image = Image.open(file)
    image = image.convert("RGBA")
    image = image.resize((360, 280))

    bob = Image.open(bob_types[bobtype]["image"])
    bob = bob.convert("RGBA")

    final = Image.new("RGBA", bob.size)
    final.paste(image, (bob_types[bobtype]["place_x"], bob_types[bobtype]["place_y"]), image)
    final.paste(bob, (0, 0), bob)
    # final = Image.alpha_composite(final, image)
    # final = Image.alpha_composite(final, bob)

    # final.show()
    return final
