import numpy as np
import Simulation

def __init__(self, id):
    id = np.ushort(id)
    # Surroundings hold the likeliness for the ant to go a certain direction.
    likelinessInput = np.zeros((2,3), dtype=np.single) # TODO: change to 2x3 matrix
    
    # TODO: Function to update the likelinessInput and send to Simulation for the instance


# Function for fetching data
def getSurroundings():
    allSurroundings = Simulation.getSegment()
    # TODO: Trim down surroundings to fit the 2x3
    # return trimmedSurroundings


## Properties for determining likeliness
    
# Temporal Tracking to assist in algorithms

# anti-aliasing movement

# Promote hitting all the points

# Promote following of pheromones

# Promote Divergence if not all points are hit

# Change Direction if there is a wall

#? Express Movement as a unit vector of likeliness

# Alter behavior depending on altered movement

## Send likeliness to simulation