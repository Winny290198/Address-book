import pickle
import os
from collections import OrderedDict 
import operator

UI = '''
1. Add a contact
2. Delete a contact
3. Display a single entry
4. Display all entries sorted by Last and First Name
5. Display all entries sorted by City, State, Zip
6. Display all entries sorted by Email
7. Quit
'''


class Person(object):

    def __init__(self, firstName=None, lastName=None, streetAddress=None, city=None, state=None,
                 zip=None, phone=None, email=None):
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email


def __str__(self):
    return "{} {:>14} {:>16} {:>15} {:>12} {:>15} {:>9} {:>20}".format(self.firstName, self.lastName, self.streetAddress,
                                     self.city, self.state, self.zip, self.phone, self.email)





class Application(object):

    def __init__(self, database):
        self.database = database
        self.persons=[]
        if not os.path.exists(self.database):
            file_pointer = open(self.database, 'wb')
            pickle.dump({}, file_pointer)
            file_pointer.close()
        else:
            with open(self.database, 'rb') as person_list:
                self.persons = pickle.load(person_list)

    def add(self):
        firstName, lastName, streetAddress, city, state, zip, phone, email = self.getdetails()
        if firstName not in self.persons:
            firstName=Person(firstName, lastName, streetAddress, city, state, zip, phone, email)
            self.persons.append(firstName)
        else:
            print("Contact already present.")

    def viewall(self):
        if self.persons:
            print("{} {:>13} {:>13} {:>13} {:>13} {:>13} {:>18} {:>13}".format('First name', 'Last name', 'Street', 'City', 'State', 'Zip',
                                            'Phone number', 'Email'))
            for person in self.persons:
                print(__str__(person))
        else:
            print("No contacts in database.")

    def sortName(self, lastName=None):
        self.persons = OrderedDict(sorted(self.persons.items())) 
        for person in self.persons.values():
            print(__str__(person))
    
    def sortLastName(self):
        print(self.persons)
        sorted_lastName = sorted(self.persons, key=lambda e:e.lastName)
        for person in sorted_lastName:
            print(__str__(person))
            
    def sortCity(self, city=None):
        print(self.persons)
        sorted_city = sorted(self.persons, key=lambda e:e.city)
        for person in sorted_city:
            print(__str__(person))

    def sortEmail(self, email=None):
        print(self.persons)
        sorted_email = sorted(self.persons, key=lambda e:e.email)
        for person in sorted_email:
            print(__str__(person))

    def getdetails(self):
        firstName = input("First name: ")
        lastName = input("Last name: ")
        streetAddress = input("Street address: ")
        city = input("City: ")
        state = input("State: ")
        zip = input("Zip code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        return firstName, lastName, streetAddress, city, state, zip, phone, email

    def delete(self):
        name = input("Enter the name to delete: ")
        if name in self.persons:
            del self.persons[name]
            print("Deleted the contact.")
        else:
            print("Contact not found in the app.")

    def __del__(self):
        with open(self.database, 'wb') as db:
            pickle.dump(self.persons, db)

    def __str__(self):
        return UI


def main():
    app = Application('contacts.data')
    choice = ''
    while choice != '7':
        print(app)
        choice = input('Choose: ')
        if choice == '1':
            app.add()
        elif choice == '2':
            app.delete()
        elif choice == '3':
            app.viewall()
        elif choice == '4':
            app.sortLastName()
        elif choice == '5':
            app.sortCity()
        elif choice == '6':
            app.sortEmail()
        elif choice == '7':
            print("Quit.")
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()