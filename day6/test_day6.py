from day6 import *
import unittest


def test_split_into_orbit_pairs():
    assert split_into_orbit_pairs(
        """COM)A
        COM)B"""
    ) == ["COM)A", "COM)B"]


def test_split_into_planets():
    assert split_into_planets("A)B") == ["A", "B"]


def test_total_number_of_orbits():
    assert total_number_of_orbits("COM)A") == 1
    assert total_number_of_orbits(
        """COM)A
        COM)B"""
    ) == 2
    assert total_number_of_orbits(
        """COM)A
        A)B"""
    ) == 3
    assert total_number_of_orbits(
        """A)B
        COM)A"""
    ) == 3
    assert total_number_of_orbits("""COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L""") == 42

def test_count_orbits():
    com = Planet("COM")
    a = Planet("a")
    b = Planet("b")
    a.set_parent(com)
    b.set_parent(a)
    assert count_orbits(com) == 0
    assert count_orbits(a) == 1
    assert count_orbits(b) == 2

def test_is_ancestor_of():
    com = Planet("COM")
    a = Planet("a")
    b = Planet("b")
    a.set_parent(com)
    b.set_parent(a)
    assert is_ancestor_of(com, a) == True
    assert is_ancestor_of(com, b) == True
    assert is_ancestor_of(a, b) == True
    assert is_ancestor_of(b, a) == False

def test_steps_to_transfer_to_common_ancestor():
    input = """COM)B
                B)C
                C)D
                D)E
                E)F
                B)G
                G)H
                D)I
                E)J
                J)K
                K)L
                K)YOU
                I)SAN"""
    assert steps_to_transfer_to_common_ancestor(input, "YOU", "SAN") == 3

def test_orbital_transfer():
    input = """COM)B
                B)C
                C)D
                D)E
                E)F
                B)G
                G)H
                D)I
                E)J
                J)K
                K)L
                K)YOU
                I)SAN"""
    assert calculate_orbital_transfer_distance(input, "YOU", "SAN") == 4

def test_distance():
    com = Planet("COM")
    a = Planet("a")
    b = Planet("b")
    a.set_parent(com)
    b.set_parent(a)
    assert distance(com, a) == 1
    assert distance(com, b) == 2
