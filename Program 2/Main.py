import sys
from functions import clean_data, get_lexical_diversity

class Main:
    if len(sys.argv) <= 1:
        print("Wrong number of arguments. Please run by using python3 Main <file_name.txt>")
        exit(1)
    
    text_arr = []
                
    try:
        raw_data = open(sys.argv[1], 'r')
        data_arr = raw_data.readlines()
        text_arr = clean_data(data_arr)
    except:
        print("Unable to find file", sys.argv[1])
        exit(1)
    
    print(text_arr)
    print(get_lexical_diversity(text_arr))
    