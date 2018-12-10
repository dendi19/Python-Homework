import csv
import os
import sys


path = os.path.join('..', 'Instructions','PyBank', 'Resources', 'budget_data.csv')
print(path) #left out of text file due to irrelevance
sys.stdout = open('Financial_Outcome.txt','wt') # needed import sys for this function
num_month = 0 # for the math to create number of months
margins_by_month = []

with open(path, 'r') as f:
    reader = csv.reader(f)
    next(f) # skips header row
    for row in reader:
        num_month = (num_month+1)
        margins_by_month.append(float(row[1])) #goes through and adds one to each new row and ends with the months included
print(f"There were {num_month} months in this reporting period.")

total_margins = (sum(margins_by_month)) 
margin_change = 0 
margin_change_list = []
for margin in margins_by_month:            
    #print(f"the margin is {margin}")
    margin_change = margin - margin_change #uses margin as the current row and then subracts the margin prior to it
    margin_change_list.append(margin_change) #adds the difference between the two numbers to a list
    #print(f"The change is {margin_change}")
    margin_change = margin #changes last margin to new one for math in row 25

standard_list = []

with open(path, 'r') as f:
    reader = csv.reader(f)
    next(f)
    for info in reader:
        standard_list.append(info[0]) #adds months into list for zipping
grouped_list = list(zip(standard_list, margin_change_list)) #combines the two lists, the 'list' at the beginning shows the whole text since python naturally stores zip in a non-visible format

for valuelist in grouped_list:
    if valuelist[1] == max(margin_change_list): #compares max from list earlier with the value in second column
        print(f"The max margin of growht was {valuelist[0]} with a growth of ${valuelist[1]}")
for valuelist in grouped_list:    
    if valuelist[1] == min(margin_change_list): # same as row 40 but for min
        print(f"The lowest margin of growth was {valuelist[0]} with a decline of ${valuelist[1]}")
total_marg_change = round(((sum(margin_change_list)-867884 )/num_month+1),2) # I couldn't get any skip functions to exclude the first value so there was an extra -867884 in the list


print(f"The average margin of change across the {num_month} months was ${total_marg_change}.")
print(f"The net profit/loss was ${total_margins}.")
