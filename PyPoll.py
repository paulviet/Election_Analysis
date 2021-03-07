# #In this project, our final Python script will need to be able to deliver the following information when the script is run: 

# #Toe data we need to retrieve.
# #Total number of votes cast
# #A complete list of candidates who received votes
# #Total number of votes each candidate received
# #Percentage of votes each candidate won
# #The winner of the election based on popular vote
# #Import the datetime class from the datetime module.

# #Add our dependencies.
import csv
import os
# #Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# #Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# create candidate options list
candidate_options = []
# Declare the empty dictionary. candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# #Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    file_reader = csv.reader(election_data)
    
    # #Read the header row.
    headers = next(file_reader)
    
    # #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# # Print the total votes.
#print(f"{total_votes:,}")
# # Print the candidate list.
#print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes.
    print(f"{candidate_name} received {vote_percentage:.1f}% of the vote ({votes:,}).\n")
    
    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# Print the winner
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)