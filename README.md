# BREVIS-SEMITA
This tool is used for finding the shortest pathway in space. The tool utilizes emergent behavior from entites that communicate via chemoreception and operate on a ruleset relefective of their collective goal.

## Installation
There are no installation methods other than installing the libraries used:
- numpy 1.26.*
- arrayfire 3.8.*

## Running
There are no instructions for running, this project is incompleted, but actively developed on!

## File Structure
The file structure depicts this codebase as an application, not a library.

### Ant:
- Holds the behavior of the ants
- Fetches data from Space
- Sends movement data to Space to be moved

### Space:
- Allocates Simulation Space
- Handles Space Data for Ants
- Handles Physics for pheremones

### Main:
- Configure the program
- Run the Funciton Loop

## Development Status
- Initial development in numpy
- Arrayfire Functionality after implementation of simulation with numpy
- Optimize numpy structures
