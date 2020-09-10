#Calculate the total memory footprint of a dataset in MB, when processing in chunks of specific number of rows at a time
#from a CSV file.
#Example: total_mem('filename.csv', 500)
#Note: Change file encoding as needed 

import pandas as pd
def total_mem(csvfile, numrows, enc='ISO-8859-1'):
    total_memory_footprint = 0
    for chunk in pd.read_csv(csvfile, chunksize=numrows, encoding=enc):
        total_memory_footprint += chunk.memory_usage(deep=True).sum()/1024**2
    return total_memory_footprint