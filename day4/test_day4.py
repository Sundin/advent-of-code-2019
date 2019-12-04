from day4 import *
import unittest


def test_is_matching():
    assert is_matching([1, 1, 1, 1, 1, 1]) == True
    assert is_matching([2, 2, 3, 4, 5, 0]) == False
    assert is_matching([1, 2, 3, 7, 8, 9]) == False


def test_is_matching_strict():
    # assert is_matching_strict([1, 1, 1, 1, 1, 1]) == False
    # assert is_matching_strict([2, 2, 3, 4, 5, 0]) == False
    # assert is_matching_strict([1, 2, 3, 7, 8, 9]) == False
    # assert is_matching_strict([1, 1, 2, 2, 3, 3]) == True
    # assert is_matching_strict([1, 2, 3, 4, 4, 4]) == False
    # assert is_matching_strict([1, 1, 1, 1, 2, 2]) == True
    assert is_matching_strict([2, 2, 1, 1, 1, 1]) == True


def test_split_into_digits():
    assert split_into_digits(123456) == [1, 2, 3, 4, 5, 6]
