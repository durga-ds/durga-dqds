# Analyze consumer complaints using CFPB Consumer Complaint Dataset

## Problem
CFPB provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This project will identify the number of complaints filed and how they're spread across different companies. 

The purpose of this project is to find for each financial product and year
-  total number of complaints
-  number of companies receiving atleast one complaint and 
-  highest percentage of complaints directed at a single company


## Input dataset
The input file is CFPB dataset called complaints.csv and contains over 1.5 million records that can be found zipped at:http://files.consumerfinance.gov/ccdb/complaints.csv.zip. The code will read that input file, process it and write the results to an output file, `report.csv` that is placed in the same directory.
(See here for more information on the data dictionary: https://cfpb.github.io/api/ccdb/fields.html)
All names, including company and product, will be treated as case insensitive. For example, "Acme", "ACME", and "acme" would represent the same company.

## Output

After reading and processing the input file, the solution code will create an output file, `report.csv`, with as many lines as unique pairs of product and year (of `Date received`) in the input file. 

Each line in the output file will list the following fields in the following order:
* product (name in all lowercase)
* year (in YYYY format)
* total number of complaints received for that product and year
* total number of companies receiving at least one complaint for that product and year
* highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Any percentage between 0.5% and 1%, inclusive, would be rounded to 1% and anything less than 0.5% to 0%)

The lines in the output csv file will also be sorted by product (alphabetically) and year (ascending)

Example lines in `report.csv` will have the following format:
```
"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100
```
When a product has a comma (`,`) in the name, the name will be enclosed by double quotation marks (`"`). 
Finally, percentages are listed as numbers and do not have `%` in them.

## Approach and run instructions

The solution source code is written in python and is in file `consumer_complaints.py`

The repo includes a shell script named run.sh that runs the program that implements the required features.
The code is using `python3.8` and is run by specifying `python3` in the run.sh script. The folder `output` is for temporary files that will get deleted by the program when it's done generating the report.csv file.

Before downloading the full CFPB dataset `complaints.csv`, the code can be tested using a smaller input file called `sample-complaints.csv`. The output report for that sample is generated to a file called `myreport.csv`.
See the figure below for the structure the repo.


    ├── README.md
    ├── run.sh
    ├── consumer_complaints.py
    ├── sample-complaints.csv
    ├── myreport.csv 
    ├── output
        └── temp files 


run.sh contains a line to execute this test. Proper line needs to be uncommented based on whether the dataset being used is smaller sample or the full dataset.

