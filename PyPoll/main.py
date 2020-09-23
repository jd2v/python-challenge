import csv
import os
# Path to resource data
election_csv = os.path.join("Resources","election_data.csv")
# variables for loops
total_vote_counter = 0
khan_votes = 1
correy_votes = 1
li_votes = 1
otooley_votes = 1
#lists for loops
cand_names = []
# Open the data
with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    election_header = next(election_reader)
    for row in election_reader:
        # increase counter to find vote numbers
        total_vote_counter += 1
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
#Find percent each cand won
khan_votes_percent = (khan_votes/total_vote_counter)*100
correy_votes_percent = (correy_votes/total_vote_counter)*100
li_votes_percent = (li_votes/total_vote_counter)*100
otooley_votes_percent = (otooley_votes/total_vote_counter)*100
#round cand votes
khan_votes_percent = round(khan_votes_percent)
correy_votes_percent = round(correy_votes_percent)
li_votes_percent = round(li_votes_percent)
otooley_votes_percent = round(otooley_votes_percent)
#turn votes and percent votes into dictionaries
vote_dict = {"Khan": khan_votes,"Li": li_votes,"O'Tooley": otooley_votes,"Correy": correy_votes}
sorted_vote = sorted(vote_dict, reverse = True)
percent_dict = {"Khan": khan_votes_percent, "Li": li_votes_percent, "O'Tooley": otooley_votes_percent, "Correy": correy_votes_percent}
sorted_percent = sorted(percent_dict, reverse = True)
print(sorted_percent)
print(sorted_vote)
#determine winner
placement = sorted([khan_votes_percent,correy_votes_percent,li_votes_percent,otooley_votes_percent], reverse = True)
print(placement)
#print results
print("Election Results")
print("-----------------------------")