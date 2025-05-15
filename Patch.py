"""
Created on May 14 2025:
@author: <NAME>

Patch module contains the attributes and functionality of a Patch from Rebellion.
"""

class Patch:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cops = []
        self.agents = []
        self.neighborhood = []