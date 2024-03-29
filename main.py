from PIL import Image, ImageDraw


def add_border_and_overlay(image_path, overlay_path, border_percent=1, overlay_percent=15):
    img = Image.open(image_path)
    size = img.size[0]

    border_size = int(size * border_percent / 100)

    draw = ImageDraw.Draw(img)

    x1 = 0
    y1 = 0
    x2 = size
    y2 = size

    draw.rectangle((x1, y1, x2, y1 + border_size), fill='red')
    draw.rectangle((x1, y1, x1 + border_size, y2), fill='red')
    draw.rectangle((x2 - border_size, y1, x2, y2), fill='red')
    draw.rectangle((x1, y2 - border_size, x2, y2), fill='red')

    overlay = Image.open(overlay_path)
    overlay_size = int(size * overlay_percent / 100)
    overlay = overlay.resize((overlay_size, overlay_size))

    x = x2 - overlay_size
    y = y2 - overlay_size

    img.paste(overlay, (x, y), overlay)

    img.save('output.png')


add_border_and_overlay('blank1000.png', 'coin-signature.png', 1, 15)
