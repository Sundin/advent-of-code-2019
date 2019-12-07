from intcode_computer import *
import itertools


def find_max_thruster_signal(program):
    max_signal = 0
    for setting in itertools.permutations([0, 1, 2, 3, 4]):
        signal = try_phase_setting_sequence(program, setting)
        max_signal = max(max_signal, signal)
    return max_signal


def try_phase_setting_sequence(program, phase_settings):
    memory = program.copy()
    a_out = get_intcode_computer_ouput(memory, [phase_settings[0], 0])[0]

    memory = program.copy()
    b_out = get_intcode_computer_ouput(memory, [phase_settings[1], a_out])[0]

    memory = program.copy()
    c_out = get_intcode_computer_ouput(memory, [phase_settings[2], b_out])[0]

    memory = program.copy()
    d_out = get_intcode_computer_ouput(memory, [phase_settings[3], c_out])[0]

    memory = program.copy()
    e_out = get_intcode_computer_ouput(memory, [phase_settings[4], d_out])[0]

    return e_out


def main():
    program = read_input_file('day7/input.txt')
    output1 = find_max_thruster_signal(program)
    print(output1)


main()
