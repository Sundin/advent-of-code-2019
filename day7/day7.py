from intcode_computer import *
import itertools


def find_max_thruster_signal(program):
    max_signal = 0
    for setting in itertools.permutations([0, 1, 2, 3, 4]):
        signal = try_phase_setting_sequence(program, setting, 0)
        max_signal = max(max_signal, signal)
    return max_signal


def find_max_thruster_signal_with_feedback(program):
    # max_signal = 0
    # for setting in itertools.permutations([5, 6, 7, 8, 9]):
    #     signal = try_phase_setting_sequence_with_feedback(program, setting, 0)
    #     max_signal = max(max_signal, signal)
    # return max_signal
    return try_phase_setting_sequence_with_feedback(program, [9, 8, 7, 6, 5], 0)


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
    print("Running setting", phase_settings)
    amp_a = program.copy()
    amp_b = program.copy()
    amp_c = program.copy()
    amp_d = program.copy()
    amp_e = program.copy()

    pointer_a = 0
    pointer_b = 0
    pointer_c = 0
    pointer_d = 0
    pointer_e = 0

    in_values = [start_value]

    # print("###############################################")
    # print("Phase settings:", phase_settings)
    # print("###############################################")

    for i in range(0, 50):
        # print("RUNNING A")
        a_res = run_program(amp_a, 0, [
                            phase_settings[0]] + in_values, [])
        amp_a = a_res[0]
        a_out = a_res[1]
        if a_res[2] == "DONE":
            pointer_a = 0
        else:
            pointer_a = a_res[2]

        # print("RUNNING B")
        b_res = run_program(amp_b, 0, [phase_settings[1]] + a_out, [])
        amp_b = b_res[0]
        b_out = b_res[1]
        if b_res[2] == "DONE":
            pointer_b = 0
        else:
            pointer_b = b_res[2]

        # print("RUNNING C")
        c_res = run_program(amp_c, 0, [phase_settings[2]] + b_out, [])
        amp_c = c_res[0]
        c_out = c_res[1]
        if c_res[2] == "DONE":
            pointer_c = 0
        else:
            pointer_c = c_res[2]

        # print("RUNNING D")
        d_res = run_program(amp_d, 0, [phase_settings[3]] + c_out, [])
        amp_d = d_res[0]
        d_out = d_res[1]
        if d_res[2] == "DONE":
            pointer_d = 0
        else:
            pointer_d = d_res[2]

        # print("RUNNING E")
        e_res = run_program(amp_e, 0, [phase_settings[4]] + d_out, [])
        amp_e = e_res[0]
        e_out = e_res[1]
        if e_res[2] == "DONE":
            pointer_e = 0
        else:
            pointer_e = e_res[2]

        # if pointer_e == "DONE":
        #     print("DONE", e_out)
        #     return e_out
        print("Looped and got", e_out)
        in_values = e_out

    print("You need a longer loop man")
    return e_out[-1]


def main():
    program = read_input_file('day7/input.txt')
    output1 = find_max_thruster_signal(program)
    print(output1)


main()
