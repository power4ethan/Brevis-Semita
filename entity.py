import arrayfire as af
class entity:
    def __init__(self):
        self.health = af.constant(100.0, 1, dtype=af.Dtype.f32)
        self.visionPoints = af.constant(0,3,3,3, dtype=af.Dtype.f32)
        self.pointsHit = []
        return None
    
    def getSurroundings():
        # TODO: Trim down surroundings to fit the 2x3
        # return trimmedSurroundings
        return None
        
