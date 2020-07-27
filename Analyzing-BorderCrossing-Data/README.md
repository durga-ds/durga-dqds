# Border Crossing Data Analysis using Python

## Problem
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

The purpose of this project is to calculate 
-  the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. 
-  the running monthly average of total number of crossings for that type of crossing and border.


## Input dataset

The Border Crossing Entry dataset is `Border_Crossing_Entry_Data.csv`. It has has over 350K lines and is found at: 
https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2. Also found there will be notes from the Bureau of Transportation Statistics for more information on each field
For the purposes of this challenge, the following fields will be paid attention to:
*	Border: Designates what border was crossed
*	Date: Timestamp indicating month and year of crossing
*	Measure: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
*	Value: Number of crossings


## Output

The solution code will, after reading and processing the input file
*	Sum the total number of crossings (Value) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used.
*	Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of Border and Measure, or means of crossing.

It will then create an output file, `report.csv`

The output will be sorted in descending order by
•	Date
•	Value (or number of crossings)
•	Measure
•	Border

Example lines in `report.csv` will have the following format:
```
Border,Date,Measure,Value,Average
US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,114487
US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,0
US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,0
US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,172163,56810
US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,0
US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,0
```
The column, Average, is for the running monthly average of total crossings for that border and means of crossing in all previous months in the year. 
In this example, to calculate the Average for the first line (i.e., running monthly average of total pedestrians crossing the US-Mexico Border in all of the months preceding March), you'd take the average sum of total number of US-Mexico pedestrian crossings in February 156,891 + 15,272 = 172,163 and January 56,810, and round it to the nearest whole number round(228,973/2) = 114,487


## Approach and run instructions

The solution source code is written in python and is in file `border_analytics.py`

The repo includes a shell script named run.sh that runs the program that implements the required features.
The code is run by specifying `python` in the run.sh script. Any temporary files will get deleted by the program when it's done generating the report.csv file.

Before downloading the full dataset `Border_Crossing_Entry_Data.csv`, the code can be tested using a smaller input file called `sample-csv.csv`. The output report for that sample is generated to a file called `sample-report.csv`.
See the figure below for the structure of the repo.


    ├── README.md ( This file )
    ├── run.sh 
    ├── border_analytics.py
    ├── sample-csv.csv
    ├── sample-report.csv 
    ├── Temp location
        └── temp files ( will be deleted after analysis and report are done)


run.sh contains a line to execute on either sample data or the full data. Proper line needs to be uncommented based on whether the dataset being used is a smaller sample or the full dataset.
The input dataset and output csv report names are passed as arguments to the program to execute.
