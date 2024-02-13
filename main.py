### Not functional

import simulation
## Initialize simulation
# Configure resolution
X_RESOLUTION = 64
Y_RESOLUTION = 64

space = simulation.configureSpace(X_RESOLUTION, Y_RESOLUTION)

# Configure entities in the space
ANT_AMOUNT = 50
Simulation.configureAnts(ANT_AMOUNT)

# Configure Points in the space
POINT_AMOUNT = 6
Simulation.configurePoints(Points.randPoints(space, POINT_AMOUNT))

# Configure entity behavior/logic functions


# Configure the amount of simulations to be ran


# Configure the visualization(s)


# Start simulation loop
    # Load ants from antIDs into space
    # All ants fetch surroundings
    # Pheromone dissipation logic is applied to all cells (can be done while ants compute on separate thread)
    # All ants compute, and send likeliness to the simulation 
    # Simulation add pheromones on their previous location (already loaded in space) in space based on likeliness (This could be changed)
    # once antIDs is completely done updating, ants in space are cleared
def simulationLoop():
    return None
    