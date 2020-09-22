import csv
import os
# Path to resource data
election_csv = os.path.join("..","Resources","election_data.csv")
# variables for loops
counter = 0
# Open the data
with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    election_header = next(election_reader)
    for row in election_reader:
        # increase counter to find vote numbers
        counter = counter + 1
        