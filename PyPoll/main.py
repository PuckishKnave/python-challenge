# PyPoll

import os
import csv

# Set variables
vote_counter = {}
percentage = {}
candidate = []

total_votes = 0

# Changes to the directory of the current .py file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get csv file resource
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # Loop through data 
    # Increases vote counter by 1
    for row in csvreader:
        total_votes += 1
        if row[2] in candidate and row[2] not in "Candidate":
            vote_counter[row[2]] = vote_counter[row[2]] + 1
        # Create new spot in list for candidate
        else:
            candidate.append(row[2])
            vote_counter[row[2]] = 1

# Percentage calculation
for key,value in vote_counter.items():
    percentage[key] = str(round((value/total_votes)*100,3)) + "% ("+str(value)+ ")"

# Set winner
winner = max(vote_counter.keys(), key=(lambda k: vote_counter[k]))

# Print election results to terminal
print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print(f"-------------------------\n")
print(f"Percentage: {percentage}\n")
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------")


# Export to election results text file (must already be in folder with .py file)
output_txt = os.path.join("election_results.txt")
with open(output_txt, "w") as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write(f"-------------------------\n")
    text.write(f"Percentage: {percentage}\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("-------------------------")


    

