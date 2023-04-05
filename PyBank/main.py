#import modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
#To export the results to a text file
output_file = 'Results.txt'

#Set the variables
column_sum = 0
diffs = []
greatest_increase = float('-inf')
month_greatest_increase = None
greatest_decrease = float('inf')
month_greatest_decrease = None

#Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the Header
    csv_header = next(csvreader)
    
    # Calculate Total Months
    csv_data = list(csvreader)
    no_months = len(csv_data)
 
    #Define the variable that will be used in the loop to calculate the changes in "Profit/Losses" 
    prev_revenue = int(csv_data[0][1])  
  
    #Loop through all the rows
    for row in csv_data:
        #Calculate the net total amount of "Profit/Losses" over the entire period
        column_sum = column_sum + int(row[1])

        #Calculate the changes in "Profit/Losses" over the entire period
        revenue_diff = int(row[1]) - prev_revenue
        diffs.append(revenue_diff)
        prev_revenue = int(row[1])

        #Calculate the greatest increase and decrease in profits over the entire period
        row_values = diffs
        increase_max = max(row_values)
        increase_min = min(row_values)
        
        if increase_max > greatest_increase:
            greatest_increase = increase_max
            month_greatest_increase = row[0]
        
        if increase_min < greatest_decrease:
            greatest_decrease = increase_min
            month_greatest_decrease = row[0]

#Printing the final solution in the Terminal:  
    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {no_months}")
    print(f"Total: $ {column_sum}")

#Calculate the average of the changes in "Profit/Losses" over the entire period 
#Notice that considering the first month does not have any previous value to be compared to, it is dropped from the Total Amount of Months by subtracting -1 to No_months:
    revenue_average = round(((sum(diffs))/(no_months-1)),2)
    print(f"Average Change: $ {revenue_average}")
    
    print(f"Greatest Increase in Profits: {month_greatest_increase} (${increase_max})")
    print(f"Greatest Decrease in Profits: {month_greatest_decrease} (${increase_min})")

#Export a text file with the results:
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write("Total Months: %d\n" % no_months)
    file.write("Total: $%d\n" % column_sum)
    file.write("Average Change: $%s\n" % revenue_average)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (month_greatest_increase, increase_max))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (month_greatest_decrease, increase_min))


       
