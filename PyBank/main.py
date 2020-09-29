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


