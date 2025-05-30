"""
Created on May 14 2025:
@author: Aidan Butler, Adam Helal, Mithun Rithvik Ayyasamy Sivakumar

This will be the main file to run the simulation. This should include the setup and the go functionality.
"""

from itertools import zip_longest

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
   
    #check for illegal combination of densities
    if (params.cop_density + params.initial_agent_density) > 0.99:
        raise ValueError("The sum of INITIAL-COP-DENSITY and INITIAL-AGENT-DENSITY should not be greater than 100")

    # Setup the grid with Patches
    grid = [[Patch(i, j, params) for j in range(params.grid_size)] for i in range(params.grid_size)]
    coords = [[i, j] for i in range(params.grid_size) for j in range(params.grid_size)]

    # For every patch, we have to find neighbour
    for row in grid:
        for patch in row:
            patch.populate_neighbours_v2(grid)

    # Get free cords for agents
    agent_coords = random.sample(coords, math.ceil(params.initial_agent_density * len(coords)))
    agent_list = []

    # Assign agent to each corresponding chosen patch based on the density
    for i, j in agent_coords:
        agent = Agent(grid[i][j], params)
        agent_list.append(agent)
        grid[i][j].occupant = agent

    # Get free cords for cops
    un_occupied_coords = [[i, j] for i in range(params.grid_size) for j in range(params.grid_size)
                          if (grid[i][j].occupant is None)]
    
    # Assign cops to each corresponding chosen patch based on the density
    cop_coords = random.sample(un_occupied_coords, math.ceil(params.cop_density * len(coords)))
    cop_list = []
    for i, j in cop_coords:
        cop = Cop(grid[i][j], params)
        cop_list.append(cop)
        grid[i][j].occupant = cop

    print("Agent - " + str(len(agent_list)))
    print("Cop - " + str(len(cop_list)))

    simulation_track = [i for i in range(0, params.simulation_time)]

    stats = Stats(params) ## init stats module
    # Run Simulation
    time_count = params.simulation_time
    stats.reporting(agent_list,cop_list) #take count of current agent list and their statuses

    #iteration to let model run within x ticks (simulation_time param)
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
                if cop.step():
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

    #function to draw graphs
    stats.plotting()
    #stats.export_to_csv()

    return stats.data_dict


#main function to run experiments involved processing csvs of a parameters
#doing 5 runs for each set of a parameters and averaging those to returrn
#output is a csv file with the counts of each type of agents
def run_experiment():
    with open('Parameters_Extended.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        dict_runs = {}


        for row in reader:
            params = Parameter(row["name"], row['cop_density'], row["initial_agent_density"], row["vision"],
                               row["government_legitimacy"], row["max_jail_term"], row["snitch"], row["cop_threshold"])

            for run in range(0, 5):
                dictionary = simulate(params)
                new_dict = {f'{key}_{run}': value for key, value in dictionary.items() if key != "time"}
                dict_runs = dict_runs | new_dict

            headers = list(dict_runs.keys())
            columns = list(dict_runs[i] for i in headers)
            rows = list(zip_longest(*columns, fillvalue=''))

            with open(f'{row["name"]}.csv',"w", newline='') as csv_write_file:
                writer = csv.writer(csv_write_file)
                writer.writerow(headers)
                writer.writerows(rows)


if __name__ == "__main__":
    run_experiment()
