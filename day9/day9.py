from intc_comp import *


def main():
    program = read_input_file('day9/input.txt')
    output1 = get_intcode_computer_ouput(program, [1])
    print("Answer1:", output1)


main()
