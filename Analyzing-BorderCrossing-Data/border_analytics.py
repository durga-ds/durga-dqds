import csv
import sys
import datetime as dt
from collections import Counter
import tempfile
import operator
import os
from statistics import mean 

# A function that takes a date and returns just the month
def get_m(input_date):
    #strtime = dt.datetime.strptime(input_date, "%m/%d/%Y %H:%M")
    strtime = dt.datetime.strptime(input_date, "%m/%d/%Y")
    return strtime.strftime("%m")

# A function that takes a date and returns just the Year
def get_Y(input_date):
    #strtime = dt.datetime.strptime(input_date, "%m/%d/%Y %H:%M")
    strtime = dt.datetime.strptime(input_date, "%m/%d/%Y")
    return strtime.strftime("%Y")

# A function that takes a date and returns in a format required for the output file; with AM/PM
def output_format(input_date):
    strtime = dt.datetime.strptime(input_date, "%m%Y")
    return strtime.strftime("%m/%d/%Y %I:%M:%S %p")
	
# A function that will when given a list, calculate a "running average" for each item in the list and return the 
# list of averages rounded to the nearest whole number
#For example: Calculate running averages for [1,2,3]
#For 1 = (2+3)/2 = 2.5
#For 2 = 3
#For 3 = 0
#Return list: [3, 3, 0]
def get_avg(input_list):
    output_list = []
    l = len(input_list)
    n = 1
    while n < l:
        output_list.append(round(mean(input_list[n:])))
        n += 1
    else: # if n == l:
        output_item = 0
        output_list.append(output_item)
    return output_list
	
# A function that creates a single list out of a list of lists
def single_list(list_nest):
    return [item for sublist in list_nest for item in sublist]

# These argument values are passed within the script run.sh that executes this program	
filename = sys.argv[1]
fileout = sys.argv[2]

# Use UTF-8 encoding to open the input dataset into a List of Lists `lol`
with open(filename, encoding = "UTF-8")as file:
   lol = list(csv.reader(file))
header = lol[0]
print ( header )
# Remove the header
rows = lol[1:]
# Total number of lines in the dataset
print (len(rows))
# Print a few rows to get familiar with the data
for i in range(6):
   print ( rows[i] ) 
file.close()

#1.Sum up the total number of crossings for each month. For this, separate the Year and month for making it convenient for analysis.
# Since time of day is not consequential to our data analysis, below, we are looking at just the date in the format `3/1/2019` to grab
# the year and month from. 
step1_list = []
for row in rows:
    run_avg_list = []
    run_avg_list.append(row[3])
    run_avg_list.append(row[5])
    run_avg_list.append(get_Y((row[4].split())[0]))
    run_avg_list.append(get_m((row[4].split())[0]))
    run_avg_list.append(int(row[6]))
    step1_list.append(run_avg_list)

print (len(step1_list))

# Convert the List of Lists into a List of tuples. Then, create a dictionary for summed up values - they belong to the 
# same combo of Border, Measure, Year and month.
tuple_list_step2 = [tuple(lst) for lst in step1_list]
s_vals = {}
for tup in tuple_list_step2:
    if tup[:4] not in s_vals:
        s_vals[tup[:4]] = tup[4]
    else:
        s_vals[tup[:4]] += tup[4]

print (len(s_vals))

# There may be several months in the same year when Crossings happen. Let's see if any year has crossings 
# for more than one month and what the crossings values are for each month.
# This changes the order of keys from the last dictionary as we are grouping values by year.
# This is a useful view for the second analysis - calculating the running monthly average ( for each year ) of total crossings.

step2_months = {}
step2_vals = {}
for tup in s_vals:
    if tup[:3] in step2_months:
        step2_months[tup[:3]].append(tup[3])
        step2_vals[tup[:3]].append(s_vals[tup])
    else:
        step2_months[tup[:3]] = [tup[3]]
        step2_vals[tup[:3]] = [s_vals[tup]]
        
print (step2_months,'\n')
print (step2_vals,'\n')

# Create a list of tuples with 1. Border 2. Date(by combining Year and month) and 3. Measure
# This will be unpacked using list comprehension.
list_my = [(key, month) for key in step2_months for month in step2_months[key]]
#print (list_my)
res = [(a, output_format(d+c), b) for (a, b, c), d in list_my]   
print (res)

# Get a list of all crossings values from the dictionary step2_vals.
vals = list(step2_vals.values())
#print (vals)
vals_flatlist =  single_list(vals)
#print (vals_flatlist)

# Calculate the list of "running average" values for each item in list 'vals'.
avg_list = []
for each_list in vals:
    avg_list.append(get_avg(each_list))
#print (avg_list)
avg_flatlist =  single_list(avg_list)
#print (avg_flatlist)

# Combine the List of Lists `vals` and `avg_list` to produce a list of tuples containing Crossings value for a month 
# in a year and its running average.
tup_dictionary_vals = []
for a, b in zip(vals, avg_list):
    tup_dictionary_vals.append(list(zip(a,b)))
#print (tup_dictionary_vals)
vals_avg_list =  single_list(tup_dictionary_vals)
print (vals_avg_list)

# Create a single dictionary using `vals_avg_list` as values and `res` as keys.
# Write this dictionary of tuples to a temporary csv file. Each key,value pair will be written to the file as a separate row
tup_dictionary = dict(zip(res, vals_avg_list))
print(tup_dictionary)
final_data = []
for (col1, col2, col3), (col4, col5) in tup_dictionary.items():
    final_data.append("%s, %s, %s, %s, %s" % (col1, col2, col3, col4, col5))
with tempfile.NamedTemporaryFile(suffix='.csv', prefix=('finaldata'), mode='w+', delete=False) as sometmp:
    sometmp.write("\n".join(final_data))
sometmp.close()
#The lines need to be sorted in descending order by
# - Date
# - Value (or number of crossings)
# - Measure
# - Border
# The temporary csv file will be used to sort the data by the said columns and written to another temp file to finally add
# a header row and create the final report.
# All interim temp csv files will be deleted
with open(sometmp.name) as read_stuff, \
    tempfile.NamedTemporaryFile(suffix='.csv', prefix=('srted'), newline='', mode='w+', delete=False) as write_stuff:
    read_data = csv.reader(read_stuff)
    write_data = csv.writer(write_stuff)
    sortedlist2 = sorted(read_data, key=operator.itemgetter(1,3,2,0),reverse=True)
    print(sortedlist2)
    for row in sortedlist2:
        write_data.writerow(row)
		
header_list = ['Border', 'Date', 'Measure', 'Value', 'Average']
with open(write_stuff.name) as read_stuff, \
    open(fileout, 'w', newline='') as result:
    rdr = csv.DictReader(read_stuff, fieldnames=header_list)
    wrtr = csv.DictWriter(result, header_list)
    wrtr.writeheader()
    for line in rdr:
        wrtr.writerow(line)				
sometmp.close()
write_stuff.close()
os.unlink(sometmp.name)
os.unlink(write_stuff.name)