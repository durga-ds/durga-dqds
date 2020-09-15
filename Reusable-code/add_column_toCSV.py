# Python function to add a list of values as a new column to an existing CSV file and write desired result to an output file
#Example: Add values from [4,4,5,5,9,9,9] as a new column to `example_csv.csv`. Output to file `new_col.csv`
#col_list = [4,4,5,5,9,9,9]
#add_col_to_csv('example_csv.csv','new_col.csv',col_list)

import csv

def add_col_to_csv(csvfile,fileout,new_list):
    with open(csvfile, 'r') as read_f, \
        open(fileout, 'w', newline='') as write_f:
        csv_reader = csv.reader(read_f)
        csv_writer = csv.writer(write_f)
        i = 0
        for row in csv_reader:
            row.append(new_list[i])
            csv_writer.writerow(row)
            i += 1 