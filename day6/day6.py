
def total_number_of_orbits(input):
    return 1


def split_into_orbit_pairs(input):
    input.replace(" ", "")
    input.replace("\t", "")
    pairs = input.split('\n')
    pairs = list(map(str.strip, pairs))
    for orbit in pairs:
        print(".", orbit, ",")
    print(pairs)
    return pairs
