import Simulation
import Points
## Initialize simulation
# Configure resolution
X_RESOLUTION = 64
Y_RESOLUTION = 64

Simulation.configureSpace(X_RESOLUTION, Y_RESOLUTION)

# Configure entities in the space
ANT_AMOUNT = 50
Simulation.configureAnts(ANT_AMOUNT)

# Configure Points in the space
POINT_AMOUNT = 6
Simulation.configurePoints(Points.randPoints(POINT_AMOUNT))

# Configure update frequency


# Configure non-complex entity logic



# Configure the amount of simulations to be ran

# Configure the visualization(s)

# Start simulation loop