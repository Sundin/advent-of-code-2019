from intc_comp import *
import sys


def main():
    program = read_input_file('day9/input.txt')
    output1 = get_intcode_computer_ouput(program, [1])
    print("Answer1:", output1)

    program2 = read_input_file('day9/input.txt')
    output2 = get_intcode_computer_ouput(program2, [2])
    print("Answer2:", output2)


main()
