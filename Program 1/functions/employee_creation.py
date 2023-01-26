from classes.person import Person
from functions.text_processing import *

# Used to process the raw data from the CSV file.
#  This assumes that data is split into a list
#  Each cell of the list is a string seperated by commas
def process_list(raw_data):
    employee_list = {}
    for line in raw_data:
        person = line.split(',')
        employee = Person()
        employee.last_name = process_name(person[0])
        employee.first_name = process_name(person[1])
        employee.middle_initial = process_middle(person[2])
        employee.id = process_id(person[3])
        employee.phone = process_phone(person[4])
        employee_list[employee.id] = employee
    return employee_list