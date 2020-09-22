import csv
import os
# Path to resource data
bank_csv = os.path.join("..","Resources","budget_data.csv")
#Lists to store data
dates = []
profits = []
losses = []
# Open the data
with open(bank_csv) as csvfile:
    bankreader = csv.reader(csvfile, delimiter=",")

