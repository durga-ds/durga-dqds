#Find file encoding value, given a csv file
#It's not good to leave encoding to guess work. This function uses chardet module to determine the encoding of a file. 
#Example: print (find_encoding(csvfilename))
#However, chardet may not be 100% reliable
#Chances are encoding is usually one of UTF-8, Latin-1 or Windows-1251

import chardet
def find_encoding(filename):
    with open(filename, mode='rb')as f:
        raw_bytes = f.read(128)   
        encoding_name = (chardet.detect(raw_bytes))['encoding']
    return encoding_name
