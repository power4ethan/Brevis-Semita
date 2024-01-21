import numpy as np
import Ant
## Create High Def Space
X_RESOLUTION = 64
Y_RESOLUTION = 64
# Dimensions with a mask to prevent edge cases within space
SpaceWithBoarder = np.zeros((3, X_RESOLUTION + 2, Y_RESOLUTION + 2), dtype=np.single) 
# Mask and Configuration to use for data fetching
Space = np.zeros_like(SpaceWithBoarder, dtype=bool)
Space[:, 0, :] = True  # First in y
Space[:, -1, :] = True  # Last in y
Space[:, :, 0] = True  # First in x
Space[:, :, -1] = True  # Last in x

# List of ants with their id, x, y, and angle
ANT_AMOUNT = 200
antSpaceDataType = np.dtype([('id', np.ushort),('x', np.ushort),('y', np.ushort),('rotate', np.ubyte)])
antIDs = np.zeros((ANT_AMOUNT,), dtype=antSpaceDataType)
# ID | X | Y | Counterclockwise Rotation factor (0-3)

# List of Points with their id, x, and y

# Initalization of Ant Space and Orientation



## Timing
ANT_REFRESH       = 30
PHEREMONE_REFRESH = 60

# Space to Ants
def getSegment(id):
    # Fetch data from AntIDs

    # Orient the Space with the ant

    # Return the data as the ant would need it 
    return Space[:, x - 1 : x + 1, y - 1 : y + 1]

## Pheremone Disipation Logic

## Functions for fetching data for ants