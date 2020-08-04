#import modules
import os
import csv
import statistics

#output results to txt file
output_file = os.path.join ('Analysis', 'budget_results.txt')
    
#set csv file path being read
file_path = os.path.join ('Resources', 'budget_data.csv')
with open(file_path, "r") as csvFile:
#Create csv reader
    csv_reader = csv.reader(csvFile, delimiter=',')
    #remove header
    next(csv_reader)
    #create variables for sum of month
    data = list(csv_reader)
    sum_month = len(data)
    #create variable for total profit/loss
    pltotal = []
    for row in data:
        pltotal.append(float(row[1]))
    final_pltotal = sum(pltotal)
    #final_pltotal = sum(pltotal2)
    #create variables for monthly change
    monthly_change = []
    previous_month = 0.00
    current_month = 0.00
    for i in range(1,len(pltotal)):
        monthly_change.append(pltotal[i] - pltotal[i-1])
        avg_change = sum(monthly_change)/len(monthly_change)
    #for row in data:
        #avg_change = row[1]
        #monthly_change.append(current_month - previous_month)
#print total months
print("Financial Analysis\n\nTotal Months: " + f'{sum_month}')
#print total profit/loss
print("Total: " + f'${final_pltotal}'.rstrip('.0'))
print(f'${avg_change}')
#---------------------------------------------------------------------------
#set file pate using write mode
with open(output_file, 'w') as txtFile:
    #output results to .txt file
    txtFile.write("Financial Analysis\n---------------------------------\nTotal Months: "+ f'{sum_month}'"\nTotal: " + f'${final_pltotal}'.rstrip('.0'))
