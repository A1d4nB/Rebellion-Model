"""
Created on May 14 2025:
@author: <NAME>

Cops module contains the attributes and functionality of a Cop from Rebellion.
"""
import random
from parameters import *
from Agent import Agent

class Cop:
    def __init__(self, patch):
        self.patch = patch

    def enforce(self):
        suspects = [patch.occupant for patch in self.patch.neighborhood if isinstance(patch.occupant, Agent) and patch.occupant.is_active]
        if suspects:
            suspect = random.choice(suspects)
            suspect.is_active = False
            suspect.jail_term = random.randint(1, max_jail_term)
            suspect.patch.jailed.append(suspect)
            self.patch.occupant = None
            self.patch = suspect.patch
            self.patch.occupant = self


    def move(self):
        potential_locations = [patch for patch in self.patch.neighborhood if patch.occupant is None]

        new_patch = random.choice(potential_locations)
        self.patch.cop = False
        self.patch.occupant = None
        self.patch = new_patch
        new_patch.cop = True
        new_patch.occupant=self

    def step(self):
        # agent.run
        self.move()
        self.enforce()
