
def run_intcode_computer(program, input):
    return run_program(program, 0, input, [])


def get_intcode_computer_ouput(program, input):
    result = run_program(program, 0, input, [])
    return result[1]


def get_intcode_computer_finished_program(program, input):
    result = run_program(program, 0, input, [])
    return result[0]


def run_program(program, pointer, input, output):
    action = get_action_code(program[pointer])
    parameter_modes = get_parameter_modes(program[pointer])

    if action == 1:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1])
        parameter3 = get_as_value(program, pointer+3)

        program[parameter3] = parameter1 + parameter2
        return run_program(program, pointer+4, input, output)
    elif action == 2:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1])
        parameter3 = get_as_value(program, pointer+3)

        program[parameter3] = parameter1 * parameter2
        return run_program(program, pointer+4, input, output)
    elif action == 3:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1))
        parameter1 = get_as_value(program, pointer+1)
        program[parameter1] = input.pop(0)
        return run_program(program, pointer+2, input, output)
    elif action == 4:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        output.append(parameter1)
        return run_program(program, pointer+2, input, output)
    elif action == 5:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1])
        if parameter1 != 0:
            return run_program(program, parameter2, input, output)
        return run_program(program, pointer+3, input, output)
    elif action == 6:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1])
        if parameter1 == 0:
            return run_program(program, parameter2, input, output)
        return run_program(program, pointer+3, input, output)
    elif action == 7:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1])
        parameter3 = get_as_value(program, pointer+3)
        if parameter1 < parameter2:
            program[parameter3] = 1
        else:
            program[parameter3] = 0
        if pointer == parameter3:
            run_program(program, pointer, input, output)
        return run_program(program, pointer+4, input, output)
    elif action == 8:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2])
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1])
        parameter3 = get_as_value(program, pointer+3)
        if parameter1 == parameter2:
            program[parameter3] = 1
        else:
            program[parameter3] = 0
        if pointer == parameter3:
            run_program(program, pointer, input, output)
        return run_program(program, pointer+4, input, output)
    elif action == 9:  # should be 99
        # print("99")
        return (program, output)
    else:
        raise RuntimeError('Unknown action code', action)
    print(program[6])


def get_as_value_or_pointer(program, pointer, mode):
    if mode == 0:
        return get_as_pointer(program, pointer)
    elif mode == 1:
        return get_as_value(program, pointer)
    else:
        raise RuntimeError('Unknown parameter mode', mode)


def get_action_code(opcode):
    digits = split_into_digits(opcode)
    # should be 2 digits
    return digits[-1]


def get_parameter_modes(opcode):
    # 0: position_mode - get_as_pointer - default
    # 1: immediate_mode - get_as_value
    digits = split_into_digits(opcode)
    try:
        del digits[-1]
        del digits[-1]
    except IndexError:
        # ignore error, will pad with 0s later
        pass

    parameter_modes = [0, 0, 0]
    number_of_digits = len(digits)
    diff = len(parameter_modes) - number_of_digits
    for i in reversed(range(0, number_of_digits)):
        parameter_modes[i+diff] = digits[i]
    return parameter_modes


def split_into_digits(number):
    digits = []
    while number:
        digit = number % 10
        digits.append(digit)
        number //= 10
    digits.reverse()
    return digits


def get_as_pointer(program, address):
    return program[program[address]]


def get_as_value(program, address):
    return program[address]


def read_input_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        split_contents = file_contents.split(',')
        content_as_int = list(map(int, split_contents))
        return content_as_int
