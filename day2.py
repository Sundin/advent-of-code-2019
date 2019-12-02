def run_intcode_computer(program):
  return run_program(program, 0)

def run_program(program, current_step):
  action = program[current_step]
  if action == 1:
    program[get_value(program, current_step+3)] = get_value_of_pointer(program, current_step+1) + get_value_of_pointer(program, current_step+2)
    return run_program(program, current_step+4)
  elif action == 2:
    program[get_value(program, current_step+3)] = get_value_of_pointer(program, current_step+1) * get_value_of_pointer(program, current_step+2)
    return run_program(program, current_step+4)
  elif action == 99:
    return program
  else:
    raise RuntimeError('Unknown action code')

def get_value_of_pointer(program, position):
  return program[program[position]]

def get_value(program, position):
  return program[position]

def read_input_file(file_path):
  with open(file_path) as file:
    file_contents = file.read()
    split_contents =  file_contents.split(',')
    content_as_int = list(map(int, split_contents)) 
    return content_as_int

def main():
  program = read_input_file('input/day2.txt')
  computer = run_intcode_computer(program)
  print(computer)

main()
