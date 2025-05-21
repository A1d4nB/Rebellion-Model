from Agent import Agent
from Patch import Patch
import random
import math


grid_size = 2
initial_agent_density = 0.2

grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
print(grid)
for i in range(grid_size):
    for j in range(grid_size):
        grid[i][j] = Patch(i,j)

coords = [[i,j] for i in range(grid_size) for j in range(grid_size)]


fill_coords = random.sample(coords, math.ceil(initial_agent_density * len(coords)))



for agent_x_coord, agent_y_coord in fill_coords:
    print(agent_x_coord, agent_y_coord)
    grid[agent_x_coord][agent_y_coord].occupied = True
    #agent = Agent(grid[agent_x_coord][agent_y_coord], 0.1, 0.1)

    #grid[fill_coords[0]][fill_coords[1]].occupied_by(agent)



print(grid)
