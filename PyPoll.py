#In this project, our final Python script will need to be able to deliver the following information when the script is run: 

# Toe data we need to retrieve.
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
# Import the datetime class from the datetime module.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    #for row in file_reader:
    #    #print(row)
    #    print(row[0])
