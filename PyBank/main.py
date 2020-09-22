import csv
import os
# Path to resource data
bank_csv = os.path.join("Resources","budget_data.csv")
#Lists to store data
dates = []
changes = []
profits = []
losses = []
#Variables for loops
counter = 0
total_change = 0
# Open the data
with open(bank_csv) as csvfile:
    bankreader = csv.reader(csvfile, delimiter=",")
    bank_header = next(bankreader)
    for row in bankreader:
        # add dates
        dates.append(row[0])
        # add profit/losses
        changes.append(row[1])
        # increase counter to find number of months
        counter = counter+1
        # add loss/profit to running total
        total_change = total_change + int(row[1])
avg_month = total_change/counter
print(avg_month)
print(counter)
print(total_change)