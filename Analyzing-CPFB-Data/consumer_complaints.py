import csv
import sys
import datetime as dt
from collections import Counter
import tempfile
import operator
import os

def just_year(input_date):
    strtime = dt.datetime.strptime(input_date, "%m/%d/%Y")
    return strtime.strftime("%Y")
	
def lower_case(input_text):
    return input_text.lower()
	
def add_quotes(input_str):
    if "," in input_str:
        return '"""'+input_str+'"""'
    else:
        return input_str       
		   
filename = sys.argv[1]
fileout = sys.argv[2]

# Use UTF-8 encoding which is default for Python 3, to open the input dataset csv file into a List of Lists. I am running this in Windows environment
with open(filename, encoding = "UTF-8")as file:
   lol = list(csv.reader(file))
# Remove the header
rows = lol[1:]
# Total number of rows or complaints
print (len(rows))
file.close()

# 1. Find total number of complaints received for each product and year. 
# When a product has a comma, the name should be enclosed by double quotation marks
outside_list_3 = []
outside_list_4 = []
for row in rows:
    product_lower = lower_case(row[1])	
    product = add_quotes(product_lower)    
    year_ = just_year(row[0])
    company = lower_case(row[7])
    
    prod_year_list = []
    prod_year_list.append(product)
    prod_year_list.append(year_)
    outside_list_3.append(prod_year_list)
	
    pyc_list = []
    pyc_list.append(product)
    pyc_list.append(year_)
    pyc_list.append(company)
    outside_list_4.append(pyc_list)

# Convert the List of Lists to a tuple List. 
# This is required to find the frequency of tuples
outside_tuple_list_py = [tuple(lst) for lst in outside_list_3]
freq_py = {}
for t in outside_tuple_list_py:
    if t in freq_py:
	    freq_py[t] += 1
    else:
        freq_py[t] = 1
print (freq_py, '\n')

# Write this dictionary of tuples to a temporary csv file
csvData = []
for (col1, col2), col3 in freq_py.items():
  csvData.append("%s, %s, %s" % (col1, col2, col3))
with tempfile.NamedTemporaryFile(suffix='.csv', prefix=('test'), dir='output', mode='w+', delete=False) as csvfile:
    csvfile.write("\n".join(csvData))
csvfile.close()

# 2. Find total number of companies receiving at least one complaint for that product and year
outside_tuple_list_pyc = [tuple(lst) for lst in outside_list_4]
#print (outside_tuple_list_pyc)
freq_comp = {}
for i in outside_tuple_list_pyc:
    if i[:2] not in freq_comp:
        freq_comp[i[:2]] = [i[2]]
    else:
        freq_comp[i[:2]].append(i[2])

# This dictionary gives List of all companies that received complaints for each product & year.
# A company will recur in this list if it received more than one complaint. 
# Form a dictionary of companies using this dictionary's keys i.e total complaints filed against a company for a 
# product and year. Highest value from list of values is the highest number of complaints
# a company	received for a product&year. This list is needed in step #3

high_list =[]
for py in freq_comp:
    z_dict = {}
    for comp in freq_comp[py]:
        if comp in z_dict:
            z_dict[comp] += 1
        else:
            z_dict[comp] = 1	
    #print (z_dict)
    complaint_list = []
    for complaint in z_dict:
        complaint_list.append(z_dict[complaint]) 
    #print (complaint_list)
    high_list.append(max(complaint_list))
print (high_list)	
# Remove duplicate companies so length of each list(of values for each key) is the total number of 
# companies that received atleast one complaint for that product&year. 
# The List of the values from this dictionary gives #2.

company_list = []
for key in freq_comp:
    freq_comp[key] = len(list(dict.fromkeys(freq_comp[key])))
    company_list.append(freq_comp[key])
#print (freq_comp)
# Append this to output csv
print (company_list)
print (len(company_list))

# 3. Find highest percentage (rounded to the nearest whole number) of total complaints filed against one company
# for that product and year. For this calculation, we use the list high_list and list of values from dictionary 
# freq_py which is the total number of complaints for each product&year.

py_list = []
for py in freq_py:
    py_list.append(freq_py[py])
print (py_list)

highest_percentage = []
for n in range(len(high_list)):
    percentage = round((high_list[n] / py_list[n])*100)
    highest_percentage.append(percentage)
# Append this to output csv
print (highest_percentage)
print (len(highest_percentage))

# Sorting by product (alphabetically) and year (ascending) which are the first 2 columns
# Open the existing csv in read mode and new temporary csv in write mode. Create a csv.reader object and a 
# csv.writer object from the input file object and output file object
# Add lists company_list and highest_percentage to existing csv file as columns
with open(csvfile.name, 'r') as read_f, \
    tempfile.NamedTemporaryFile(suffix='.csv', prefix=('inter'), dir='output', newline='', mode='w+', delete=False) as write_f:
    csv_reader = csv.reader(read_f)
    csv_writer = csv.writer(write_f)
    i = 0
    for row in csv_reader:
        # Append the new list values to that row/list 
        row.append(company_list[i])
        row.append(highest_percentage[i])
        # Add the updated row / list to the output file
        csv_writer.writerow(row)
        i += 1
# Use the temporary file to sort the data by first 2 columns and write to the final output csv file. 
# The newline='' parameter inside the open method is added so rows are not separated by a new line when code is run in Windows
# Finally, delete all the temp files.   
with open(write_f.name) as read_stuff, \
    open(fileout, 'w', newline='') as write_stuff:
    read_data = csv.reader(read_stuff)
    write_data = csv.writer(write_stuff)
    sortedlist = sorted(read_data, key=operator.itemgetter(0, 1))
    for row in sortedlist:
	    write_data.writerow(row)
write_f.close()
os.unlink(write_f.name)	
os.unlink(csvfile.name)	