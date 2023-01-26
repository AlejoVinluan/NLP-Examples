import sys
from classes.person import Person
from functions.text_processing import *

# Used to process the raw data from the CSV file.
#  This assumes that data is split into a list
#  Each cell of the list is a string seperated by commas
def process_data(raw_data):
    for line in raw_data:
        person = line.split(',')
        last_name = process_name(person[0])
        first_name = process_name(person[1])
        middle_initial = process_middle(person[2])
        person_id = process_id(person[3])
        phone_number = process_phone(person[4])
        
        
    

# Read the file given the file path
def read_file(filepath):
    # Try/Except block used in case the file is not found
    try:
        csv_obj = open(filepath, 'r')
        csv_data = csv_obj.read()
        # Split lines from 1 until the end of the file
        #  Used in order to ignore the first line of CSV
        raw_data = csv_data.splitlines()[1:]
        process_data(raw_data)
    except:
        print("Could not find file. Check spelling or file path.")
        exit()

    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a file name as a system argument.')
        exit()
    else:
        fp = sys.argv[1]
        read_file(fp)