#import libraries
import os
import csv

#Path to csv file
budget_csv = '../PyBank/Resources/budget_data.csv'

#Declare variables
total_months = []
total_profit = []
monthly_profit_change = []

#Open/read csv file
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

     # Iterate through the rows 
    for row in csv_reader: 

        # Append the total months and total profit 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits 
    for i in range(len(total_profit)-1):
        
        # Take the difference 
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

with open('result.txt', 'w') as txtfile:
    print("Financial Analysis", file=txtfile)
    print("----------------------------", file=txtfile)
    print(f"Total Months: {len(total_months)}", file=txtfile)
    print(f"Total: ${sum(total_profit)}", file=txtfile)
    print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}", file=txtfile)
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})", file=txtfile)
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})", file=txtfile)  
   





    


    