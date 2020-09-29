# PyPoll

import os
import csv

# Set variables
votecount = {}
percentage = {}
candidate = []

total_votes = 0

# Changes to the directory of the current .py file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
