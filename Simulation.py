import numpy as np
import Ant

## Create High Def Space
space = None
def configureSpace(X_RESOLUTION, Y_RESOLUTION):
    # Dimensions with a mask to prevent edge cases within space
    spaceWithBoarder = np.zeros((3, X_RESOLUTION + 2, Y_RESOLUTION + 2), dtype=np.single) 
    # Mask and Configuration to use for data fetching
    space = np.zeros_like(spaceWithBoarder, dtype=bool)
    space[:, 0, :] = True  # First in y
    space[:, -1, :] = True  # Last in y
    space[:, :, 0] = True  # First in x
    space[:, :, -1] = True  # Last in x
    return space
#---------------------------------------------------------------------------------------------

## Generate Ant List
antIDs = None
def configureAnts(ANT_AMOUNT):
    # List of ants with their id, x, y, and angle
    # ID | X | Y | Counterclockwise Rotation factor (0-3)
    antSpaceDataType = np.dtype([('id', np.ushort),('x', np.ushort),('y', np.ushort),('rotate', np.ubyte)])
    antIDs = np.zeros((ANT_AMOUNT,), dtype=antSpaceDataType)
    return antIDs
#---------------------------------------------------------------------------------------------



### List of Points with their id, x, and y
## TODO: Implement a function that takes a list of x, y points
## TODO: Implement data type

### Initialization of Ant Space and Orientation
## TODO: Think this out.


### Timing
ANT_REFRESH       = None
PHEROMONE_REFRESH = None

def configureTime(ANT_REFRESH, PHEROMONE_REFRESH):
    ANT_REFRESH = ANT_REFRESH
    PHEROMONE_REFRESH = PHEROMONE_REFRESH


### Pheromone Dissipation Logic
## TODO: Implement various algorithms for pheromone dissipation

## Road Generation
## TODO: Add Objects that block and/or can alter movement properties of the ants; akin to roads and buildings.

### Functions for fetching data for ants

## Return a 3x3x3 segment of spatial data for the ant to utilize
def getSegment(id):
    # Fetch data from AntIDs

    # Orient the Space with the ant

    # Return the data as the ant would need it 
    return space[:, x - 1 : x + 1, y - 1 : y + 1]
