import math

def get_all_asteroids(map):
    asteroids = []

    map = map.strip()
    rows = map.split('\n')
    for y, row in enumerate(rows):
        row = row.strip()
        for x, col in enumerate(row):
            if col == "#":
                asteroids.append((x, y))
    return asteroids

def number_of_asteroids(map):
    asteroids = get_all_asteroids(map)
    return len(asteroids)

def count_asteroids_in_sight(map, coordinates):
    return 1

def has_line_of_sight(map, a, b):
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    asteroids = get_all_asteroids(map)

    if x_diff == 0:
        x = a[0]
        left_y = min(a[1], b[1])
        for y in range(left_y + 1, left_y + y_diff):
            if (x, y) in asteroids:
                return False

    if y_diff == 0:
        y = a[1]
        left_x = min(a[0], b[0])
        for x in range(left_x + 1, left_x + x_diff):
            if (x, y) in asteroids:
                return False

    if x_diff == y_diff:
        left_x = min(a[0], b[0])
        left_y = min(a[1], b[1])
        for x in range(left_x + 1, left_x + x_diff):
            print(x)
            for y in range(left_y + 1, left_y + y_diff):
                print(x, y)
                if (x, y) in asteroids:
                    return False
                    
    return True