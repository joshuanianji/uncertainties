import math
from Values import Values
from Uncertainties import *


# Universal
mass_water = scale(Values(100, 0.5), 0.001)
mass_washer = scale(Values(5.56, 0.005), 0.001)

heat_capacity_water = Values(4200, 20)  # joules per kilogram celsius


# Energy absorbed by water (with uncertainties)

# trial 1
t_initial_water_1 = Values(21.7, 0.5)
t_final_water_1 = Values(22.5, 0.5)


delta_t_1 = subtract(t_final_water_1, t_initial_water_1)
# print("del t: " + delta_t_1.output_absolute())

mass_test = multiply(mass_water, heat_capacity_water)
# print("mc: " + mass_test.output_absolute())

q_water_1 = multiply(mass_test, delta_t_1)

print("Q1: " + q_water_1.output_absolute())


# trial 2
t_initial_water_2 = Values(22.5, 0.5)
t_final_water_2 = Values(23.1, 0.5)

delta_t_2 = subtract(t_final_water_2, t_initial_water_2)
# print("del t: " + delta_t_2.output_absolute())

mass_test = multiply(mass_water, heat_capacity_water)
# print("mc: " + mass_test.output_absolute())

q_water_2 = multiply(mass_test, delta_t_2)

print("Q2: " + q_water_2.output_absolute())


# HEAT CAPACITIES OF WASHER

# trial 1
delta_t_washer_1 = subtract(Values(100, 0.5), t_final_water_1)
c_washer_1 = divide(divide(q_water_1, mass_washer), delta_t_washer_1)
print("C of washer (trial 1): " + c_washer_1.output_absolute())

# trial 2
delta_t_washer_2 = subtract(Values(100, 0.5), t_final_water_2)
c_washer_2 = divide(divide(q_water_2, mass_washer), delta_t_washer_2)
print("C of washer (trial 2): " + c_washer_2.output_absolute())

# average
c_washer_avg = average(c_washer_1, c_washer_2)
print("percent error of c washer: " + c_washer_avg.output_relative())
print("average c of washer: " + c_washer_avg.output_absolute())
