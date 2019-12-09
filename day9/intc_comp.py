
def run_intcode_computer(program, input):
    return run_program(program, 0, input, [])


def get_intcode_computer_ouput(program, input):
    result = run_program(program, 0, input, [])
    return result[1]


def get_intcode_computer_finished_program(program, input):
    result = run_program(program, 0, input, [])
    return result[0]


def run_program(program, pointer, input, output):
    return run_program_with_relative_base(program, pointer, 0, input, output)


def get_final_relative_base(program):
    return run_program(program, 0, [], [])[3]


def run_program_with_relative_base(program, pointer, relative_base, input, output):
    # Returns (program, output, current_pointer/"DONE", relative_base)
    action = get_action_code(program[pointer])
    parameter_modes = get_parameter_modes(program[pointer])

    ### Addition ###
    if action == 1:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1),
        #       get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1], relative_base)
        parameter3 = get_as_value(program, pointer+3)

        write_value(program, parameter3, parameter1 + parameter2)
        return run_program_with_relative_base(program, pointer+4, relative_base, input, output)

    ### Multiplication ###
    elif action == 2:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1], relative_base)
        parameter3 = get_as_value(program, pointer+3)

        write_value(program, parameter3, parameter1 * parameter2)
        return run_program_with_relative_base(program, pointer+4, relative_base, input, output)

    ### Input ###
    elif action == 3:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1))
        # if len(input) == 0:
        #     print("HALTING AT", pointer)
        #     return (program, output, pointer)

        address = get_for_writing(
            program, pointer+1, parameter_modes[2], relative_base)
        write_value(program, address, input.pop(0))
        return run_program_with_relative_base(program, pointer+2, relative_base, input, output)

    ### Output ###
    elif action == 4:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        output.append(parameter1)
        return run_program_with_relative_base(program, pointer+2, relative_base, input, output)

    ### Jump if not 0 ###
    elif action == 5:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1], relative_base)
        if parameter1 != 0:
            return run_program_with_relative_base(program, parameter2, relative_base, input, output)
        return run_program_with_relative_base(program, pointer+3, relative_base, input, output)

    ### Jump if 0 ###
    elif action == 6:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1], relative_base)
        if parameter1 == 0:
            return run_program_with_relative_base(program, parameter2, relative_base, input, output)
        return run_program_with_relative_base(program, pointer+3, relative_base, input, output)

    ### Less than ###
    elif action == 7:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1], relative_base)
        parameter3 = get_as_value(program, pointer+3)
        if parameter1 < parameter2:
            write_value(program, parameter3, 1)
        else:
            write_value(program, parameter3, 0)
        if pointer == parameter3:
            run_program_with_relative_base(
                program, pointer, relative_base, input, output)
        return run_program_with_relative_base(program, pointer+4, relative_base, input, output)

    ### Equals ###
    elif action == 8:
        # print(get_as_value(program, pointer), get_as_value(program, pointer+1), get_as_value(program, pointer+2), get_as_value(program, pointer+3))
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        parameter2 = get_as_value_or_pointer(
            program, pointer+2, parameter_modes[1], relative_base)
        parameter3 = get_as_value(program, pointer+3)
        if parameter1 == parameter2:
            write_value(program, parameter3, 1)
        else:
            write_value(program, parameter3, 0)
        if pointer == parameter3:
            run_program_with_relative_base(
                program, pointer, relative_base, input, output)
        return run_program_with_relative_base(program, pointer+4, relative_base, input, output)

    # Adjust relative_base
    elif action == 9:
        parameter1 = get_as_value_or_pointer(
            program, pointer+1, parameter_modes[2], relative_base)
        return run_program_with_relative_base(program, pointer+2, relative_base+parameter1, input, output)

        ### Exit ###
    elif action == 99:
        return (program, output, "DONE", relative_base)
    else:
        raise RuntimeError('Unknown action code', action)
    raise RuntimeError('Out of bounds')


def get_for_writing(program, pointer, mode, relative_base):
    if mode == 0:
        return get_as_value(program, pointer)
    elif mode == 1:
        raise RuntimeError("not implemented", mode)
    elif mode == 2:
        return get_as_value(program, pointer+1) + relative_base
        # return get_as_relative_base(program, pointer, relative_base)
    else:
        raise RuntimeError('Unknown parameter mode', mode)


def get_as_value_or_pointer(program, pointer, mode, relative_base):
    if mode == 0:
        return get_as_pointer(program, pointer)
    elif mode == 1:
        return get_as_value(program, pointer)
    elif mode == 2:
        return get_as_relative_base(program, pointer, relative_base)
    else:
        raise RuntimeError('Unknown parameter mode', mode)


def get_action_code(opcode):
    if opcode < 10:
        return opcode
    digits = split_into_digits(opcode)
    return digits[-2] * 10 + digits[-1]


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
    pointer = program[address]
    return get_as_value(program, pointer)


def write_value(program, address, value):
    potentially_increase_memory(program, address)
    program[address] = value


def get_as_value(program, address):
    potentially_increase_memory(program, address)
    return program[address]


def potentially_increase_memory(program, address):
    if address >= len(program):
        n = address - len(program) + 1
        listofzeros = [0] * n
        program += listofzeros


def get_as_relative_base(program, address, relative_base):
    return program[program[address] + relative_base]


def read_input_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        split_contents = file_contents.split(',')
        content_as_int = list(map(int, split_contents))
        return content_as_int
