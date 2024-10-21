from wand.image import Image
from collections import Counter


def get_colors(image_path, num_colors):
    with Image(filename=image_path) as img:
        img.resize(100, 100)

        img.quantize(number_colors=num_colors)

        colors = img.make_blob(format='RGB')

        color_list = [colors[i:i + 3] for i in range(0, len(colors), 3)]

        color_counts = Counter(color_list)

        most_common_colors = color_counts.most_common(num_colors)

        hex_colors = ['#{:02x}{:02x}{:02x}'.format(
            color[0][0], color[0][1], color[0][2]) for color in most_common_colors]
    return hex_colors
