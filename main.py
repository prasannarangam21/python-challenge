import csv
import os

csvpath = os.path.join("Resources","budget_data.csv")
no_of_months = 0
greatest_increase = {"date": '',"net_change":0}
greatest_decrease = {"date": '',"net_change":9999999}
average = []
average_change = 0
net_total = 0
with open(csvpath) as budgetfile:
    reader = csv.reader(budgetfile,delimiter=",")
    header = next(reader)
    first_row = next(reader)
    no_of_months +=1
    net_total = net_total + int(first_row[1])
    prv_row = int(first_row[1])
    for row in reader:
        no_of_months +=1
        net_total = net_total + int(row[1])
        net_change = int(row[1]) - prv_row
        average.append(net_change)
        prv_row = int(row[1])
        if net_change > greatest_increase["net_change"]:
            greatest_increase["date"] = row[0]
            greatest_increase["net_change"] = net_change
        if net_change < greatest_decrease["net_change"]:    
            greatest_decrease["date"] = row[0]
            greatest_decrease["net_change"] = net_change
    average_change =  sum(average)/len(average)
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

with open('budget_analysis.txt', 'w') as outputfile:
    outputfile.write(output)



   


    