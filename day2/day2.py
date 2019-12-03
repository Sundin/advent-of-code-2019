# Day 2 - part 1
def run_intcode_computer(program):
  return run_program(program, 0)

# Day 2 - part 2
def find_input_brute_force(program, output):
  for noun in range(0, 99):
    for verb in range(0, 99):
      memory = program.copy()
      memory[1] = noun
      memory[2] = verb
      memory = run_program(memory, 0)
      if memory[0] == output:
        return memory
  return "No solution found"

def run_program(program, pointer):
  action = program[pointer]
  if action == 1:
    program[get_value(program, pointer+3)] = get_value_of_pointer(program, pointer+1) + get_value_of_pointer(program, pointer+2)
    return run_program(program, pointer+4)
  elif action == 2:
    program[get_value(program, pointer+3)] = get_value_of_pointer(program, pointer+1) * get_value_of_pointer(program, pointer+2)
    return run_program(program, pointer+4)
  elif action == 99:
    return program
  else:
    raise RuntimeError('Unknown action code', action)

def get_value_of_pointer(program, address):
  return program[program[address]]

def get_value(program, address):
  return program[address]

def read_input_file(file_path):
  with open(file_path) as file:
    file_contents = file.read()
    split_contents =  file_contents.split(',')
    content_as_int = list(map(int, split_contents)) 
    return content_as_int

def main():
  program = read_input_file('day2/input.txt')
  computer = find_input_brute_force(program, 19690720)
  print(computer)

main()
