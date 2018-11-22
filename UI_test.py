import math
from Values import Values
from Uncertainties import *
from Parser import *
from Main import *

m_metal = "Values(5.56, 0.005)"
m_water = "Values(100, 0.5)"

percent_mass_metal = mass_washer.relative_unc

# Trial 1

percent_q_metal_1 = q_water_1.relative_unc
percent_t_metal_1 = delta_t_washer_1.relative_unc

percent_c_metal_1 = percent_q_metal_1 + percent_mass_metal + percent_t_metal_1

# Trial 2

percent_q_metal_2 = q_water_2.relative_unc
percent_t_metal_2 = delta_t_washer_2.relative_unc

percent_c_metal_2 = percent_q_metal_2 + percent_mass_metal + percent_t_metal_2

print("first trial: " + str(percent_c_metal_1))
print("second trial: " + str(percent_c_metal_2))

print("average: " + str((percent_c_metal_1 + percent_c_metal_2)/2))

print(c_washer_avg.absolute_unc)
