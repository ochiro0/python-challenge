#import libraries
import os
import csv

#Path to csv file
election_csv = '../Pypoll/Resources/election_data.csv'


with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

    data = list(csv_reader)
    row_count = len(data)

  # Create new list from CSV column "C" to get a complete list of candidates who received votes
    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
    candicount = len(candilist)

  # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # The winner of the election based on popular vote.
    winner = votes.index(max(votes))    


  # Print statements

with open('PyPoll_result.txt', 'w') as txtfile:
    print("Election Results", file=txtfile)
    print("----------------------------", file=txtfile)
    print(f"Total Votes: {row_count:,}", file=txtfile)
    print("----------------------------", file=txtfile)
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=txtfile)
    print("----------------------------", file=txtfile)
    print(f"Winner: {candilist[winner]}", file=txtfile)
    print("----------------------------", file=txtfile)

