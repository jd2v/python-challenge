import csv
import os
# Path to resource data
election_csv = os.path.join("Resources","election_data.csv")
# variables for loops
total_vote_counter = 0
#lists for loops
cand_votes = []
cand_names = []
# Open the data
with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    election_header = next(election_reader)
    for row in election_reader:
        # increase counter to find vote numbers
        total_vote_counter = total_vote_counter + 1
        #Add name to cand_name if not already present in list
        if row[2] not in cand_names:
            cand_names.append(row[2])
print(cand_names)