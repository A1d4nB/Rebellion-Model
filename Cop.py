"""
Created on May 14 2025:
@author: <NAME>

Cops module contains the attributes and functionality of a Cop from Rebellion.
"""
import random


class Cop:
    def __init__(self, patch):
        self.patch = patch
        self.location = 0

    def enforce(self, k, max_jail_term):
        suspects = [agent for patch in self.patch.neighborhood for agent in patch.agents if agent.active]
        if suspects:
            suspect = random.choice(suspects)
            suspect.active = False
            suspect.jail_term = random.randint(k, max_jail_term)
            self.patch = suspect.patch


    def move(self):
        potential_locations = [patch for patch in self.patch.neighborhood if not patch.agent and not patch.cop]

        new_patch = random.choice(potential_locations)
        self.patch.cop = False
        self.patch = new_patch
        new_patch.cop = True