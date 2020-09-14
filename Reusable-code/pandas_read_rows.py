#Function to read given a csv file, using default encoding and print the specified number of lines from the DataFrame.
#Example: pdread_csv(csvfile_name, 5) 

import pandas as pd
def pdread_csv(csvfile, numrows, enc='ISO-8859-1'):
    rows = pd.read_csv(csvfile, nrows=numrows, encoding=enc)
    return rows