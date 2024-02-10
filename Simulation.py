import arrayfire as af
import entity
class Spaces:
    def __init__(self, xRes, yRes):
        self.antSpace = af.constant(0, xRes + 2, yRes + 2, dtype=af.Dtype.f32)
        Spaces.maskBoarders(self.antSpace, -1)
        self.pheromoneSpace = af.constant(0, xRes + 2, yRes + 2, dtype=af.Dtype.f32)
        Spaces.maskBoarders(self.pheromoneSpace, -1)
        self.pointSpace = af.constant(0, xRes + 2, yRes + 2, dtype=af.Dtype.u16)        
        Spaces.maskBoarders(self.pointSpace, 65535)
        return None



    ### Masking function
    def maskBoarders(xySpace, borderValue):
        xySpace[0, :] = borderValue
        xySpace[-1, :] = borderValue
        xySpace[:, 0] = borderValue
        xySpace[:, -1] = borderValue
        return borderValue


class Entities:
    def __init__(self, space, antAmount):
        self.space = space

        self.id = [entity.entity() for _ in range(antAmount)]
        self.x = af.constant(0, antAmount, dtype=af.Dtype.u16),
        self.y = af.constant(0, antAmount, dtype=af.Dtype.u16),
        self.rotate = af.constant(0, antAmount, dtype=af.Dtype.u8)
        return None
    
    def randomAnts(self):
        xResolution = self.space.antSpace.dims()[1] - 2
        yResolution = self.space.antSpace.dims()[0] - 2

        self.x = (af.randu(self.x[0].elements(), dtype=af.Dtype.u16) % xResolution).as_type(af.Dtype.u16)
        self.y = (af.randu(self.y[0].elements(), dtype=af.Dtype.u16) % yResolution).as_type(af.Dtype.u16)
        self.rotate = (af.randu(self.rotate.elements(), dtype=af.Dtype.u8) % 4).as_type(af.Dtype.u8)
        return self
    
    def loadAnts(self):
        # collect size of the arrays
        xResolution = self.space.antSpace.dims()[1] - 2
        yResolution = self.space.antSpace.dims()[0] - 2

        # Reset Space to zero and replace mask
        self.space.antSpace = af.constant(0, xResolution + 2, yResolution + 2, dtype=af.Dtype.f32)
        Spaces.maskBoarders(self.space.antSpace, -1)

        # Adjust coordinates for the boarders
        xArray = self.x + 1
        yArray = self.y + 1
        
        # Column Major noted, Calculate linear indices
        indices = af.join(1, xArray, yArray)
        

        # Assign id to linear indices
        for i in range(xArray.elements()):
            self.space.antSpace[xArray[i], yArray[i]] = self.id[i].health
        af.display(self.space.antSpace)
        return self



class Points:
    # Recreate Points object if need to alter the points locations 
    def __init__(self, space, pointFunction):
        self.space = space
        totalPoints = pointFunction.dims()[0]

        # List of points with their id, x, and y
        # ID | X | Y
        self.id = af.iota(totalPoints, dtype=af.Dtype.u16)
        self.x = pointFunction[:, 1].as_type(af.Dtype.u16)
        self.y =  pointFunction[:, 0].as_type(af.Dtype.u16)
        return None
    
    # Loads points to the Space
    def loadPoints(self):
        # collect size of the arrays
        xResolution = self.space.pointSpace.dims()[1] - 2
        yResolution = self.space.pointSpace.dims()[0] - 2

        # Reset Space to zero and replace mask
        self.space.pointSpace = af.constant(0, xResolution + 2, yResolution + 2, dtype=af.Dtype.u16)
        Spaces.maskBoarders(self.space.pointSpace, 65535)

        # Adjust coordinates for the boarders
        xArray = self.x + 1
        yArray = self.y + 1

        # Column Major noted, Calculate linear indices
        indices = af.join(1, xArray, yArray)
        
        # Assign id to linear indices
        for i in range(xArray.elements()):
            self.space.pointSpace[xArray[i], yArray[i]] = self.id[i]
        af.display(self.space.pointSpace)
        
        return self.space

    # Provides random points for the constructor
    def randPoints(space, num):
        # Spatial Bounds
        yResolution = space.antSpace.dims()[0] - 2
        xResolution = space.antSpace.dims()[1] - 2
        
        # Error Handling
        if num > xResolution * yResolution:
            raise ValueError("n exceeds the number of unique points available in the space")

        # Sequences of numbers
        numbersX = af.iota(xResolution, dtype=af.Dtype.u16)
        numbersY = af.iota(yResolution, dtype=af.Dtype.u16)

        # Shuffle the sequences' indices
        xIndices = af.sort(af.randu(xResolution, dtype=af.Dtype.u16))
        yIndices = af.sort(af.randu(yResolution, dtype=af.Dtype.u16))

        # Fetch sequences with shuffled index
        shuffledX = af.lookup(numbersX, xIndices, 0)
        shuffledY = af.lookup(numbersY, yIndices, 0)
        
        # Repeat the process if n is larger than x_res or y_res
        if num > xResolution:
            shuffledX = af.tile(shuffledX, num // xResolution + 1)[:num]
        else:
            shuffledX = shuffledX[:num]

        if num > yResolution:
            shuffledY = af.tile(shuffledY, num // yResolution + 1)[:num]
        else:
            shuffledY = shuffledY[:num]

        # Combine the x and y coordinates
        points = af.join(1, shuffledX, shuffledY)

        return points