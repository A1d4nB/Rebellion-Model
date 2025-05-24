"""
Created on May 14 2025:
@author: <NAME>

Patch module contains the attributes and functionality of a Patch from Rebellion.
"""
import math
import Agent
import Cop

from parameters import *

class Patch:
    def __init__(self, x, y, params):
        self.coords = [x, y]
        self.occupant = None
        # VARIABLE defintion if the Patch will be occupied next turn.
        self.neighborhood = set()
        self.params = params

    def populate_neighbours(self, grid):
        for row in grid:
            for neighbor_patch in row:
                distance = self.patch_distance(neighbor_patch)

                if distance <= self.params.vision:
                    self.neighborhood.add(neighbor_patch)

    def populate_neighbours_v2(self, grid):
        x, y = self.coords
        for i in range(-self.params.vision, self.params.vision + 1):
            for j in range(-self.params.vision, self.params.vision + 1):
                if i == 0 and j == 0:
                    continue
                grid_x = (x + i) % self.params.grid_size
                grid_y = (y + j) % self.params.grid_size
                self.neighborhood.add(grid[grid_x][grid_y])


    # Could be optimised but should work for now
    def patch_distance(self, neighbor_patch):

        # Calculate distance assuming the board wraps around.

        dr = min(abs(self.coords[0] - neighbor_patch.coords[0]),
                 self.params.grid_size - abs(self.coords[0] - neighbor_patch.coords[0]))
        dc = min(abs(self.coords[1] - neighbor_patch.coords[1]),
                 self.params.grid_size - abs(self.coords[1] - neighbor_patch.coords[1]))

        return math.sqrt((dr ** 2 + dc ** 2))


    def __repr__(self):
        to_string = ""
        if isinstance(self.occupant, Cop):
            to_string += "Cop "
        elif isinstance(self.occupant, Agent):
            to_string += "Agent "
        else:
            to_string += "Un-Occupied "

        to_string = f"patch at {self.coords} with Neighbors {len(self.neighborhood)}"


        return  to_string
