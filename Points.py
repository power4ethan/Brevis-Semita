import Simulation
import arrayfire as af
## TODO: Implement
## Point handler
# All functions return a 2 x n matrix of   

# Function to generate a valid random set of points
def randPoints(space, num):
    # Spatial Bounds
    xResolution = space['antSpace'].dims()[1] - 1
    yResolution = space['antSpace'].dims()[0] - 1
    
    # Error Handling
    if num > xResolution * yResolution:
        raise ValueError("n exceeds the number of unique points available in the space")

    # Sequences of numbers
    numbersX = af.seq(1, xResolution)
    numbersY = af.seq(1, yResolution)

    # Shuffle the sequences' indices
    xIndices = af.argsort(af.randu(xResolution, dtype=af.Dtype.u16))
    yIndices = af.argsort(af.randu(yResolution, dtype=af.Dtype.u16))

    # Fetch sequences with shuffled index
    shuffledX = numbersX[xIndices]
    shuffledX = numbersX[yIndices]

    # Repeat the process if n is larger than x_res or y_res
    if num > xResolution:
        shuffled_x = af.tile(shuffled_x, num // xResolution + 1)[:num]
    else:
        shuffled_x = shuffled_x[:num]

    if num > yResolution:
        shuffled_y = af.tile(shuffled_y, num // yResolution + 1)[:num]
    else:
        shuffled_y = shuffled_y[:num]

    # Combine the x and y coordinates
    points = af.join(1, shuffled_x, shuffled_y)

    return points
    
# Function to generate a valid set of points from an list via argument
def argPoints(pointList):
    return None

# Function to generate a valid set of points from a file
def filePoints(file):
    return None
    # TODO: Add decoding for a file type