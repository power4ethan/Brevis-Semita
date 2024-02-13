import simulation
import arrayfire as af

af.set_backend('opencl')

# Configure Space Resolution
s = simulation.Spaces(10,10)
af.display(s.antSpace[:,:])
af.display(s.pheromoneSpace[:,:])
af.display(s.pointSpace[:,:])

# Configure Simulation Points
p = simulation.Points(s, simulation.Points.randPoints(s, 10))
# Load the points
p.loadPoints()
af.display(s.pointSpace)

# Configure entities
e = simulation.Entities(s, 25)
e.randomAnts() # Randomize ant location + orientation
af.display(e.x[:])
af.display(e.y[:])
af.display(e.rotate[:])
print(e.id)

# Load Ants into space
e.loadAnts()

e.runAnts()