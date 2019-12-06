from day6 import *
import unittest


def test_split_into_orbit_pairs():
    assert split_into_orbit_pairs(
        """COM)A
        COM)B"""
    ) == ["COM)A", "COM)B"]


def test_total_number_of_orbits():
    assert total_number_of_orbits("COM)A") == 1
    # assert total_number_of_orbits(
    #     """COM)A
    #     COM)B"""
    # ) == 2
