#Import Dependencies
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..','Resources','budet_data.csv')

# count no of rows in csv file for no of months.
#Create Variables

total_net_value = 0
row_count = 1
greatest_increase = ["", 0]
Greatest_decrease = ["", 999999999999999999999999999999]

# open CSV files

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #row_count = sum(1 for row in csv_file)
    # to reduce header row count
    header = next(csv_reader)
    first_row = next(csv_reader)
    prev_net = int(first_row[1])

    total_net_value = total_net_value + int(first_row[1]) 
    
    #Create For loop to read the all rows
   
    for row in csv_reader:
        sumOfBudgetValue = 0
        total_net_value = total_net_value + int(row[1]) 
        row_count = row_count + 1
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])

        if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change

        if net_change < Greatest_decrease[1]:
           Greatest_decrease[0] = row[0]
           Greatest_decrease[1] = net_change

# Print out results

print ("Financial Analysis")
print ("--------------------------------------------------------------")
print(f"Total Months: {row_count}")
print (f"Total: {total_net_value}")
print (f"Average Change: {net_change}")
print (f"Greatest Increase in profits: {greatest_increase[0]} {greatest_increase[1]}")
print (f"Greatest Decrease in profits: {Greatest_decrease[0]} {Greatest_decrease[1]}")         


# to print to a output txt file 
with open('output.txt','a')as txtfile:
    txtfile.write("\nFinancial Analysis")  
    txtfile.write("\n--------------------------------------------------------------")
    txtfile.write("\nTotal Months     :")
    txtfile.write(str(row_count))
    txtfile.write("\nTotal Net Value  :")
    txtfile.write(str(total_net_value) )
    txtfile.write("\nAverage Change   :")
    txtfile.write(str(net_change))
    txtfile.write("\nGreatest Increase in profits:")
    txtfile.write(str(greatest_increase[0]))
    txtfile.write( str(greatest_increase[1]))
    txtfile.write("\nGreatest Decrease in profits: ")
    txtfile.write(str(Greatest_decrease[0]))
    txtfile.write(str(Greatest_decrease[1]))
    txtfile.write("\n--------------------------------------------------------------")
txtfile.close()


