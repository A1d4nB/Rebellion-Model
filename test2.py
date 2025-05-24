import csv
from parameters import Parameter

with open('Sample_Parameters.csv') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        params = Parameter(row["name"], row['cop_density'], row["initial_agent_density"], row["vision"], row["government_legitimacy"], row["max_jail_term"])

        print(params)

