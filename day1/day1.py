import math

# Day 1 - Part 1
def sum_fuel_requirements_for_all_modules_on_spacecraft(modules):
  total_fuel = 0
  for module in modules:
    total_fuel += get_fuel_requirements_for_mass(module)
  return total_fuel

# Day 1 - Part 2
def sum_fuel_requirements_for_all_modules_on_spacecraft_recursive(modules):
  total_fuel = 0
  for module in modules:
    total_fuel += get_fuel_requirements_for_mass_recursive(module)
  return total_fuel

def get_fuel_requirements_for_mass(mass):
  floor = math.floor(mass / 3)
  fuel_req = floor - 2
  return fuel_req

def get_fuel_requirements_for_mass_recursive(mass):
  fuel_req = get_fuel_requirements_for_mass(mass)
  if fuel_req <= 0:
    return 0

  return fuel_req + get_fuel_requirements_for_mass_recursive(fuel_req)

def read_input_file(file_path):
  with open(file_path) as file:
    file_contents = file.read()
    return file_contents.split('\n')

def main():
  modules = read_input_file('day1/input.txt')
  modules_as_int = list(map(int, modules)) 
  fuel_req = sum_fuel_requirements_for_all_modules_on_spacecraft_recursive(modules_as_int)
  print(fuel_req)
  
main()
