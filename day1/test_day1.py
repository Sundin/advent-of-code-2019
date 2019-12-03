from day1 import *
import unittest

def test_get_fuel_requirements_for_mass():
  assert get_fuel_requirements_for_mass(12) == 2
  assert get_fuel_requirements_for_mass(14) == 2
  assert get_fuel_requirements_for_mass(1969) == 654
  assert get_fuel_requirements_for_mass(100756) == 33583

def test_sum_fuel_requirements_for_all_modules_on_spacecraft():
  assert sum_fuel_requirements_for_all_modules_on_spacecraft([12, 14, 1969, 100756]) == 34241

def test_get_fuel_requirements_for_mass_recursive():
  assert get_fuel_requirements_for_mass_recursive(14) == 2
  assert get_fuel_requirements_for_mass_recursive(1969) == 966
  assert get_fuel_requirements_for_mass_recursive(100756) == 50346
