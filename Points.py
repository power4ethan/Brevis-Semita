import numpy as np
import Simulation
## TODO: Implement
## Point handler
# All functions return a 2 x n matrix of   

# Function to generate a valid random set of points
def randPoints(num):
    # Using a set to ensure uniqueness
    coordinates = set() 

    while len(coordinates) < num:
        x = np.random.randint(1, Simulation.X_RESOLUTION + 1 , dtype=np.ushort)
        y = np.random.randint(1, Simulation.Y_RESOLUTION + 1 , dtype=np.ushort)
        coordinates.add((x, y))

    return np.array(list(coordinates))
    
# Function to generate a valid set of points from an list via argument
def argPoints(pointList):
    return None

# Function to generate a valid set of points from a file
def filePoints(file):
    return None
    # TODO: Add decoding for a file type