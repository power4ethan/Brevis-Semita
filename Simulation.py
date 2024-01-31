import Ant
import arrayfire as af

## ---------------------------------- CONFIGURATION ----------------------------------

### Create High Def Space
# X and Y are shifted up and to the right by 1 due to boarders
def configureSpace(X_RESOLUTION, Y_RESOLUTION):
    ## TODO: Add ability to add layers with configurable dtypes to allow for roads
    xResolution = X_RESOLUTION
    yResolution = Y_RESOLUTION
    # Dimensions with a mask to prevent edge cases within space
    # Holds Pheromones, Ants, and Points
    antSpace = af.constant(0, X_RESOLUTION + 2, Y_RESOLUTION + 2, dtype=af.Dtype.u16) # Holds id of ant
    pointSpace = af.constant(0, X_RESOLUTION + 2, Y_RESOLUTION + 2, dtype=af.Dtype.u16) # Holds id of point
    pheromoneSpace = af.constant(0, X_RESOLUTION + 2, Y_RESOLUTION + 2, dtype=af.Dtype.f32) # Holds strength of pheromone
    
    # Masking
    maskBoarders(antSpace)
    maskBoarders(pointSpace)
    maskBoarders(pheromoneSpace)
    
    # Embed results to space
    space = {
        'antSpace': antSpace, 
        'pointSpace': pointSpace, 
        'pheromoneSpace': pheromoneSpace
    }

    return space

### Masking function
def maskBoarders(xySpace):
        xySpace[0, :] = True
        xySpace[-1, :] = True
        xySpace[:, 0] = True
        xySpace[:, -1] = True
#---------------------------------------------------------------------------------------------


### Generate Ant List
def configureAnts(ANT_AMOUNT):
    # List of ants with their id, x, y, and angle
    # ID | X | Y | Counterclockwise Rotation factor (0-3)
    ids = af.iota(ANT_AMOUNT, dtype=af.Dtype.U16)
    xCoords = af.constant(0, ANT_AMOUNT, dtype=af.Dtype.U16)
    yCoords = af.constant(0, ANT_AMOUNT, dtype=af.Dtype.U16)
    rotates = af.constant(0, ANT_AMOUNT, dtype=af.Dtype.u8)

    antIDs = {
        'id': ids,
        'x': xCoords,
        'y': yCoords,
        'rotate': rotates
    }

    return antIDs

### Initialization of Ant Space and Orientation
def randomAnts(space, antIDs):
    xResolution = space['antSpace'].dims()[1] - 2
    yResolution = space['antSpace'].dims()[0] - 2

    antIDs['x'] = (af.randu(antIDs['x'].dims(), dtype=af.Dtype.u16) * xResolution).as_type(af.Dtype.u16) + 1
    antIDs['y'] = (af.randu(antIDs['y'].dims(), dtype=af.Dtype.u16) * yResolution).as_type(af.Dtype.u16) + 1
    antIDs['rotate'] = (af.randu(antIDs['rotate'].dims(), dtype=af.Dtype.u8) * 4).as_type(af.Dtype.u8)


#---------------------------------------------------------------------------------------------


### List of Points with their id, x, and y
def configurePoints(pointFunction):
    totalPoints = pointFunction.dims()[0]
    # List of points with their id, x, and y
    # ID | X | Y
    ids = af.iota(totalPoints, dtype=af.Dtype.u16)
    xCoords = pointFunction[:, 1].as_type(af.Dtype.U16)
    yCoords = pointFunction[:, 0].as_type(af.Dtype.U16)

    pointIDs = {
        'id': ids,
        'x': xCoords,
        'y': yCoords,
    }
    
    return pointIDs
#---------------------------------------------------------------------------------------------


## ---------------------------------- SPATIAL LOADING FUNCTIONS ----------------------------------

### Update antIDs data in the space
def loadAnts(space, antIDs):
    # collect size of the arrays
    xResolution = space['antSpace'].dims()[1] - 2
    yResolution = space['antSpace'].dims()[0] - 2

    # Reset Space to zero and replace mask
    space['antSpace'] = af.constant(0, xResolution + 2, yResolution + 2, dtype=af.Dtype.u16)
    maskBoarders(space['antSpace'])

    # Adjust coordinates for the boarders
    xArray = antIDs['x'] + 1
    yArray = antIDs['y'] + 1
    
    # Column Major noted, Calculate linear indices
    linearIndices = xArray + yArray * space['antSpace'].dims()[1]

    # Assign id to linear indices
    space['antSpace'][linearIndices] = antIDs['id']

    return space
#---------------------------------------------------------------------------------------------


### Update pointIDs data in the space
def loadPoints(space, pointIDs):
    # collect size of the arrays
    xResolution = space['pointSpace'].dims()[1] - 2
    yResolution = space['pointSpace'].dims()[0] - 2

    # Reset Space to zero and replace mask
    space['pointSpace'] = af.constant(0, xResolution + 2, yResolution + 2, dtype=af.Dtype.u16)
    maskBoarders(space['pointSpace'])

    # Adjust coordinates for the boarders
    xArray = pointIDs['x'] + 1
    yArray = pointIDs['y'] + 1

    # Column Major noted, Calculate linear indices
    linearIndices = xArray + yArray * space['pointSpace'].dims()[1]

    # Assign id to linear indices
    space['pointSpace'][linearIndices] = pointIDs['id']
    
    return space
#---------------------------------------------------------------------------------------------

## ---------------------------------- PHEROMONE FUNCTIONS ----------------------------------
### Update pheromone data in the space

## TODO: Add pheromone behind the ant after finish

## TODO: Add pheromone dispersion cycle

## TODO: Add pheromone fade cycle


## ---------------------------------- ANT FUNCTIONS ----------------------------------
### Allow for interaction between ants and space

## TODO: Run activation on all ants

## TODO: Fetch, clip, and orient data for ant

## TODO: Move ant in antIDs