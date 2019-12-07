from intcode_computer import *
import itertools


def find_max_thruster_signal(program):
    max_signal = 0
    for setting in itertools.permutations([0, 1, 2, 3, 4]):
        signal = try_phase_setting_sequence(program, setting, 0)
        max_signal = max(max_signal, signal)
    return max_signal


def find_max_thruster_signal_with_feedback(program):
    max_signal = 0
    for setting in itertools.permutations([5, 6, 7, 8, 9]):
        signal = try_phase_setting_sequence_with_feedback(program, setting, 0)
        max_signal = max(max_signal, signal)
    return max_signal


def try_phase_setting_sequence(program, phase_settings, start_value):
    amp_a = program.copy()
    amp_b = program.copy()
    amp_c = program.copy()
    amp_d = program.copy()
    amp_e = program.copy()

    a_out = get_intcode_computer_ouput(
        amp_a, [phase_settings[0], start_value])[0]

    b_out = get_intcode_computer_ouput(
        amp_b, [phase_settings[1], a_out])[0]

    c_out = get_intcode_computer_ouput(
        amp_c, [phase_settings[2], b_out])[0]

    d_out = get_intcode_computer_ouput(
        amp_d, [phase_settings[3], c_out])[0]

    e_out = get_intcode_computer_ouput(
        amp_e, [phase_settings[4], d_out])[0]

    return e_out


def try_phase_setting_sequence_with_feedback(program, phase_settings, start_value):
    amp_a = program.copy()
    amp_b = program.copy()
    amp_c = program.copy()
    amp_d = program.copy()
    amp_e = program.copy()

    in_value = start_value

    # print("###############################################")
    # print("Phase settings:", phase_settings)
    # print("###############################################")

    # for i in range(0, 10):
    a_out = get_intcode_computer_ouput(
        amp_a, [phase_settings[0], in_value])[0]

    b_out = get_intcode_computer_ouput(
        amp_b, [phase_settings[1], a_out])[0]

    c_out = get_intcode_computer_ouput(
        amp_c, [phase_settings[2], b_out])[0]

    d_out = get_intcode_computer_ouput(
        amp_d, [phase_settings[3], c_out])[0]

    e_out = get_intcode_computer_ouput(
        amp_e, [phase_settings[4], d_out])[0]

    print(e_out)
    in_value = e_out

    return e_out


def main():
    program = read_input_file('day7/input.txt')
    output1 = find_max_thruster_signal(program)
    print(output1)


main()
