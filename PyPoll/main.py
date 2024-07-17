import csv

csvpath = '/Users/katchu/Desktop/Data Analysis Bootcamp/Module 3 Starter_Code/PyPoll/Resources/election_data.csv'
with open(csvpath, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)