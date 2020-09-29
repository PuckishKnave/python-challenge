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
    profit_average = round(profit_sum/(month_counter - 1), 2)

    # Highest and lowest changes in Profit/Loss
    highest_change = max(profit_change)
    lowest_change = min(profit_change)
    
    highest_month = profit_change.index(highest_change)
    lowest_month = profit_change.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month]
    worst_month = months[lowest_month]

# Print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_counter}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${profit_average}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Profits: {worst_month} (${lowest_change})")

# Export to analysis results text file (must already be in folder)
output_txt = os.path.join("analysis_results.txt")
with open(output_txt, "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {month_counter}\n")
    text.write(f"Total: ${net_profit}\n")
    text.write(f"Average Change: ${profit_average}\n")
    text.write(f"Greatest Increase in Profits: {best_month} (${highest_change})\n")
    text.write(f"Greatest Decrease in Profits: {worst_month} (${lowest_change})\n")
    




        





