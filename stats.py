"""
Created on May 14 2025:
@author: Aidan Butler, Adam Helal, Mithun Rithvik Ayyasamy Sivakumar

Stats module contains functionality to track and plot the passed stats
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Stats:

    #track items such as time
    # and variety of agents (quiet,active,jailed)
    def __init__(self, params):
        self.time_track = np.arange(0, params.simulation_time+1)
        self.quiet_track = []
        self.active_track = []
        self.jailed_track = []
        self.params = params

    #count agents and classify them
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

        self.quiet_track.append(quiet)
        self.active_track.append(active)
        self.jailed_track.append(jailed)


    #take tracked counts and plot them on a graph
    def plotting(self):

        self.quiet_track = np.array(self.quiet_track)
        self.active_track = np.array(self.active_track)
        self.jailed_track = np.array(self.jailed_track)

        plt.plot(self.time_track, self.quiet_track, label="Quiet", color="green")
        plt.plot(self.time_track, self.active_track, label="Active", color="red")
        plt.plot(self.time_track, self.jailed_track, label="Jailed", color="black")


        plt.title(f"{self.params.name}")
        plt.xlabel("Time")
        plt.ylabel("Number of Agents")

        plt.legend()
        plt.grid(True)
        plt.savefig(f"{self.params.name}.jpg", dpi=300)

        plt.clf()

    def export_df(self):
        df = pd.DataFrame(
            {
                f"Quiet": self.quiet_track,
                f"Active": self.active_track,
                f"Jailed": self.jailed_track
            })
        return df


