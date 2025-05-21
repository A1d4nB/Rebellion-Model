from Agent import Agent
from Patch import Patch
import random
import math
from Cop import Cop


grid_size = 6
initial_agent_density = 0.25
cop_density = 0.5
vision = 2

#grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

grid = [[Patch(i, j) for j in range(grid_size)] for i in range(grid_size)]
coords = [[i,j] for i in range(grid_size) for j in range(grid_size)]


fill_coords = random.sample(coords, math.ceil(initial_agent_density * len(coords)))




for i,j in fill_coords:
    agent = Agent(grid[i][j])
    grid[i][j].agent = True

un_occupied_coords = [[i,j] for i in range(grid_size) for j in range(grid_size)
                      if (grid[i][j].agent == False and grid[i][j].cop == False)]

cop_coords = random.sample(un_occupied_coords, math.ceil(cop_density * len(un_occupied_coords)))

cop_list = []
for i, j in cop_coords:
    cop_list.append(Cop(grid[i][j]))
    grid[i][j].cop = True


#print(grid)

# Testing for Neighbours





sample = grid[0][0]
x,y = sample.coords
for i in range(-vision, vision + 1):

    for j in range(-vision, vision + 1):
        if (i == 0 and j == 0):
            continue

        grid_x = (x+i)%grid_size
        grid_y = (y+j)%grid_size
        sample.neighborhood.append(grid[grid_x][grid_y])
print(len(sample.neighborhood))

sample.populate_neighbours(grid)
print(len(sample.neighborhood))


