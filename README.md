# BREVIS-SEMITA (Short Path)
This tool is used for finding the shortest pathway in space. The tool utilizes emergent behavior from entites that communicate via chemoreception and operate on a ruleset relefective of their collective goal. 

The codebase utilizes Numpy to for the data structures and manipulation. The goal is to keep utlizise the data structures developed in alpha and alter the codebase's Numpy based funcitons to operate with Arrayfire.

## Installation
There are no installation methods other than installing the libraries used:
- numpy 1.26.*
- arrayfire 3.8.*

## Running
There are no instructions for running, this project is incompleted, but actively developed on!

## File Structure
The file structure depicts this codebase as an application, not a library. This will be changed promptly.

### Ant:
- Fetches spatial data from Space.py
- Short term temporal tracking
- Sends movement data to Space.py to move itself

### Space:
- Allocates simulation space
- Holds data without complex behavor (Pheremones, Roads, etc.)
- Handles raw space data for entities (Ant.py).
- Keeps track of entity spacial data and moves entities based on their likeliness to move. 

### Main:
- Configure the program
- Run the simulation loop

## Development Status
- Restructure current code to easily configure in main
- make the current structures more configurable/flexible
- Create data strucutes with numpy
- Implement entity behavior with numpy
- Integrate arrayfire with numpy
- Optimize numpy structures
