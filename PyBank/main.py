# PyBank

import os
import csv

# Set variables
months = []
profit_change = []

month_counter = 0
net_profit = 0
this_month = 0
last_month = 0
profit_changes = 0

# Changes to the directory of current .py file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get data from .csv file in resources folder
budget_data = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    csv_header = next(csvfile)

    # Read through each row
    for row in csvreader:

        # Keeps track of months
        month_counter += 1

        # Net total for Profit/Losses
        this_month = int(row[1])
        net_profit += this_month

        if (month_counter == 1):
            last_month = this_month
            continue
        # Calculate Profit/Loss change
        else:
            profit_changes = this_month - last_month

            # Add months to month list
            months.append(row[0])

            #add change in Profit/Loss to profit change list
            profit_change.append(profit_changes)

            # Move on to next month for next loop
            last_month = this_month
        
    # Sum of net total Profit/Loss
    profit_sum = sum(profit_change)

    # Average of change in Profit/Loss
    profit_average = (profit_sum/month_counter)
    

        





