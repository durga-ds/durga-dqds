#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python 3
# python consumer_complaints.py complaints.csv report.csv

# Run the code on sample dataset(argument 1)`sample-complaints.csv` and generate output(argument 2) into `myreport.csv`
python3 consumer_complaints.py sample-complaints.csv myreport.csv

# Run the code on full CFPB dataset `complaints.csv` and generate output (argument 2) into 'report.csv' 
# If you face error `ValueError("time data m/d/Y does not match format %r" %`, do as follows in function `just_year`:
# def just_year(input_date):
#     strtime = dt.datetime.strptime(input_date, "%m/%d/%Y")
#     #strtime = dt.datetime.strptime(input_date, "%Y-%m-%d")
#     return strtime.strftime("%Y")```
#python3 consumer_complaints.py complaints.csv report.csv