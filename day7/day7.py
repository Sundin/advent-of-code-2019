from intcode_computer import *


def find_max_thruster_signal(program):
    max_signal = 0
    for a in range(0, 5):
        memory = program.copy()
        a_out = get_intcode_computer_ouput(memory, [a, 0])[0]
        for b in range(0, 5):
            memory = program.copy()
            b_out = get_intcode_computer_ouput(memory, [b, a_out])[0]
            for c in range(0, 5):
                memory = program.copy()
                c_out = get_intcode_computer_ouput(memory, [c, b_out])[0]
                for d in range(0, 5):
                    memory = program.copy()
                    d_out = get_intcode_computer_ouput(memory, [d, c_out])[0]
                    for e in range(0, 5):
                        memory = program.copy()
                        e_out = get_intcode_computer_ouput(
                            memory, [e, d_out])[0]
                        max_signal = max(max_signal, e_out)
    return max_signal


def main():
    program = read_input_file('day7/input.txt')
    output1 = get_intcode_computer_ouput(program, [1, 0])
    print(output1)


main()
