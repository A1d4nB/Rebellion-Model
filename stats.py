"""
Created on May 14 2025:
@author: Aidan Butler, Adam Helal, Mithun Rithvik Ayyasamy Sivakumar

Stats module contains functionality to track and plot the passed stats
"""

class Stats:

    """track items such as time
     and variety of agents (quiet,active,jailed)
     + extension ones  of cops and of agents"""
    def __init__(self, params):
        self.params = params

        self.time = 0
        self.data_dict = {
                          "time": [],

                          "quiet_track": [],
                          "active_track": [],
                          "jailed_track": [],

                          "cop_track": [],
                          "agent_track": []}
        
    "count agents and classify them"
    def reporting(self, agent_list,cop_list):
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


        self.data_dict["quiet_track"].append(quiet)
        self.data_dict["active_track"].append(active)
        self.data_dict["jailed_track"].append(jailed)
        self.data_dict["time"].append(self.time)
        self.time += 1

        # Data for extension graphs
        self.data_dict["cop_track"].append(len(cop_list))
        self.data_dict["agent_track"].append(len(agent_list))
