import os

# Module for reading CSV files
import csv

#set file path
csvpath = os.path.join("..", "Resources", "election_data.csv")

#set list
candidates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

#find the candidates and add them to the list if unique, total votes
    for row in csvreader:
        current_candidate = row[2]
        if current_candidate in candidates:
            candidates[current_candidate] += 1
        else:
            candidates[current_candidate] = 1

#sum the total votes
total_votes = sum(candidates.values())
print("Total Votes:", total_votes)

#find the vote percent and votes per candidates
for c in candidates:
    vote_percent = candidates[c] / total_votes
    print(f"{c}: {vote_percent:.3%} ({candidates[c]})")
    def loop():
        print(f"{c}: {vote_percent:.3%} ({candidates[c]})")

print(f"Winner: {max(candidates, key=candidates.get)}")

with open("pypoll_analysis.txt", "w") as output_file:
    output_file.write(f"Total Votes: {total_votes}\n")
    for c in candidates:
        vote_percent = candidates[c] / total_votes
        output_file.write(f"{c}: {vote_percent:.3%} ({candidates[c]})\n")
    output_file.write(f"Winner: {max(candidates, key=candidates.get)}")