"""
Created on May 14 2025:
@author: <NAME>

Patch module contains the attributes and functionality of a Patch from Rebellion.
"""
import math

from parameters import *

class Patch:
    def __init__(self, x, y):
        self.coords = [x, y]
        self.jailed = []
        self.cop = False
        self.agent = False
        self.occupant = None
        # VARIABLE defintion if the Patch will be occupied next turn.
        self.neighborhood = set()

    def populate_neighbours(self, grid):
        for row in grid:
            for neighbor_patch in row:
                distance = self.patch_distance(neighbor_patch)

                if distance <= vision:
                    self.neighborhood.add(neighbor_patch)

    def populate_neighbours_v2(self, grid):
        x,y = self.coords
        for i in range(-vision, vision + 1):
            for j in range(-vision, vision + 1):
                if i == 0 and j == 0:
                    continue
                grid_x = (x + i) % grid_size
                grid_y = (y + j) % grid_size
                self.neighborhood.add(grid[grid_x][grid_y])


    # Could be optimised but should work for now
    def patch_distance(self, neighbor_patch):

        # Calculate distance assuming the board wraps around.

        dr = min(abs(self.coords[0] - neighbor_patch.coords[0]),
                 grid_size - abs(self.coords[0] - neighbor_patch.coords[0]))
        dc = min(abs(self.coords[1] - neighbor_patch.coords[1]),
                 grid_size - abs(self.coords[1] - neighbor_patch.coords[1]))

        return math.sqrt((dr ** 2 + dc ** 2))


    def __repr__(self):
        to_string = ""
        if self.cop:
            to_string += "Cop "
        elif self.agent:
            to_string += "Agent "
        else:
            to_string += "Un-Occupied "

        to_string = f"patch at {self.coords} with Neighbors {len(self.neighborhood)}"


        return  to_string
