"""
Created on May 14 2025:
@author: <NAME>

Agent module contains the attributes and functionality of an Agent from Rebellion.
"""

class Agent:
    def __init__(self):
        self.isActive = False
        self.jailTerm = False

# follow the netlogo code
    def determineBehaviour(self):
        self.isActive = True

    def calculateGrievance(self):
        self.jailTerm = False

    def arrestProbability(self):
        self.jailTerm = False



