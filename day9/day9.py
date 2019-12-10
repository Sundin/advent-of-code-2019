from intc_comp import *
import sys


def main():
    program = read_input_file('day9/input.txt')
    output1 = get_intcode_computer_ouput(program, [1])
    print("Answer1:", output1)

    program = read_input_file('day9/input.txt')
    sys.setrecursionlimit(32000)
    output2 = get_intcode_computer_ouput(program, [2])
    print("Answer1:", output2)


main()
