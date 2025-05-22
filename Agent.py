"""
Created on May 14 2025:
@author: <NAME>

Agent module contains the attributes and functionality of an Agent from Rebellion.
"""
import math
import random
from parameters import *

class Agent:
    def __init__(self, patch):
        self.is_active = False
        self.jail_term = 0
        self.risk_aversion = random.uniform(0.0, 1.0)
        self.hardship = random.uniform(0.0, 1.0)
        
        self.patch = patch
        self.patch.agent = True
        self.patch.occupant = self

    def __repr__(self):
        to_string = ""

        if self.is_active:
            to_string += "active"
        elif self.jail_term > 0:
            to_string += "jail"
        else:
            to_string += "quiet"

        return to_string

# follow the netlogo code
    def determine_behaviour(self):
        grievance = self.calculate_grievance()
        p = self.arrest_probability(self.patch.neighborhood)
        self.is_active = (grievance - self.risk_aversion * p) > threshold

    def calculate_grievance(self):
        return self.hardship * (1 - government_legitimacy)

    def arrest_probability(self, neighborhood):
        c = sum(1 for patch in neighborhood if patch)
        a = 1 + sum(1 for patch in neighborhood if patch.agent and patch.occupant.is_active)
        return 1 - math.exp(-k * math.floor(c / a))

    def move(self):
        potential_locations = [patch for patch in self.patch.neighborhood if not patch.agent and not patch.cop]
        print(len(potential_locations))
        if potential_locations:
            new_patch = random.choice(potential_locations)
            self.patch.agent = False
            self.patch.occupant = None
            self.patch = new_patch
            new_patch.agent = True
            new_patch.occupant = self

    def step(self):
        if self.jail_term == 0:
            self.move()
            self.determine_behaviour()
        else:
            self.jail_term -= 1



