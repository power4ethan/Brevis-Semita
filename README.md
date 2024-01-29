# BREVIS-SEMITA (Short Path)
This tool is used for finding the shortest pathway between a set of points in space. The tool utilizes emergent behavior from entities that communicate via chemoreception and operate on a rule-set reflective of their collective goal. 

## Installation
There are no installation methods other than installing the libraries used:
- ArrayFire 3.8.*

## Running
There are no instructions for running, this project is incomplete, but actively developed on!

## File Structure
The file structure depicts this codebase as an application, not a library. This will be changed promptly.

### main.py:
- Configure the program.
- Run the simulation loop.

### Ant.py:
- Fetches spatial data from Simulation.py.
- Short term temporal tracking.
- Sends movement data to Simulation.py to move itself.

### Simulation.py:
- Allocates the simulation space.
- Holds data about entities without complex behavior (Pheromones, Roads, etc.)
- Handles raw space data for entities (Ant.py).
- Moves entities based on their likeliness to move. 

### Points.py
- Parses points from a file.
- Generates a list of points from an argument.
- Generates a list of random points.

## Current Development Goals
- Complete pheromone physics.
- Complete Simulation to Ant communication.
- Complete Ant behavioral logic.
- Implement entity behavior using genetic evolution.
