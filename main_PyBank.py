# Import modules os and csv
import csv
import os
# Set the path for the CSV file csvpath
csvpath = os.path.join("Resources","budget_data.csv")
# Create the lists,dictionaries and  variables as required to store data.
no_of_months = 0
greatest_increase = {"date": '',"net_change":0}
greatest_decrease = {"date": '',"net_change":9999999}
average = []
average_change = 0
net_total = 0
# Open the CSV using the set path csvpath
with open(csvpath) as budgetfile:
    reader = csv.reader(budgetfile,delimiter=",")
    header = next(reader)
    first_row = next(reader)
    no_of_months +=1
    net_total = net_total + int(first_row[1])
    # Initializing the 1st row to previous row 
    prv_row = int(first_row[1])
    for row in reader:
        # Calculate the no of months
        no_of_months +=1
        # Calculate the net total
        net_total = net_total + int(row[1])
        # Calculate the net change
        net_change = int(row[1]) - prv_row
        # Append the net change to average list for finding min and max profits
        average.append(net_change)
        # Resetting the previous row for initial value
        prv_row = int(row[1])
        # Find the max and min change in profits and the corresponding dates
        if net_change > greatest_increase["net_change"]:
            greatest_increase["date"] = row[0]
            greatest_increase["net_change"] = net_change
        if net_change < greatest_decrease["net_change"]:    
            greatest_decrease["date"] = row[0]
            greatest_decrease["net_change"] = net_change
    # Calculate the average change in profits        
    average_change =  sum(average)/len(average)
# Putting the result into output variable for printing on terminal    
output = (         
        "Financial Analysis \n"
        "-------------------------\n"   
        "Total Months: " + str(no_of_months) + "\n"
        "Total Profits: " + "$" + str(net_total) + "\n"
        f"Average Change: ${average_change:.2f}\n" 
        f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['net_change']})\n"
        f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['net_change']})\n"
        )   
print(output)
# Writing the output onto the budget analysis test file
with open('budget_analysis.txt', 'w') as outputfile:
    outputfile.write(output)



   


    