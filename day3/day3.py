import math

grid_size = 10000


def manhattan_distance_of_closest_crossing(lines):
    line1 = draw_line(lines[0])
    line2 = draw_line(lines[1])

    crossings = find_all_crossings(line1, line2)

    return find_closest_crossing(crossings)

def  find_all_crossings(line1, line2):
    return list(set(line1).intersection(line2))


def find_closest_crossing(crossings):
    distances = []
    for crossing in crossings:
        distance = get_manhattan_distance(crossing)
        distances.append(distance)
        print(crossing, distance)
    return min(distances)

def get_manhattan_distance(crossing):
    return abs(crossing[0]) + abs(crossing[1])


def draw_line(line):
    coordinates = []
    current_position = (0, 0)
    for step in line:
        step_coordinates = draw_step(step, current_position[0], current_position[1])
        current_position = step_coordinates[-1]
        coordinates += step_coordinates
    return coordinates


def draw_step(step, start_x, start_y):
    direction = step[:1]
    distance = int(step[1:])

    coordinates = []

    if (direction == "U"):
        r = range(start_y + 1, start_y + distance + 1)
        for y in r:
            coordinates.append((start_x, y))
    elif (direction == "D"):
        r = reversed(range(start_y - distance, start_y))
        for y in r:
            coordinates.append((start_x, y))
    elif (direction == "R"):
        r = range(start_x + 1, start_x + distance + 1)
        for x in r:
            coordinates.append((x, start_y))
    elif (direction == "L"):
        r = reversed(range(start_x - distance, start_x))
        for x in r:
            coordinates.append((x, start_y))
    else:
        raise RuntimeError('Unknown direction code', direction)

    return coordinates


def read_input_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        lines = file_contents.split('\n')
        return_data = []
        for line in lines:
            return_data.append(get_data_from_line(line))
        return return_data


def get_data_from_line(line):
    split_contents = line.split(',')
    return split_contents


def main():
    lines = read_input_file('day3/input.txt')
    answer = manhattan_distance_of_closest_crossing(lines)
    print("Closest crossing", answer)


main()
