"""
Created on May 14 2025:
@author: <NAME>

Patch module contains the attributes and functionality of a Patch from Rebellion.
"""
import math

from parameters import vision
import parameters

class Patch:
    def __init__(self, x, y):
        self.coords = [x, y]
        self.jailed = []
        self.cop = False
        self.agent = False
        self.neighborhood = []

    def patch_distance(self, original_patch, grid):
        for row in grid:
            for neighbor_patch in row:
                dr = min(abs(original_patch.coords[0] - neighbor_patch.coords[0]),
                         parameters.grid_size - abs(original_patch.coords[0] - neighbor_patch.coords[0]))
                dc = min(abs(original_patch.coords[1] - neighbor_patch.coords[1]),
                         parameters.grid_size - abs(original_patch.coords[1] - neighbor_patch.coords[1]))
                if (math.sqrt((dr ** 2 + dc ** 2))) <= vision:
                    self.neighborhood.append(neighbor_patch)


    def __repr__(self):
        return f"Patch({self.coords[0]}, {self.coords[1]})"
