from intc_comp import *
import unittest


def test_run_intcode_computer_basic_op_codes():
    assert get_intcode_computer_finished_program(
        [1, 0, 0, 0, 99], []) == [2, 0, 0, 0, 99]
    assert get_intcode_computer_finished_program(
        [2, 3, 0, 3, 99], []) == [2, 3, 0, 6, 99]
    assert get_intcode_computer_finished_program([2, 4, 4, 5, 99, 0], []) == [
        2, 4, 4, 5, 99, 9801]
    assert get_intcode_computer_finished_program([1, 1, 1, 4, 99, 5, 6, 0, 99], []) == [
        30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert get_intcode_computer_finished_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], []) == [
        3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_run_intcode_computer_opcodes_3_4():
    assert get_intcode_computer_ouput([3, 0, 4, 0, 99], [1]) == [1]
    assert get_intcode_computer_ouput([3, 0, 4, 0, 99], [666]) == [666]


def test_action_code_99():
    assert get_intcode_computer_finished_program(
        [1, 0, 0, 0, 99], []) == [2, 0, 0, 0, 99]


def test_run_intcode_computer_opcode_8():
    assert get_intcode_computer_ouput(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8]) == [1]
    assert get_intcode_computer_ouput(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [9]) == [0]
    assert get_intcode_computer_ouput(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [7]) == [0]
    assert get_intcode_computer_ouput(
        [3, 3, 1108, -1, 8, 3, 4, 3, 99], [8]) == [1]
    assert get_intcode_computer_ouput(
        [3, 3, 1108, -1, 8, 3, 4, 3, 99], [9]) == [0]
    assert get_intcode_computer_ouput(
        [3, 3, 1108, -1, 8, 3, 4, 3, 99], [7]) == [0]


def test_run_intcode_computer_opcode_7():
    assert get_intcode_computer_ouput(
        [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8]) == [0]
    assert get_intcode_computer_ouput(
        [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [9]) == [0]
    assert get_intcode_computer_ouput(
        [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7]) == [1]
    assert get_intcode_computer_ouput(
        [3, 3, 1107, -1, 8, 3, 4, 3, 99], [8]) == [0]
    assert get_intcode_computer_ouput(
        [3, 3, 1107, -1, 8, 3, 4, 3, 99], [9]) == [0]
    assert get_intcode_computer_ouput(
        [3, 3, 1107, -1, 8, 3, 4, 3, 99], [7]) == [1]


def test_run_intcode_computer_opcodes_5_6():
    assert get_intcode_computer_ouput(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0]) == [0]
    assert get_intcode_computer_ouput(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [666]) == [1]
    assert get_intcode_computer_ouput(
        [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [0]) == [0]
    assert get_intcode_computer_ouput(
        [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [666]) == [1]


def test_advanced_opcodes():
    assert get_intcode_computer_ouput([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [8]) == [1000]
    assert get_intcode_computer_ouput([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [7]) == [999]
    assert get_intcode_computer_ouput([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                                       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                                       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [9]) == [1001]


def test_get_action_code():
    assert get_action_code(1102) == 2
    assert get_action_code(2) == 2
    assert get_action_code(99) == 99


def test_get_parameter_modes():
    assert get_parameter_modes(11002) == [1, 1, 0]
    assert get_parameter_modes(11102) == [1, 1, 1]
    assert get_parameter_modes(1102) == [0, 1, 1]
    assert get_parameter_modes(2) == [0, 0, 0]
    assert get_parameter_modes(102) == [0, 0, 1]


def test_relative_base():
    assert get_final_relative_base([1, 0, 0, 0, 99]) == 0
    assert get_final_relative_base([109, 100, 99]) == 100
    assert get_final_relative_base([109, -100, 99]) == -100

def test_day9_capabilities():
    assert get_intcode_computer_ouput([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], []) == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert get_intcode_computer_ouput([104,1125899906842624,99], []) == [1125899906842624]
    assert get_intcode_computer_ouput([1102,34915192,34915192,7,4,7,99,0], []) == [1219070632396864]