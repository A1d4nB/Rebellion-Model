import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Stats:
    def __init__(self, params):
        self.time_track = np.arange(0, params.simulation_time+1)
        self.quiet_track = []
        self.active_track = []
        self.jailed_track = []
        self.params = params

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
        print(quiet, active, jailed)

        self.quiet_track.append(quiet)
        self.active_track.append(active)
        self.jailed_track.append(jailed)

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

    def export_to_csv(self):
        df = pd.DataFrame(
            {
                "Time": self.time_track,
                "Quiet": self.quiet_track,
                "Active": self.active_track,
                "Jailed": self.jailed_track
            })
        df.to_csv(f"{self.params.name}.csv", index=False)
