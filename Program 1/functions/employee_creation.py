from classes.person import Person
from functions.text_processing import *

# Used to process the raw data from the CSV file.
#  This assumes that data is split into a list
#  Each cell of the list is a string seperated by commas
def process_list(raw_data):
    employee_list = {}
    # Run this loop for every employee in the raw data
    for line in raw_data:
        # Split the original string based on a comma as a delimeter
        person = line.split(',')
        employee = Person()
        # Process each of the inputs provided
        employee.last_name = process_name(person[0])
        employee.first_name = process_name(person[1])
        employee.middle_initial = process_middle(person[2])
        employee.id = process_id(person[3])
        employee.phone = process_phone(person[4])
        # Add the employee to the employee list, with the ID as key
        employee_list[employee.id] = employee
    return employee_list