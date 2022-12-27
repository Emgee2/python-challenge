import os
import csv

#set the path to the csv file
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv file and read through the rows
with open(csvpath) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    #counter for the total of the months
    #skip the header row
    header = next(reader)

    #variables
    count = 0
    total = 0
    average = 0
    current = 0
    highprofit = 0
    highloss = 0
    profitlossdate = ""
    lossdate = ""

    #iterate through the row of the csv file
    for row in reader:
        total += int(row[1])
        count += 1
        current = int(row[1])
        if(current>= 0): #decide of profit or loss
            if(current > highprofit): #store highest profit date
                highprofit = current
                profitdate = str(row[0])
        elif(current< 0):
            if(current < highloss): #store worst loss ever
                highloss = current
                lossdate = str(row[0])
    average = total / count  #average profit over x months

    #generate output summary
    output = (
        f"Financial Analysis\n"
        f"--------------------------\n"
        f"Total Months: {count}\n"
        f"Total: {total}\n"
        f"Average Change: ${average:2f}\n"
        f"Greatest Increase in Profits: {profitdate}  ${highprofit}\n"
        f"Greatest Decrease in Profits: {lossdate}   ${highloss}"
    )

#print the output(to terminal)
print(output)
#export the result to text file
file = 'Analysis.txt'
with open(file,"w") as txt_file:
    formatTxt = ()
    txt_file.write(output)