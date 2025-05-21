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
    if (cop_density + initial_agent_density) > 1:
        raise ValueError("The sum of INITIAL-COP-DENSITY and INITIAL-AGENT-DENSITY should not be greater than 100")

    # Setup the grid with Patches
    #Change this grid to grid in testing and should still work
    grid = [[Patch(i, j) for j in range(grid_size)] for i in range(grid_size)]
    coords = [[i,j] for i in range(grid_size) for j in range(grid_size)]

    # For every patch, we have to find neighbour

    for row in grid:
        for patch in row:
            #patch.populate_neighbours(grid)
            patch.populate_neighbours_v2(grid)




    # Spawn Agents
    agent_coords = random.sample(coords, math.ceil(initial_agent_density * len(coords)))
    # Array of All Agents
    agent_list = []

    for i, j in agent_coords:
        agent_list.append(Agent(grid[i][j]))
        grid[i][j].agent = True

    # Spawn Cops
    un_occupied_coords = [[i, j] for i in range(grid_size) for j in range(grid_size)
                          if (grid[i][j].agent == False and grid[i][j].cop == False)]

    cop_coords = random.sample(un_occupied_coords, math.ceil(cop_density * len(un_occupied_coords)))
    cop_list = []
    for i, j in cop_coords:
        cop_list.append(Cop(grid[i][j]))
        grid[i][j].cop = True

    print("Agent - " + str(len(agent_list)))
    print("Cop - " +str(len(cop_list)))

    #print(len(grid[0][0].neighborhood))


    #Run Simulation



if __name__ == "__main__":
    main()

