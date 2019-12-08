import math


def count_digits(data, digit):
    data_list = list(data)
    matching_digits = list(filter(lambda x: x == str(digit), data_list))
    return len(matching_digits)


def get_image_layers(data, width, height):
    layer_size = width * height
    layers = []
    while len(data) > 0:
        layer = data[0:layer_size]
        layers.append(layer)
        data = data[layer_size:]
    return layers


def get_pixel_in_position(data, width, height, position):
    layers = get_image_layers(data, width, height)
    pixels = []
    for layer in layers:
        pixels.append(layer[position])
    for pixel in pixels:
        if pixel != "2":
            return pixel
    return "2"


def read_input_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def main():
    input = read_input_file("day8/input.txt")
    layers = get_image_layers(input, 25, 6)

    min_number_of_0 = math.inf
    number_of_1 = 0
    number_of_2 = 0

    for layer in layers:
        number_of_0 = count_digits(layer, 0)
        if number_of_0 < min_number_of_0:
            min_number_of_0 = number_of_0
            number_of_1 = count_digits(layer, 1)
            number_of_2 = count_digits(layer, 2)

    print("Answer 1:", number_of_1 * number_of_2)

    for row in range(0, 6):
        row_pixels = ""
        for i in range(0, 25):
            pixel = get_pixel_in_position(input, 25, 6, i + (row * 25))
            if pixel == "0":
                row_pixels += " "
            elif pixel == "1":
                row_pixels += "¶"
        print(row_pixels)


main()
