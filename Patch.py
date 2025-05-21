"""
Created on May 14 2025:
@author: <NAME>

Patch module contains the attributes and functionality of a Patch from Rebellion.
"""
from parameters import vision

class Patch:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jailed = []
        self.cop = False
        self.agent = False
        self.neighborhood = []
    def __repr__(self):
        return f"Patch({self.x}, {self.y}, {self.occupied_by})"
