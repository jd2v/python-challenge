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
#zip dates and changes together
full_data = zip(dates, changes)
#find avg month net +/-
avg_month = total_change/counter
#find best and worst increase/decrease
best_month = max(changes)
worst_month = min(changes)
#find best worst month date
best_month_date = dates[full_data.index(best_month)]
worst_month_date = [dates for changes in full_data if changes == worst_month]
# print
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(counter))
print("Total: $" + str(total_change))
print("Average Change: $" + str(avg_month))
print("Greatest Increase in Profits: " + str(best_month_date) + " ($" + str(best_month) + ")")
print("Worst Decrease in Profits: " + str(worst_month_date) + " ($" + str(worst_month) + ")")
#export
output 