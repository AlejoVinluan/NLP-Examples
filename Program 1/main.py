import sys
import pickle
from classes.person import Person
from functions.employee_creation import process_list

# Saves the list as a Pickle file then opens it and reads it.
def save_and_read(employee_dict):
    pickle.dump(employee_dict, open('employee_file.p', 'wb'))
    employee_pickle_list = pickle.load(open('employee_file.p', 'rb'))
    print("Employee list:")
    for employee in employee_pickle_list:
        employee_pickle_list[employee].display()
    exit(0)
    
# Used to process the raw data from the CSV file.
#  This assumes that data is split into a list
#  Each cell of the list is a string seperated by commas
def process_data(raw_data):
    employee_list = process_list(raw_data)
    save_and_read(employee_list)

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
    except FileNotFoundError:
        print("Could not find file. Check spelling or file path.")
        exit(1)
    # Except block used in case program quits
    #  Example: User uses CTRL+C to quit the program
    except:
        print("Program exited unexpectedly.")
        exit(1)

# This runs once program is run
if __name__ == '__main__':
    # Check that there are at least 2 arguments provided
    #  Exits if there is no argument provided.
    if len(sys.argv) < 2:
        print('Please enter a file name as a system argument.')
        exit(1)
    # Attempts to read file if argument is found
    else:
        fp = sys.argv[1]
        read_file(fp)