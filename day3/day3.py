import math

grid_size = 20000


def manhattan_distance_of_closest_crossing(lines):
    grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    for line in lines:
        draw_line(grid, line, 1, 1)

    # print(grid)
    return find_closest_crossing(grid)


def find_closest_crossing(grid):
    crossings = all_crossing_distances(grid)
    print(crossings)
    return min(crossings)


def all_crossing_distances(grid):
    crossing_distances = []
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            if (grid[x][y] >= 2):
                print(x, y)
                crossing_distances.append(x + y - 2)
    return crossing_distances


def draw_line(grid, line, prev_x, prev_y):
    coordinates = (1, 1)
    for step in line:
        coordinates = draw_step(grid, step, coordinates[0], coordinates[1])


def draw_step(grid, step, start_x, start_y):
    direction = step[:1]
    distance = int(step[1:])
    if (direction == "U"):
        r = range(start_y + 1, start_y + distance)
        for y in r:
            grid[start_x][y] += 1
        return (start_x, start_y + distance)
    elif (direction == "D"):
        r = range(start_y - distance, start_y - 1)
        for y in r:
            grid[start_x][y] += 1
        return (start_x, start_y - distance)
    elif (direction == "R"):
        r = range(start_x + 1, start_x + distance)
        for x in r:
            grid[x][start_y] += 1
        return (start_x + distance, start_y)
    elif (direction == "L"):
        r = range(start_x - distance, start_x - 1)
        for x in r:
            grid[x][start_y] += 1
        return (start_x - distance, start_y)
    else:
        raise RuntimeError('Unknown direction code', direction)


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
    # content_as_int = list(map(int, split_contents))
    return split_contents


def main():
    lines = read_input_file('day3/input.txt')
    answer = manhattan_distance_of_closest_crossing(lines)
    print("Closest crossing", answer)


main()
