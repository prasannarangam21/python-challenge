# Import modules os and csv
import csv
import os
# Set the path for the CSV file csvpath
csvpath = os.path.join("Resources","election_data.csv")
# Create the lists , dictionaries and variables as required to store data.
total_votes = 0
candidate_list = []
candidate_votes = {}
winning_votes = 0
# Open the CSV using the set path csvpath
with open(csvpath) as electionfile:
    reader = csv.reader(electionfile,delimiter=",")
    header = next(reader)
    for row in reader:
        # This is the total votes cast
        total_votes +=1
        name = row[2]
        # cheking and appending then candidate names to candidate list and getting the vote count
        if name not in candidate_list:
            candidate_list.append(name)
            candidate_votes[name] = 0
        candidate_votes[name]+=1
# writing to output file and terminal          
with open('election_analysis.txt', 'w') as outputfile:
    output = (
                "Election Results    \n"
                "---------------------------\n"
                f"Total Votes:  {str(total_votes)}\n" 
                "---------------------------\n"
             )    
    print(output)
    outputfile.write(output)
    # calculating total no of votes for each candidate and their percentage
    for candidate_name in candidate_votes:
        x = candidate_votes[candidate_name]
        # to get the float value for percentage
        p = float(x)/float(total_votes)*100
        candidate_output = f"{candidate_name}: {p:.3f}% ({x})\n"
        outputfile.write(candidate_output)
        print(candidate_output)
        if x > winning_votes:
            winning_votes = x
            winning_candidate = candidate_name
    winner_output = ( "---------------------------\n"
                      f"Winner: {winning_candidate}\n"  
                      "---------------------------\n") 
    print(winner_output) 
    outputfile.write(winner_output)                   

     
      

        
            
            
            

    

