import re

def process_name(name):
    processed_name = name.capitalize()
    return processed_name

def process_middle(middle_initial):
    if middle_initial:
        return middle_initial[0].upper()
    else:
        return 'X'
    
def process_id(person_id):
    acceptable_id = re.compile("[A-Za-z]{2}[0-9]{4}")
    while not acceptable_id.match(person_id):
        print('ID invalid: ', person_id)
        print('ID is two letters followed by 4 digits')
        person_id = input('Please enter a valid id: ')
    return person_id

def process_phone(phone_number):
    acceptable_phone = re.compile("[0-9]{3}-[0-9]{3}-[0-9]{4}")
    while not acceptable_phone.match(phone_number):
        print("Phone ", phone_number, " is invalid.")
        print("Enter phone number in form 123-456-7890")
        phone_number = input("Enter phone number: ")
    return phone_number