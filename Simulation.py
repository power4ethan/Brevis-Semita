import numpy as np
import Ant

## Create High Def Space
# X and Y are shifted up and to the right by 1 due to boarders
space = None
def configureSpace(X_RESOLUTION, Y_RESOLUTION):
    ## TODO: This is ugly, fix

    # Dimensions with a mask to prevent edge cases within space
    # Holds Pheromones, Ants, and Points
    antSpace = np.zeros((X_RESOLUTION + 2, Y_RESOLUTION + 2), dtype=np.ushort) # Holds id of ant
    pointSpace = np.zeros((X_RESOLUTION + 2, Y_RESOLUTION + 2), dtype=np.ushort) # Holds id of point
    pheromoneSpace = np.zeros((X_RESOLUTION + 2, Y_RESOLUTION + 2), dtype=np.single) # Holds strength of pheromone
    
    # Masking
    antSpace[0, :] = True
    antSpace[-1, :] = True
    pointSpace[0, :] = True
    pointSpace[-1, :] = True
    pheromoneSpace[0, :] = True
    pheromoneSpace[-1, :] = True
    antSpace[:, 0] = True
    antSpace[:, -1] = True
    pointSpace[:, 0] = True
    pointSpace[:, -1] = True
    pheromoneSpace[:, 0] = True
    pheromoneSpace[:, -1] = True

    # Embed results to space
    space = {'antSpace': antSpace, 'pointSpace': pointSpace, 'pheromoneSpace': pheromoneSpace}

    return space
#---------------------------------------------------------------------------------------------

## Generate Ant List
antIDs = None
def configureAnts(ANT_AMOUNT):
    # List of ants with their id, x, y, and angle
    # ID | X | Y | Counterclockwise Rotation factor (0-3)
    antSpaceDataType = np.dtype([('id', np.ushort),('x', np.ushort),('y', np.ushort),('rotate', np.ubyte)])
    antIDs = np.zeros((ANT_AMOUNT,), dtype=antSpaceDataType)

    # Populate id column
    antIDs['id'] = np.arange(ANT_AMOUNT, dtype=np.ushort)

    # Use Ant Space/Orientation function
    randomAnts()

    return antIDs

#---------------------------------------------------------------------------------------------


### List of Points with their id, x, and y
pointIDs = None
def configurePoints(pointFunction):
    # List of points with their id, x, and y
    # ID | X | Y
    pointSpaceDataType = np.dtype([('id', np.ushort), ('x', np.ushort), ('y', np.ushort)])
    pointIDs = np.zeros((len(pointFunction),), dtype=pointSpaceDataType)
    
    # Populate id column
    pointIDs['id'] = np.arange(len(pointFunction))
    
    # Populate the X and Y
    pointIDs['x'] = pointFunction[:, 0]
    pointIDs['y'] = pointFunction[:, 1]
    return pointIDs
#---------------------------------------------------------------------------------------------


### Initialization of Ant Space and Orientation
def randomAnts():
    antIDs['x'] = np.random.randint(1,space.shape[1] - 1, len(antIDs), dtype=np.ushort)
    antIDs['y'] = np.random.randint(1, space.shape[2] - 1, len(antIDs), dtype=np.ushort)
    antIDs['rotate'] = np.random.randint(0,4,len(antIDs), dtype=np.ubyte)


### Timing
ANT_REFRESH       = None
PHEROMONE_REFRESH = None

def configureTime(ANT_REFRESH, PHEROMONE_REFRESH):
    ANT_REFRESH = ANT_REFRESH
    PHEROMONE_REFRESH = PHEROMONE_REFRESH

## TODO: Update ant id in the space

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
