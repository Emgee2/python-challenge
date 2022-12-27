import os
import csv

#set the path to the csv file
csvpath = os.path.join('Resources','election_data.csv')

#open the csv file and read through the rows
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    #count for total number of votes cast
    #skip the header row
    header = next(reader)

    #variables
    count = 0
    candidate1_percentage_votes = 0
    candidate2_percentage_votes = 0
    candidate3_percentage_votes = 0
    candidate1_votes = 0
    candidate2_votes = 0
    candidate3_votes = 0

    total_votes = 0
    max_votes = 0
    candidate = ""
    winner = ""

    #candidates list
    candidate_list = {"Charles Casper Stockham":0,"Diana DeGette":0,"Raymon Anthony Doane":0}

    # loop through the rows in the csv file
    for row in reader:
        total_votes = sum(candidate_list.values())
        if count == 0:
            count += 1
            continue
        candidate_list.update({row[2]:candidate_list.get(row[2])+1})

    #average of votes each candidate
    candidate1_percentage_votes = candidate_list.get('Charles Casper Stockham')*100/total_votes
    candidate2_percentage_votes = candidate_list.get('Diana DeGette')*100/total_votes
    candidate3_percentage_votes = candidate_list.get('Raymon Anthony Doane')*100/total_votes

    #total number of votes each candidate won
    candidate1_votes = candidate_list.get('Charles Casper Stockham')
    candidate2_votes = candidate_list.get('Diana DeGette')
    candidate3_votes = candidate_list.get('Raymon Anthony Doane')

    for key, val in candidate_list.items(): #decide the winner
        if val > max_votes:
            max_votes = val
            winner = key
    #generate output summary
    output = (
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes:  {total_votes}\n"
        f"---------------------------\n"
        f"Charles Casper Stockham:  {candidate1_percentage_votes:2f}%,{candidate1_votes}\n"
        f"Dianan DeGette:  {candidate2_percentage_votes:2f}%,{candidate2_votes}\n"
        f"Raymon Anthony Doane:  {candidate3_percentage_votes:2f}%,{candidate3_votes}\n"
        f"-------------------------------\n"
        f"Winner: {winner}"
       )

#print the output(to terminal)
print(output)

#export the result to text file
file = 'Results.txt'
with open(file,"w") as txt_file:
    formatTxt = ()
    txt_file.write(output)