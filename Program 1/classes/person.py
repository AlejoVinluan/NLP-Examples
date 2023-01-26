class Person:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.middle_initial = ''
        self.id = ''
        self.phone = ''
        
    def display(self):
        print('\nEmployee id: ', self.id)
        print('\t', self.first_name, self.middle_initial, self.last_name)
        print('\t', self.phone)