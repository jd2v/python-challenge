import csv
import os
# Path to resource data
election_csv = os.path.join("Resources","election_data.csv")
# variables for loops
total_vote_counter = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
#lists for loops
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
            
        #count votes for cands
        elif row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
print(str(otooley_votes))