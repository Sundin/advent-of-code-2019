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
