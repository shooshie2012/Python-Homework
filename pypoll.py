#import the data
import os
#read the csv file
import csv
#set file path
csvpath= os.path.join('Resources', 'election_data.csv')
#CSV reader specifies delimier and variable holds the contents
with open(csvpath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #variables
        candidates = []
        totalcount= []
        votes = 0

        #skip header
        next(csvreader, None)

        #votes
        for line in csvreader:

        #add to number of votes
            votes = votes + 1

        #candidate
            candidate = line[2]

        #total candidate votes
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            totalcount[candidate_index] = totalcount[candidate_index] + 1
        
        else:
            candidate.append(candidate)
            totalcount.append(1)
percentage = []
totalvotes = totalcount [0]
results = 0
        #percentage of vote and winners
for count in range (len(candidates)):
            vote_percentage = totalcount[count]/votes*100
            percentage.append(vote_percentage)
            if totalcount [count] > totalvotes:
                totalvotes = totalcount[count]
                print(totalvotes)
                results = count
winner = candidates [results]

#print
print ("Election Results")
print ("-----------------------------------")
print(f"Total Votes: {votes}")
for count in range (len(candidates)):
            print(f"{candidate [count]}: {round(percentage[count])}% {totalcount[count]}")
print ("-----------------------------------")
print(f"Winner: {winner}")
print ("-----------------------------------")

output_path = os.path.join('', 'pypoll' + '.txt')

#open file 
with open(output_path,'w') as txt:
    csvwriter = csv.writer(txt, delimiter=',')

    #make column headers
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {votes}"])
    csvwriter.writerow(["----------------------------"])
    for count in range(len(candidates)):
        csvwriter.writerow([f"{candidates[count]}: {round(percentage[count])}% ({totalcount[count]})"])
    csvwriter.writerow(["----------------------------"])   
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------"])   
