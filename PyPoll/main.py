#Task: Create a Python script that analyzes the votes. 
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#Import os module
import os

#Variables
voter_data = []
candidates = []
voted_for_candidate = []


#Module for reading csv and path
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

import collections
from collections import Counter

# Open and read csv
with open(csvpath, "r", newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

     #File has headers, we want to start on the next row.
    header = next(csvreader)

    # Read the data
    for row in csvreader:
        # append the cadidate data on the third row to candidates variable
        candidates.append(row[2])

    # sort the candidates to make operations
    sorted_candidates = sorted(candidates)
    
    #review the data
    #print(sorted_candidates)

    #count votes per candidate
    candidate_counter = Counter (sorted_candidates) 
    #append the votes using the most_common function to order
    voted_for_candidate.append(candidate_counter.most_common(4))
    #add the values for percentage calculation
    total_votes = sum(candidate_counter.values())
    
    #review the data
    #print(voted_for_candidate)
    
    #calculate results to print
    
    winner = voted_for_candidate[0][0][0]
    winner_votes = voted_for_candidate[0][0][1]
    
    #print(winner)
    #print(winner_votes)
    
    second_place = voted_for_candidate[0][1][0]
    second_place_votes = voted_for_candidate[0][1][1]
  
    #print(second_place)
    #print(second_place_votes)
    
    third_place = voted_for_candidate[0][2][0]
    third_place_votes = voted_for_candidate[0][2][1]
  
    #print(third_place)
    #print(third_place_votes)
    
    fourth_place = voted_for_candidate[0][3][0]
    fourth_place_votes = voted_for_candidate[0][3][1]
  
    #print(fourth_place)
    #print(fourth_place_votes)
    
    #calculate percentages
    winner_percentage = format((winner_votes/total_votes)*100,'.3f')
    #print(winner_percentage)
    second_place_percentage = format((second_place_votes/total_votes)*100,'.3f')
    #print(second_place_percentage)
    third_place_percentage = format((third_place_votes/total_votes)*100,'.3f')
    #print(third_place_percentage)
    fourth_place_percentage = format((fourth_place_votes/total_votes)*100,'.3f')
    #print(fourth_place_percentage)
    
# print resutls
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(candidate_counter.values())}")
print("-------------------------")
print(f"{winner}: {winner_percentage}% ({winner_votes})")
print(f"{second_place}: {second_place_percentage}% ({second_place_votes})")
print(f"{third_place}: {third_place_percentage}% ({third_place_votes})")
print(f"{fourth_place}: {fourth_place_percentage}% ({fourth_place_votes})")
print("-------------------------")
print(f"Winner:  {winner}")
print("-------------------------")

#Output to text file
text_file = open("analysis/election_Results.txt", "w")
text_file.write("Election Results\n")
text_file.write("-------------------------\n")
text_file.write(f"Total Votes:  {sum(candidate_counter.values())}\n")
text_file.write("-------------------------\n")
text_file.write(f"{winner}: {winner_percentage}% ({winner_votes})\n")
text_file.write(f"{second_place}: {second_place_percentage}% ({second_place_votes})\n")
text_file.write(f"{third_place}: {third_place_percentage}% ({third_place_votes})\n")
text_file.write(f"{fourth_place}: {fourth_place_percentage}% ({fourth_place_votes})\n")
text_file.write("-------------------------\n")
text_file.write(f"Winner:  {winner}\n")
text_file.write("-------------------------\n")    
text_file.close()