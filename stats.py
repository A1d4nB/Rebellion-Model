"""
Created on May 14 2025:
@author: Aidan Butler, Adam Helal, Mithun Rithvik Ayyasamy Sivakumar

Stats module contains functionality to track and plot the passed stats
"""

class Stats:

    "track items such as time and variety of agents (quiet,active,jailed)"
    def __init__(self, params):
        self.time = 0
        self.data_dict = {
            "time": [],

            "quiet_track": [],
            "active_track": [],
            "jailed_track": [],
        }
        self.params = params

    "count agents and classify them"
    def reporting(self, agent_list):
        quiet = 0
        jailed = 0
        active = 0
        for agent in agent_list:
            if agent.jail_term >= 1:
                jailed += 1
            elif agent.is_active:
                active += 1
            else:
                quiet += 1

        # Add data to the dicitonary
        self.data_dict["quiet_track"].append(quiet)
        self.data_dict["active_track"].append(active)
        self.data_dict["jailed_track"].append(jailed)
        self.data_dict["time"].append(self.time)
        self.time += 1

