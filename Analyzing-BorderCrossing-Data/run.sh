#!/bin/bash
#
# Use this shell script to compile (if necessary) your Python code and then execute it.

# Uncomment this line for creating a report on the full dataset 
python border_analytics.py Border_Crossing_Entry_Data.csv report.csv

# Uncomment this line for creating a sample report on the sample dataset
#python border_analytics.py sample-csv.csv sample-report.csv
