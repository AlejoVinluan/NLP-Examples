import re

# Capitalizes the first character and lower cases the remaining string
def process_name(name):
    processed_name = name.capitalize()
    return processed_name

# Isolates the first character of the middle initial and makes it uppercase
#  If there is no middle character, return 'X'
def process_middle(middle_initial):
    if middle_initial:
        return middle_initial[0].upper()
    else:
        return 'X'
    
# Uses regex to process a personal ID. Checks for proper formatting
#  and asks user for a fixed ID if one is not provided. 
#  Will not proceed until ID matches proper formatting.
def process_id(person_id):
    acceptable_id = re.compile("[A-Za-z]{2}[0-9]{4}")
    while not acceptable_id.match(person_id):
        print('ID invalid: ', person_id)
        print('ID is two letters followed by 4 digits')
        person_id = input('Please enter a valid id: ')
    return person_id

# Uses regex to process a phone number. Checks for proper formatting and
#  asks user for a fixed phone number if one is not provided.
#  Will not proceed until phone number matches proper formatting.
def process_phone(phone_number):
    acceptable_phone = re.compile("[0-9]{3}-[0-9]{3}-[0-9]{4}")
    while not acceptable_phone.match(phone_number):
        print("Phone ", phone_number, " is invalid.")
        print("Enter phone number in form 123-456-7890")
        phone_number = input("Enter phone number: ")
    return phone_number