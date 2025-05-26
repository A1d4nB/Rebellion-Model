"""
Created on May 14 2025:
@author: <NAME>

This will be the main file to run the simulation. This should include the setup and the go functionality.
"""
from parameters import Parameter
from Agent import Agent
from Cop import Cop
from Patch import Patch
from stats import Stats
import random
import math
import csv


# Setup
def simulate(params):
    # Setup

    # All variables in parameters file

    # Checking if the values match
    print(params.cop_density)
    print(params.initial_agent_density)
    if (params.cop_density + params.initial_agent_density) > 0.99:
        raise ValueError("The sum of INITIAL-COP-DENSITY and INITIAL-AGENT-DENSITY should not be greater than 100")

    # Setup the grid with Patches
    # Change this grid to grid in testing and should still work
    grid = [[Patch(i, j, params) for j in range(params.grid_size)] for i in range(params.grid_size)]
    coords = [[i, j] for i in range(params.grid_size) for j in range(params.grid_size)]

    # For every patch, we have to find neighbour

    for row in grid:
        for patch in row:
            patch.populate_neighbours_v2(grid)

    # Spawn Agents
    agent_coords = random.sample(coords, math.ceil(params.initial_agent_density * len(coords)))
    # Array of All Agents
    agent_list = []

    for i, j in agent_coords:
        agent = Agent(grid[i][j], params)
        agent_list.append(agent)
        grid[i][j].occupant = agent

    # Spawn Cops
    un_occupied_coords = [[i, j] for i in range(params.grid_size) for j in range(params.grid_size)
                          if (grid[i][j].occupant is None)]

    cop_coords = random.sample(un_occupied_coords, math.ceil(params.cop_density * len(coords)))
    cop_list = []
    for i, j in cop_coords:
        cop = Cop(grid[i][j], params)
        cop_list.append(cop)
        grid[i][j].occupant = cop

    print("Agent - " + str(len(agent_list)))
    print("Cop - " + str(len(cop_list)))

    simulation_track = [i for i in range(0, params.simulation_time)]

    stats = Stats(params)
    # Run Simulation
    time_count = params.simulation_time
    stats.reporting(agent_list,cop_list)

    while time_count > 0:
        try:
            for agent in agent_list:
                # If the agent  turns into a class traitor
                if agent.step():
                    new_cop = Cop(agent.patch, params)
                    agent.patch.occupant = new_cop
                    cop_list.append(new_cop)
                    agent_list.remove(agent)


            for cop in cop_list:
                # When cop becomes overwhelmed with active agents, they turn into an rebelling agent
                if cop.enforce():
                    new_agent = Agent(cop.patch, params)
                    new_agent.is_active = True
                    cop.patch.occupant = new_agent
                    cop_list.remove(cop)
                    agent_list.append(new_agent)

            time_count -= 1
            stats.reporting(agent_list,cop_list)
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user, exiting....")
            exit(1)
        # Function for reporting

    stats.plotting()
    stats.export_to_csv()


# free_agents = len(agent_list) -

if __name__ == "__main__":

    with open('Parameters_new.csv') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            params = Parameter(row["name"], row['cop_density'], row["initial_agent_density"], row["vision"],
                               row["government_legitimacy"], row["max_jail_term"], row["snitch"], row["cop_threshold"])
            simulate(params)





# variable
# simulation_time = 500
# cop_density = 0.40
# initial_agent_density = 0.56
# vision = 7
# government_legitimacy = 0.12
# max_jail_term = 4
