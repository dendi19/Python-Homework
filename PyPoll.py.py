import csv
import os
import sys

path = os.path.join('..', 'Instructions','PyPoll', 'Resources', 'election_data.csv')
sys.stdout = open('Election_Outcome.txt','wt') # needed import sys for this function

sum_of_votes = []
num_of_voter = 0

with open(path, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for votes in reader:
        num_of_voter = (num_of_voter + 1 )
        #sum_of_votes.append(float(votes[0]))
        #totals = sum(votes[0])
print(f"There were {num_of_voter} votes in the last elecion.")

unique_list = []

with open(path, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for candids in reader:
        if candids[2] not in unique_list:
            unique_list.append(candids[2])
print(f"Those who ran were {unique_list[0]}, {unique_list[1]}, {unique_list[2]}, and {unique_list[3]}.")

num_of_Khan = 0
num_of_Correy = 0
num_of_Li = 0
num_of_Tooley = 0

with open(path, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for candidatename in reader:
        if candidatename[2] == "Khan":
            num_of_Khan = (num_of_Khan + 1)
        elif candidatename[2] == "Correy":
            num_of_Correy = (num_of_Correy + 1)
        elif candidatename[2] == "Li":
            num_of_Li = (num_of_Li + 1)
        elif candidatename[2] == "O'Tooley":
            num_of_Tooley = (num_of_Tooley + 1)
 
perc_khan = round((num_of_Khan/num_of_voter)*100,3)
perc_correy = round((num_of_Correy/num_of_voter)*100,3)
perc_li = round((num_of_Li/num_of_voter)*100,2)
perc_tooley = round((num_of_Tooley/num_of_voter)*100,3)

print(f"The votes came down to Khan with {perc_khan}% of the vote, \nCorrey with {perc_correy}% of the vote, \nLi with {perc_li}% percent of the vote, \nand O'Tooley {perc_tooley}% of the vote.")

perc_votes = []

perc_votes.append(perc_khan)
perc_votes.append(perc_correy)
perc_votes.append(perc_li)
perc_votes.append(perc_tooley)

grouped_list = list(zip(unique_list,perc_votes))

for winner in grouped_list:
    if winner[1] == max(perc_votes):
        print(f"The winner of the election was {winner[0]} with {winner[1]}% of the vote!")

