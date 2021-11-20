## PYBANK ASSIGNMENT


# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path("budget_data.csv")

# Initialize variable to hold number of months
month = []
total_pl = 0
counter = 0
lag = 0
current = 0
pnl_changes = 0
ave_changes = 0

# Open the csv file as an object
with open(csvpath, 'r') as csvfile:
 # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

#The total number of months included in the dataset.
#The net total amount of Profit/Losses over the entire period.
#records.append(csv_header)
    month = 0
    total_pnl = 0
    delta = []
    prev_mth = 0
    delta_ave = 0
    max_up_month = 0
    max_up_date = ""
    max_down_month = 0
    max_down_date = ""
    sum_delta = 0
    len_delta = 0
     
    for row in csvreader:
        if row[0] == "Date":
            pass # do nothing
        elif row[0] == "Jan-2010":
            prev_mth = int(row[1])
            month = month +1
            total_pnl += int(row[1])
            max_up_month = 0
            max_up_date = row[0]
            max_down_month = 0
            max_down_date = row[0]
        elif row[0] == "Feb-2010":
            max_up_month = int(row[1]) - prev_mth
            max_up_date = row[0]
            max_down_month = int(row[1]) - prev_mth
            max_down_date = int(row[1])
            month = month + 1
            total_pnl += int(row[1])
            max_up_date = row[0]
#             delta.append(max_up_month)
            print(prev_mth)
            delta.append(int(row[1]) - prev_mth)
        else:
            month = month + 1
            total_pnl += int(row[1])
            delta.append(int(row[1])-prev_mth)
        if (int(row[1])-prev_mth) > max_up_month:
            max_up_month = int(row[1]) - prev_mth
            max_up_date = row[0]
            
        if (int(row[1])-prev_mth) < max_down_month:
            max_down_month = int(row[1]) - prev_mth
            max_down_date = row[0]
            
        prev_mth = int(row[1])    
#     ave_Delta = sum(delta)/len(delta)
  
#     sum_delta = sum(delta)
#     len_delta = len(delta)
#     delta_ave = (sum_delta-row[1])/(len_delta)
    
    ave_delta = (sum(delta)) / len(delta)
    print(f"Total Months: {month}")
    print(f"Total Profit & Losses is ${total_pnl}")
    print(f"Average delta is ${ave_delta}")
    print(f"Max Up Month ${max_up_month}")
    print(f"Max Up Date {max_up_date}")
    print(f"Max Down Month ${max_down_month}")
    print(f"Max Down Date {max_down_date}")
   

#Set the output header
header = ["Total Months", "Profit & Losses", "Average delta", "Max Up Month", "Max Up Date", "Max Down Month", "Max Down Date"]
# Create a list of metrics
metrics = [month, total_pnl, ave_delta, max_up_month, max_up_date, max_down_month, max_down_date]

# Set the output file path
output_path = Path('output.csv')

# Open the output path as a file object
with open(output_path, 'w') as csvfile:
    # Set the file object as a csvwriter object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    # Write the list of metrics to the output file
    csvwriter.writerow(metrics)