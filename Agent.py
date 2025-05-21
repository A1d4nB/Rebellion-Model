"""
Created on May 14 2025:
@author: <NAME>

Agent module contains the attributes and functionality of an Agent from Rebellion.
"""
import math
import random

class Agent:
    def __init__(self, patch):
        self.is_active = False
        self.jail_term = 0
        self.patch = patch
        self.risk_aversion = random.uniform(0.0, 1.0)
        self.hardship = random.uniform(0.0, 1.0)

# follow the netlogo code
    def determine_behaviour(self, k, threshold, government_legitimacy):
        grievance = self.calculate_grievance(government_legitimacy)
        p = self.arrest_probability(self.patch.neighborhood, k)
        self.is_active = (grievance - self.risk_aversion * p) > threshold

    def calculate_grievance(self, government_legitimacy):
        return self.hardship * (1 - government_legitimacy)

    def arrest_probability(self, neighborhood, k):
        c = sum(1 for patch in neighborhood if patch)
        a = 1 + sum(1 for patch in neighborhood for agent in patch.agents if agent.active)
        return 1 - math.exp(-k * math.floor(c / a))

# Function for run/simulation behaviour
# Should include jail term minus,
# Should include Active or not
# then Move

# Function for Move behaviour - Trial
def move(self):
    potential_locations = [patch for patch in self.patch.neighborhood if not patch.agent and not patch.cop]

    new_patch = random.choice(potential_locations)
    self.patch.agent = False
    self.patch = new_patch
    new_patch.agent = True

#Not sure if we should have an external Turtle class of just have move logic within
#each agent class, then have a "simulation" class which might just be in main.



