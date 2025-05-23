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
from stats import Stats
from parameters import *
import random
import math

# Setup
def simulate():
    # Setup


    # All variables in parameters file

    # Checking if the values match
    if (cop_density + initial_agent_density) >= 1:
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
        agent = Agent(grid[i][j])
        agent_list.append(agent)
        grid[i][j].occupant = agent


    # Spawn Cops
    un_occupied_coords = [[i, j] for i in range(grid_size) for j in range(grid_size)
                          if (grid[i][j].occupant is None)]

    cop_coords = random.sample(un_occupied_coords, math.ceil(cop_density * len(coords)))
    cop_list = []
    for i, j in cop_coords:
        cop = Cop(grid[i][j])
        cop_list.append(cop)
        grid[i][j].occupant = cop


    print("Agent - " + str(len(agent_list)))
    print("Cop - " +str(len(cop_list)))

    simulation_track = [i for i in range(0, simulation_time)]


    stats = Stats()
    #Run Simulation
    time_count = simulation_time

    while (time_count > 0):
        try:
            for agent in agent_list:
                agent.step()

            for cop in cop_list:
                cop.enforce()
            time_count -=1

            stats.reporting(agent_list)


        except KeyboardInterrupt:
            print("\nSimulation interrupted by user, exiting....")
            exit(1)
        # Function for reporting

    stats.plotting()




#free_agents = len(agent_list) -

if __name__ == "__main__":
    simulate()

