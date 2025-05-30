import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Stats:
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


        #
        self.data_dict["quiet_track"].append(quiet)
        self.data_dict["active_track"].append(active)
        self.data_dict["jailed_track"].append(jailed)
        self.data_dict["time"].append(self.time)
        self.time += 1

        # Data for extension graphs
        self.data_dict["cop_track"].append(len(cop_list))
        self.data_dict["agent_track"].append(len(agent_list))


    def plotting(self):

        quiet_track = np.array(self.data_dict["quiet_track"])
        active_track = np.array(self.data_dict["active_track"])
        jailed_track = np.array(self.data_dict["jailed_track"])
        time_track = np.array(self.data_dict["time"])

        plt.plot(time_track, quiet_track, label="Quiet", color="green")
        plt.plot(time_track, active_track, label="Active", color="red")
        plt.plot(time_track, jailed_track, label="Jailed", color="black")


        plt.title(f"{self.params.name}")
        plt.xlabel("Time")
        plt.ylabel("Number of Agents")

        plt.legend()
        plt.grid(True)
        plt.savefig(f"{self.params.name}.jpg", dpi=300)

        plt.clf()

        # Extension Graphs
        agent_track = np.array(self.data_dict["agent_track"])
        cop_track = np.array(self.data_dict["cop_track"])

        plt.plot(time_track, agent_track, label="Agents", color="green")
        plt.plot(time_track, cop_track, label="Cops", color="blue")

        plt.title(f"{self.params.name} v2")
        plt.xlabel("Time")
        plt.ylabel("Number of Turtles")

        plt.legend()
        plt.grid(True)
        plt.savefig(f"{self.params.name}v2.jpg", dpi=300)

        plt.clf()
