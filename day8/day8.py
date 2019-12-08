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


main()
