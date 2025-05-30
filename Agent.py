"""
Created on May 14 2025:
@author: Aidan Butler, Adam Helal, Mithun Rithvik Ayyasamy Sivakumar

Agent module contains the attributes and functionality of an Agent from Rebellion.
"""
import math
import random

class Agent:
    def __init__(self, patch, params):
        self.is_active = False #boolean for whether an agent is active or not
        self.jail_term = 0

        self.risk_aversion = random.uniform(0.0, 1.0) #randomized properties on init
        self.hardship = random.uniform(0.0, 1.0)
        self.params = params #set of params inputted by the user
        self.patch = patch #each agent contains a reference to the patch they reisde on

    #printable format for an agent
    def __repr__(self):
        to_string = ""

        if self.is_active:
            to_string += "active"
        elif self.jail_term > 0:
            to_string += "jail"
        else:
            to_string += "quiet"

        return to_string

    # function to determine whether an agent will remain quiet or become active 
    # based on the corresponding netlogo information
    # EXTENSION: if an agent is risk averse, going through hard times and has a high arrest probablity
    # and that exceeds a threshold --> they become informants
    def determine_behaviour(self):
        grievance = self.calculate_grievance()
        p = self.arrest_probability(self.patch.neighborhood)
        if (self.risk_aversion * self.hardship * p) > self.params.snitch:
            return True

        self.is_active = (grievance - self.risk_aversion * p) > self.params.threshold
        return False

    # function to calculate grevience for an agent
    # based on the corresponding netlogo information
    def calculate_grievance(self):
        return self.hardship * (1 - self.params.government_legitimacy)
    

    # function to calculate arrest probability for an agent
    # based on the corresponding netlogo information
    #iterates to gather number of cops c in the neighborhood and the number of active agents a
    #k is constant that was taken as is from the netlogo model
    def arrest_probability(self, neighborhood):
        c = sum(1 for patch in neighborhood if not isinstance(patch.occupant, Agent) and patch.occupant is not None)
        a = 1 + sum(1 for patch in neighborhood if isinstance(patch.occupant, Agent) and patch.occupant.is_active)
        calc = 1 - math.exp(-self.params.k * math.floor(c / a))
        return calc

    #move to any location without an occupant ( no cop and only jailed agents)
    def move(self):
        potential_locations = [patch for patch in self.patch.neighborhood if patch.occupant is None]

        if potential_locations:
            new_patch = random.choice(potential_locations)
            self.patch.occupant = None
            self.patch = new_patch
            new_patch.occupant = self

    #function for an iteration of behavior for the agent
    ## changed format to accomadata extension and make sure agent gets turned
    ## into a cop if they become an informant (informally known as a 'snitch')
    def step(self):
        if self.jail_term == 0:
            self.move()
            if (self.determine_behaviour()): 
                return True
        else:
            self.jail_term -= 1

        return False