"""
Created on May 14 2025:
@author: <NAME>

Agent module contains the attributes and functionality of an Agent from Rebellion.
"""
import math

class Agent:
    def __init__(self, patch, risk_aversion, hardship):
        self.is_active = False
        self.jail_term = 0
        self.patch = patch
        self.risk_aversion = risk_aversion
        self.hardship = hardship

# follow the netlogo code
    def determine_behaviour(self, k, threshold, government_legitimacy):
        grievance = self.calculate_grievance(government_legitimacy)
        p = self.arrest_probability(self.patch.neighborhood, k)
        self.is_active = (grievance - self.risk_aversion * p) > threshold

    def calculate_grievance(self, government_legitimacy):
        return self.hardship * (1 - government_legitimacy)

    def arrest_probability(self, neighborhood, k):
        c = sum(1 for patch in neighborhood for cop in patch.cops)
        a = 1 + sum(1 for patch in neighborhood for agent in patch.agents if agent.active)
        return 1 - math.exp(-k * math.floor(c / a))

#Jail term should be calculated within the Cop.
#Not sure if we should have an external Turtle class of just have move logic within
#each agent class, then have a "simulation" class which might just be in main.



