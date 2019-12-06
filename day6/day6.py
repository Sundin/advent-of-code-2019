
def total_number_of_orbits(input):
    orbital_map = get_orbital_map(input)
    return count_all_orbits(orbital_map)

def get_orbital_map(input):
    all_planets = {}
    orbit_pairs = split_into_orbit_pairs(input)
    for pair in orbit_pairs:
        planets = split_into_planets(pair)
        if planets[0] not in all_planets:
            all_planets[planets[0]] = Planet(planets[0])
        if planets[1] not in all_planets:
            all_planets[planets[1]] = Planet(planets[1])
        all_planets[planets[0]].add_child(all_planets[planets[1]])
        all_planets[planets[1]].set_parent(all_planets[planets[0]])
    return all_planets

def count_all_orbits(orbit_map):
    sum = 0
    for planet in orbit_map.values():
        sum += count_orbits(planet)
    return sum
        
def count_orbits(planet):
    if planet.parent == "":
        return 0
    return count_orbits(planet.parent) + 1    

def split_into_planets(orbit_pair):
    return orbit_pair.split(')')

def split_into_orbit_pairs(input):
    input.replace(" ", "")
    input.replace("\t", "")
    pairs = input.split('\n')
    pairs = list(map(str.strip, pairs))
    return pairs

def is_ancestor_of(ancestor, descendant):
    assert isinstance(ancestor, Planet)
    assert isinstance(descendant, Planet)
    if descendant.parent == "":
        return False
    elif descendant.parent == ancestor:
        return True
    return is_ancestor_of(ancestor, descendant.parent)

def steps_to_transfer_to_common_ancestor(input, startName, targetName):
    orbit_map = get_orbital_map(input)
    return steps_to_ancestor_helper(orbit_map, startName, targetName)

def steps_to_ancestor_helper(orbit_map, startName, targetName):
    start_parent = orbit_map[startName].parent
    if is_ancestor_of(start_parent, orbit_map[targetName]):
        return 0
    return 1 + steps_to_ancestor_helper(orbit_map, start_parent.name, targetName)

def distance(ancestor, descendant):
    if descendant == ancestor:
        return 0
    elif descendant.parent == ancestor:
        return 1
    return 1 + distance(ancestor, descendant.parent)

def get_common_ancestor(orbit_map, startName, targetName):
    start_parent = orbit_map[startName].parent
    if is_ancestor_of(start_parent, orbit_map[targetName]):
        assert isinstance(start_parent, Planet)
        return start_parent
    return get_common_ancestor(orbit_map, start_parent.name, targetName)

def calculate_orbital_transfer_distance(input, startName, targetName):
    orbit_map = get_orbital_map(input)
    common_ancestor = get_common_ancestor(orbit_map, startName, targetName)
    return distance(common_ancestor, orbit_map[startName]) + distance(common_ancestor, orbit_map[targetName]) - 2

class Planet(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = ""
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Planet)
        self.children.append(node)
    def set_parent(self, node):
        assert isinstance(node, Planet)
        self.parent = node

def read_input_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    input = read_input_file('day6/input.txt')
    orbits = total_number_of_orbits(input)
    print("Answer 1:", orbits)
    input = read_input_file('day6/input.txt')
    orbital_transfer_distance = calculate_orbital_transfer_distance(input, "YOU", "SAN")
    print("Answer 2:", orbital_transfer_distance)

main()
