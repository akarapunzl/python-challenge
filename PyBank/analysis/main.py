import os

# Module for reading CSV files
import csv

#set file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#define values
months = 0
profit = 0
max_value = 0
changes = []
max_month = ""
min_month = ""
min_value = 0
previous = 0

#tell python how to read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Loop through doc counting rows
    for row in csvreader:

        #count months
        months = months + 1
        #add up profit
        profit += int(row[1])
        #add up total changes
        if months != 1:
            current_change = int(row[1]) - previous
            changes.append(current_change)
            #find max increase
            if current_change > max_value:
                max_value = current_change
                max_month = row[0]
            #find max decrease
            if current_change < min_value:
                min_value = current_change
                min_month = row[0]
        previous = int(row[1])
        
#find the average 
average = sum(changes) / len(changes)

print("Total Months:", months)
print(f"Total: ${profit}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {max_month} (${max_value})")
print(f"Greatest Decrease in Profits: {min_month} (${min_value})")

with open("pybank_analysis.txt", "w") as output_file:
    output_file.write(f"Total Months: {months} \n")
    output_file.write(f"Total: ${profit:,}\n")
    output_file.write(f"Average Change: ${average}\n")
    output_file.write(f"Greatest Increase in Profits: {max_month} (${max_value})\n")
    output_file.write(f"Greatest Decrease in Profits: {min_month} (${min_value})\n")