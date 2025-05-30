"""
Created on May 14 2025:
@author: <NAME>

Agent module contains the attributes and functionality of an Agent from Rebellion.
"""
import math
import random

class Agent:
    def __init__(self, patch, params):
        self.is_active = False
        self.jail_term = 0

        self.risk_aversion = random.uniform(0.0, 1.0)
        self.hardship = random.uniform(0.0, 1.0)
        self.params = params
        self.patch = patch

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
        if ((self.risk_aversion * self.hardship * p) > self.params.snitch):
            return True
        p = self.arrest_probability(self.patch.neighborhood)
        self.is_active = (grievance - self.risk_aversion * p) > self.params.threshold
        return False

    def calculate_grievance(self):
        return self.hardship * (1 - self.params.government_legitimacy)

    def arrest_probability(self, neighborhood):
        c = sum(1 for patch in neighborhood if not isinstance(patch.occupant, Agent) and patch.occupant is not None)
        a = 1 + sum(1 for patch in neighborhood if isinstance(patch.occupant, Agent) and patch.occupant.is_active)
        calc = 1 - math.exp(-self.params.k * math.floor(c / a))
        return calc

    def move(self):
        potential_locations = [patch for patch in self.patch.neighborhood if patch.occupant is None]

        if potential_locations:
            new_patch = random.choice(potential_locations)
            self.patch.occupant = None
            self.patch = new_patch
            new_patch.occupant = self

    def step(self):
        if self.jail_term == 0:
            self.move()
            if (self.determine_behaviour()):
                return True


        else:
            self.jail_term -= 1

        return False