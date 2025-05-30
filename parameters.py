"""
Created on May 14 2025:
@author: Aidan Butler, Adam Helal, Mithun Rithvik Ayyasamy Sivakumar

Parameters module contains the fixed and variables params used for a simulation
"""

class Parameter:

    def __init__(self, name, cop_density, initial_agent_density, vision, government_legitimacy, max_jail_term):
        # Constant Values
        self.grid_size = 40
        self.k = 2.3
        self.threshold = 0.1
        self.simulation_time = 250

        #Variable Values
        self.name = name
        self.vision = int(vision)
        self.cop_density = float(cop_density)
        self.initial_agent_density = float(initial_agent_density)
        self.government_legitimacy = float(government_legitimacy)
        self.max_jail_term = int(max_jail_term)

    #printable format for the parameters
    def __repr__(self):
        return f"Parameter(name={self.name} cop_density={self.cop_density} initial_agent_density={self.initial_agent_density} government_legitimacy={self.government_legitimacy}"


