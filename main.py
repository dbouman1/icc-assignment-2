"""

"""
## Import modules
import simulation               # simulation module
import numpy as np
import save_data as save
import os
import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values

np.seterr(divide='ignore', invalid='ignore')

# Simulation
minBeads, maxBeads, plot_data = simulation.user_input()  # User input for simualation variables

# Check if multiple polymer lengths are simulated
if (minBeads+1) == maxBeads:
    write_mode="w"
    multi = False
else:             
    # os.remove("R_squared.dat")
    write_mode="a"
    multi = True

# for iii in range(minBeads, maxBeads):
existingPos = simulation.simulation(multi,write_mode)

if plot_data == 'y':                                            # Plot when chosen
    simulation.plot(existingPos)