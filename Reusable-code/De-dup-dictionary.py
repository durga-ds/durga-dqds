#Remove duplicate values from a python dictionary, where the key values are in a List. 
#It will return the dictionary where each key value is a list of only unique values
#Example:
#test_dict = {'a':[1,2,2,3,3,4,1], 'b':[100,100,100]}
#dedup_dictionary(test_dict)
#Output: {'a': [1, 2, 3, 4], 'b': [100]}

def dedup_dictionary(dict_name):
    for key in dict_name:
        dict_name[key] = list(dict.fromkeys(dict_name[key]))
    return dict_name
