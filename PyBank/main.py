#Task: Analyze financial records of your company. 
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (data and amount) over the entire period
#The greatest decrease in losses (data and amount) over the entire period

#Import os module
import os

#Variables
data = []
profitOrLosses = []
monthname = []

#Module for reading csv and path
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    total = 0
    months = 0
    #File has headers, we want to start on the next row.
    header = next(csvreader)
    
   #for row in csvreader:
            #print(row[0])
    #Use a For Loop to go down along rows
    for row in csv.reader(csvfile):
        #Append to data list the information on the second column.
        data.append(row[1])
        #Append month names to retrieve month data later.
        monthname.append(row[0])
        ##Convert the data list into integer and add it to calculate profit/loss 
        total = total + (int(row[1]))
        #total months
        months = months + 1
            
#Setup for reader of csv file and start a list of cell values for profitOrLosses
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #File has headers, we want to start on the next row.
    header = next(csvreader)
    
    #Zip 
    for firstNumber, secondNumber in zip(data, data[1:]):
        #File has headers, we want to start on the next row.
        header = next(csvreader)
        #Append the difference between the months
        profitOrLosses.append(int(secondNumber) - int(firstNumber))
        #sum for the total values
        total_change = sum(profitOrLosses)
        #average change, take one month because we cannot compare it to another value
        average = round((total_change / (months-1)),2)
        
#The greatest increase or decrease in profits for all the data
greatest_increase = max(profitOrLosses)
greatest_increase_month_index = profitOrLosses.index(greatest_increase)
result_greatest_increase_name = monthname[greatest_increase_month_index]
greatest_decrease = min(profitOrLosses)
greatest_decrease_month_index = profitOrLosses.index(greatest_decrease)
result_greatest_decrease_name = monthname[greatest_decrease_month_index]


#Test print of maths
print("Financial Analysis")
print("------------------------")
print("Total months: " + str(months))
print("Total volume: $" + str(total))
#The average change in "Profit/Losses" between months over the entire period
print("Average Change: "+ str(average))
#The greatest increase in profits (data and amount) over the entire period
print("Greatest Increase in Profits: " + str(result_greatest_increase_name) + " ($" + str(greatest_increase)  + ")")
#The greatest decrease in losses (data and amount) over the entire period
print("Greatest Decrease in Profits: " + str(result_greatest_decrease_name) + " ($" + str(greatest_decrease) + ")")

#Output to text file
text_file = open("PyBank_Results.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: $" + str(total) + "\n")
text_file.write("Average Change: " + str(average) + "\n")
text_file.write("Greatest Increase in Profits: " + str(result_greatest_increase_name) + " ($" + str(greatest_increase) + ")" + "\n")
text_file.write("Greatest Decrease in Profits: " + str(result_greatest_decrease_name) + " ($" + str(greatest_decrease) + ")" + "\n")
text_file.close()