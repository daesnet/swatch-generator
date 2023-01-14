import png


def create_swatch(hex_color=None, rgb_color=None, swatch_path='./swatches'):
    # Figure out our color and its name
    if hex_color is not None:
        rgb_color = hex_to_rgb(hex_color)
    else:
        hex_color = rgb_to_hex(rgb_color)

    # Loop through to create the needed array
    swatch_size = 100
    pixels = []
    for r in range(0, swatch_size):
        row = []
        for s in range(0, swatch_size):
            row.append(rgb_color[0])
            row.append(rgb_color[1])
            row.append(rgb_color[2])

        pixels.append(row)

    # Write the file
    with open(f'{swatch_path}/{hex_color}.png', 'wb') as file:
        writer = png.Writer(swatch_size, swatch_size, greyscale=False)
        writer.write(file, pixels)
        print(f'Wrote {hex_color} {rgb_color}')


def generate_all_swatches():
    red = 0
    green = 0
    blue = 0

    for r in range(red, 256):
        for g in range(green, 256):
            for b in range(blue, 129):
                create_swatch(rgb_color=(r, g, b))


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


if __name__ == '__main__':
    create_swatch()
    # generate_all_swatches()
