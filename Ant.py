import numpy as np
import Space

def __init__(self, id):
    id = np.ushort(id)
    # Surroundings hold the likeliness for the ant to go a certian direction.
    likelinessInput = np.array([0,0,0,0,0,0], dtype=np.single)

# Function for fetching data
    def getSurroundings():
        allSurroundings = Space.getSegment()
        

# Properties for determining likeliness
# anti-aliasing movement



## Configure Intelligence

## Promote hitting all the points

## Promote following of pheremones

## Promote Divergence if not all points are hit

## Change Direction if there is a wall

## Express Movement as a unit vector of likeliness

## Conduct Movement