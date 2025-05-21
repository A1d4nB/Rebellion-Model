"""
Created on May 14 2025:
@author: <NAME>

This will be the main file to run the simulation. This should include the setup and the go functionality.
"""
from numpy.f2py.auxfuncs import throw_error

from turtle import Turtle
from Agent import Agent
from Cop import Cop
from Patch import Patch
from parameters import *

# Setup
def main():
    # Setup

    # All variables in parameters file

    # Checking if the values match
    if (cop_density + initial_agent_density) < 1:
        raise ValueError("The sum of INITIAL-COP-DENSITY and INITIAL-AGENT-DENSITY should not be greater than 100")

    # Setup the grid with Patches
    grid = [[Patch(x,y) for y in range(grid_size) for x in range(grid_size)]]
    coords = [[i,j] for i in range(grid_size) for j in range(grid_size)]


    for row in grid:
        for patch in row:
            patch.neighborhood = get_neighborhood(grid, patch)



    # Spawn Agents
    # Find Random Subset of cords


    # Spawn Cops
    # Find Unoccupied Coords
    # Then DO GPT code

    #Run Simulation



if __name__ == "__main__":
    main()


def get_neighborhood(grid, patch):
    neighbors = []
    for row in grid:
        for p in row:
            if (abs(p.x - patch.x) <= vision) and (abs(p.y - patch.y) <= vision and p != patch):
                neighbors.append(patch)
    return neighbors