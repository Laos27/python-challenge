#import modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
print(csvpath)
#To export the results to a text file
output_file = os.path.join("analysis", "Results.txt")

#Set the variables
column_count = 0
list_candidates = []
final_results =[]
final_votes = []
final_percentage = []

#Open the CSV
with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        #Skip the Header
        csv_header = next(csvreader)

        #Print the final solution header in the Terminal:  
        print("Election Results")
        print("--------------------------------")        
          

        #Calculate Total Votes
        csv_data = list(csvreader)
        no_votes = len(csv_data)
        print(f"Total Votes: {no_votes}")
        print("--------------------------------")   
           
        #Set Variables to find List of Candidates and No. of Votes
        unique_counts = {}
        max_votes = 0
        
        #Loop to find total number of Votes of each Candidate:
        for row in csv_data:
                value = row[2]
                if value not in unique_counts:
                        unique_counts[value] = 1
                        
                else:
                        unique_counts[value] +=1
              
                #Conditional to find the max Number of Votes:
                if unique_counts[value] > max_votes:
                        max_votes = unique_counts[value]

#Loop to store the total Number of Votes of each Candidate and the %:
for value, count in unique_counts.items():
        candidate = (value)
        votes = (count)
        percentage = round(((count/no_votes)*100),3)

        #Print all results within the loop and send them to the Terminal:
        print(f"{candidate}: {percentage}% ({votes})")
        
        #Set the Lists
        list_candidates.append(candidate)
        final_votes.append(votes)
        final_percentage.append(percentage)
        
        #Conditional to find which candidate was the Winner:
        if count == max_votes:
                winner = (value)
        
     
print("--------------------------------")
print(f"Winner: {winner}")
print("--------------------------------")

#Export a text file with the results:
with open(output_file, 'w') as file:
        file.write("Election Results\n")
        file.write("---------------------------\n")
        file.write("Total Votes: %d\n" % no_votes)
        file.write("---------------------------\n")
        for i in range(len(list_candidates)):
                file.write("%s: %.3f%% (%d)\n" % (list_candidates[i], float(final_percentage[i]), (final_votes[i])))
        file.write("---------------------------\n")    
        file.write("Winner: %s\n" % winner)
        file.write("---------------------------\n")

    


        
       
        
        
        