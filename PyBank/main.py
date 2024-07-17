import csv
csvpath = '/Users/katchu/Desktop/Data Analysis Bootcamp/Module 3 Starter_Code/PyBank/Resources/budget_data.csv'

total_months=0 #defines rows of total_months 
net_total= 0 #defines the net total
previous_profit_loss = 0
total_change = 0
changes = []
dates = []

def calculate_profit_loss(row):
    return int(row[1])


with open(csvpath, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader: #basically goes through the row...
        total_months += 1 #counts the number of months or rows in the column
        print(row) #idk if this stays here or not 
        current_profit_loss = calculate_profit_loss(row) #it keeps saying the this is not defined?? 
        net_total += current_profit_loss #adds the numbers up in row 1, or column 2
        dates.append(row[0])
    
        if total_months > 1: #starts calculating from the second month           
            change = current_profit_loss - previous_profit_loss # type: ignore
            total_change += change #adds each monthly profit/loss to the toal change
            changes.append(change) #adds these values to changes list
        previous_profit_loss = current_profit_loss # type: ignore #updates previous_profit_loss for the correct calculations as the loop continues 
    average_change = total_change / (total_months - 1)
    #calculate average change #total_months - 1, since we started at month 2

increase_amount = max(changes)
increase_index = changes.index(increase_amount)
increase_date = dates[increase_index + 1] #gotta adjust because we started calculations in month 2

decrease_amount = min(changes)
decrease_index = changes.index(decrease_amount)
decrease_date = dates[decrease_index+1] 

print("Financial Analysis")
print("---------------------")
print(f"Total Number of Months: {total_months}")
print(f"Net Profit and Losses: ${net_total}")
print(f"Average change: ${average_change:.2f}") #give it two decimal places after the decimal point (f)
print(f"Greatest Increase in Profits: {increase_date} (${increase_amount})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount})")