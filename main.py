#!python3

import os
from PIL import Image, ImageDraw


def addOverlay(image_path, overlay_path, border_percent=1, overlay_percent=15):
    img = Image.open(image_path)
    size = min(img.size)

    border_size = int(size * border_percent / 100)

    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, size, border_size), fill='red')
    draw.rectangle((0, 0, border_size, size), fill='red')
    draw.rectangle((size - border_size, 0, size, size), fill='red')
    draw.rectangle((0, size - border_size, size, size), fill='red')

    overlay = Image.open(overlay_path)
    overlay_size = int(size * overlay_percent / 100)
    overlay = overlay.resize((overlay_size, overlay_size))

    x = size - overlay_size
    y = size - overlay_size

    img.paste(overlay, (x, y), overlay)

    img.save(os.path.splitext(image_path)[0] + '_ovd' + os.path.splitext(image_path)[1])


for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        addOverlay(filename, 'assets/leCoin.png', 1, 15)

