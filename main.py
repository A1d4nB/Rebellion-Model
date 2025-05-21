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
import random
import math

# Setup
def main():
    # Setup

    # All variables in parameters file

    # Checking if the values match
    if (cop_density + initial_agent_density) < 1:
        raise ValueError("The sum of INITIAL-COP-DENSITY and INITIAL-AGENT-DENSITY should not be greater than 100")

    # Setup the grid with Patches
    #Change this grid to grid in testing and should still work
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    print(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = Patch(i, j)
    coords = [[i,j] for i in range(grid_size) for j in range(grid_size)]

    for row in grid:
        for patch in row:
            patch.patch_distance(grid)



    # Spawn Agents
    agent_coords = random.sample(coords, math.ceil(initial_agent_density * len(coords)))

    #for i, j in agent_coords:
    # Find Random Subset of cords


    # Spawn Cops
    # Find Unoccupied Coords
    # Then DO GPT code

    #Run Simulation



if __name__ == "__main__":
    main()

#This is moved into patch, can probably get rid of this
def get_neighborhood(grid, original_patch):
    neighbors = []
    for row in grid:
        for neighbor_patch in row:
            dr = min(abs(original_patch.coords[0] - neighbor_patch.coords[0]), grid_size - abs(original_patch.coords[0] - neighbor_patch.coords[0]))
            dc = min(abs(original_patch.coords[1] - neighbor_patch.coords[1]), grid_size - abs(original_patch.coords[1] - neighbor_patch.coords[1]))
            if(math.sqrt((dr ** 2 + dc ** 2))) >= vision:
                neighbors.append(neighbor_patch)
    return neighbors

