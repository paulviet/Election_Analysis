# Election_Analysis
CU-VIRT-DATA-PT-02-2021-U-B-TTH 
Module 03 : Data Analytics Class - Python

## Project Overview
A Colorado Board of Elections personnel assigned the following tasks to complete an audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes
3. Total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Resources
- Data Source:  [election_results.csv](Resources/election_results.csv) 
- Software: Python 3.8.5, Visual Studio Code 1.54.1, Git version 2.30.0.windows.2

## Analysis
- Analysis File: [election_analysis.txt](analysis/election_analysis.txt)

## Summary
The [analysis](analysis/election_analysis.txt) of the election show that:
- There were 369,711 total votes cast in the election in the 3-county vote tally
- The Candidates whom received votes were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The Candidate Results were: 
	- Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
	- Diana DeGette received 73.8% of the vote and 272,892 number of votes.
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the Election was: 
	- Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
	
## Challenge Overview
The data set provided three columns of information, a "Ballot ID", "County", and the "Candidate" voted for. With this date we need to compile a list of Candidates, and totals voter counts that each candidate received.
Some challenges with looking at the data or working with Excel (in 32 bit version) is that the number of lines 369,712 significantly exceeds 32-bit version capability of 65,536. And reviewing the data line by line would be near impossible. Also in addition, an assumption was made that the data set contains unique Ballot ID's, that one Ballot ID was cast for one Candidate.

## Challenge Summary
The challenge was accomplished using Python to read the Comma Separated File and display on the terminal and an analysis file of the accumulating result totals and noting the winner
