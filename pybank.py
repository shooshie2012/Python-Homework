
import os
import csv
	
csvpath = os.path.join('Resources' 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
	

	    # CSV reader specifies delimiter and variable that holds contents
	    csvreader = csv.reader(csvfile, delimiter=',')
	    next(csvreader, None)
	

	    #variables
	    months = []
	    profitlosses = []
	    pl_change = []
	

	

	    # count months and PnL
	    
	    for row in csvreader:
	        months.append(row[0])
	        profitlosses.append(int(row[1]))
	

	    #results total months and total PnL
	    print("Financial Analysis")
	    print("-----------------------------------")
	    print("Total Months:", len(months))
	    print("Total: $", sum(profitlosses))
	

	    # calc avg change; min and max PnL
	    for i in range(1,len(profitlosses)):
	        pl_change.append(profitlosses[i] - profitlosses[i-1])   
	        avg_pl_change= sum(pl_change)/len(pl_change)
	

	        max_pl_change = max(pl_change)
	

	        min_pl_change = min(pl_change)
	

	        max_pl_change_date = str(months[pl_change.index(max(pl_change))])
	        min_pl_change_date = str(months[pl_change.index(min(pl_change))])
	

	

	    print("Average Change: $", round(avg_pl_change))
	    print("Greatest Increase in Profits:", max_pl_change_date,"($", max_pl_change,")")
	    print("Greatest Decrease in Profits:", min_pl_change_date,"($", min_pl_change,")")
	

	

output_path = os.path.join('', 'pybank' + '.txt')
	
with open(output_path, 'w') as txt:
	

	    # Initialize csv.writer
	    csvwriter = csv.writer(txt, delimiter=',')
	

	    # Write the first row (column headers)
	    csvwriter.writerow(["Financial Analysis"])
	    csvwriter.writerow(["-----------------------------------"])
	    csvwriter.writerow(["Total Months:" , len(months)])
	    csvwriter.writerow(["Total: $" , sum(profitlosses)])
	    csvwriter.writerow(["Average Change: $" , round(avg_pl_change)])
	    csvwriter.writerow(["Greatest Increase in Profits:" , max_pl_change_date , "($" , max_pl_change , ")"])
	    csvwriter.writerow(["Greatest Decrease in Profits:" , min_pl_change_date , "($" , min_pl_change , ")"])
	
