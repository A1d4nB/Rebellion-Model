"""
Created on May 14 2025:
@author: <NAME>

Cops module contains the attributes and functionality of a Cop from Rebellion.
"""
import random


class Cop:
    def __init__(self, patch, params):
        self.patch = patch
        self.params = params

    def enforce(self):
        suspects = [patch.occupant for patch in self.patch.neighborhood if not
                    isinstance(patch.occupant, Cop) and patch.occupant is not None and patch.occupant.is_active]
        average = len(suspects) / len(self.patch.neighborhood)
        if suspects and average > self.params.cop_threshold:
            return True
        elif suspects:
            suspect = random.choice(suspects)
            suspect.is_active = False
            suspect.jail_term = random.randint(1, self.params.max_jail_term)
            self.patch.occupant = None
            self.patch = suspect.patch
            self.patch.occupant = self
        return False

    def move(self):
        potential_locations = [patch for patch in self.patch.neighborhood if patch.occupant is None]

        new_patch = random.choice(potential_locations)
        self.patch.occupant = None
        self.patch = new_patch
        new_patch.occupant = self

    def step(self):
        # agent.run
        self.move()
        if self.enforce():
            return True
        return False

