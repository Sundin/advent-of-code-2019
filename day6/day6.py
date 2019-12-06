
def total_number_of_orbits(input):
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
    return count_all_orbits(all_planets)

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

main()
