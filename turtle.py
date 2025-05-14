"""
Created on May 14 2025:
@author: <NAME>

Turtle module contains functions to capture the essential attributes such as location and methods for movement
like turtles in netlogo

"""
import random as rand

DIMENSIONS = 40*40
class Turtle:

    def __init__(self):
        self.locationX = rand.randint(-200, 200)
        self.locationY = rand.randint(-200, 200)

    """
    Function to move turtles to a empty space"""
    def move(self):
        self.locationX += rand.randint(-1,1)

