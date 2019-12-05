from day5 import *
import unittest


# def test_run_intcode_computer_basic_op_codes():
# assert run_intcode_computer([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
# assert run_intcode_computer([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
# assert run_intcode_computer([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
# assert run_intcode_computer([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
#     30, 1, 1, 4, 2, 5, 6, 0, 99]
# assert run_intcode_computer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [
#     3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_run_intcode_computer_new_op_codes():
    assert get_intcode_computer_ouput([3, 0, 4, 0, 99], [1]) == [1]


def test_get_action_code():
    assert get_action_code(1102) == 2


def test_get_parameter_modes():
    assert get_parameter_modes(11002) == [1, 1, 0]
    assert get_parameter_modes(11102) == [1, 1, 1]
    assert get_parameter_modes(1102) == [0, 1, 1]
