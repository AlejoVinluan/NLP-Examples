import sys
import os
from functions import cleanData, getLexicalDiversity

class Main:
    if len(sys.argv) <= 1:
        print("Wrong number of arguments. Please run by using python3 Main <file_name.txt>")
        exit(1)
    
    text = ""
        
    print(os.getcwd())
    print(os.listdir('.'))
        
    try:
        f = open(sys.argv[1], 'r')
        raw_data = f.readlines()
        text = cleanData(raw_data)
    except:
        print("Unable to find file", sys.argv[1])
        exit(1)
    
    print(text)