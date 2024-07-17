import csv

total_votes = 0  #Start variable of votes off at zero
candidate_column = {}  #Dictionary to store candidate names as keys and vote counts as values
winner_name = ""  #Will store the name of the candidate with the most votes
max_votes = 0  #Start count at zero

csvpath = '/Users/katchu/Desktop/Data Analysis Bootcamp/Module 3 Starter_Code/PyPoll/Resources/election_data.csv'

with open(csvpath, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1  #Go through the row and add the total to get total votes
        candidate_name = row[2]  #Column 3, but starts at index 0. Grabs candidate names

        if candidate_name in candidate_column:
            candidate_column[candidate_name] += 1  #If candidate exists, add a vote to them
        else:
            candidate_column[candidate_name] = 1  #If candidate doesn't exist, start with 1 vote

    for candidate_name in candidate_column:
        votes = candidate_column[candidate_name]  #Retrieve vote count for the candidate
        vote_percentage = (votes / total_votes) * 100  #Convert votes to percentage
        
        if votes > max_votes:
            max_votes = votes
            winner_name = candidate_name  #Update winner_name to current candidate if they have more votes

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate_name in candidate_column:
    votes = candidate_column[candidate_name]
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.3f}% ({votes})") #Prints the candidate name and their voting percentage
print("-------------------------")
print(f"Winner: {winner_name}")  #Print the winner based on the highest vote count
print("-------------------------")  