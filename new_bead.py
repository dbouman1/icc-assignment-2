"""

"""

## Import libraries
import numpy as np
def positions(previous_beads_pos, angles):
    offset = 2*np.pi*(np.random.random())               # create random offset of each angle to avoid preferential angles
    angles = np.add(angles,offset)                      # add offset to all possible angles
    
    possible_beads_pos = np.zeros((len(angles),2),dtype=float)      # initialize the possible bead possitions, wrt the origin
    possible_rel_prev_beads_pos = np.zeros((len(angles),2),dtype=float) # initialize the possible bead positions, relative to the previous bead

    possible_rel_prev_beads_pos[:,0] = np.cos(angles)         # calcate x-position relative to previous point
    possible_rel_prev_beads_pos[:,1] = np.sin(angles)         # calcate y-position relative to previous point
    return previous_beads_pos[:] + possible_rel_prev_beads_pos[:,:], angles;
"""

"""
def roulette(energies,T,L):
    boltzmann_weights = np.exp(-np.divide(energies,T))   # unnormalized probabilities
    boltzmann_weights_sum = sum(boltzmann_weights)
    probabilities = np.divide(boltzmann_weights,boltzmann_weights_sum) # normalize probabilities by dividing by their sum
    cumsum_probabilities = np.cumsum(probabilities)
    print('Bead: '+str(L)+', probabilities:\n'+str(probabilities))
    print('Weights:\n'+str(boltzmann_weights))
    # Here the final position is selected with the roulette wheel algortim
    RNG = np.random.random()
    for ii in range(0, len(probabilities)):
        if cumsum_probabilities[ii] > RNG:
            print('Select: '+str(ii))
            break
    return ii,boltzmann_weights[ii];
