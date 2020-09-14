# When given a list, calculate the "Running Average" for each item in the list and return a 
# list of averages rounded to the nearest integer
#Example: Calculate running averages for 
#test_list = [3,2,4]
#print (get_avg(test_list))
#[3, 4, 0]

from statistics import mean 
def get_avg(input_list):
    output_list = []
    l = len(input_list)
    n = 1
    while n < l:
        output_list.append(round(mean(input_list[n:])))
        n += 1
    else: # if n == l:
        output_list.append(0)
    return output_list