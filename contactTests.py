import sys 

sys.path.append('src')

from src.models.Contact import Contact 
from src.models.ContactRepository import ContactRepository

name = 'John Doe'
address = '221B Baker Street'
phone = '11912345678'

print('Saving Contact...')
mockedContact = Contact(name, address, phone)
print('\n',mockedContact.name, mockedContact.address, mockedContact.phone, '\n')

mockedContact = mockedContact.getContact() #mockedContact is converted to a dictionary
Repository = ContactRepository()

#Saving the contact
Repository.saveContact(mockedContact)

#Checking if the contact now exists
foundContact = Repository.findByPhone(phone)
print('\n\nSearch:\n',foundContact)


input('\nPress ENTER for the next step (Contact Update)')
#Updating the contact
newName = 'Jane Doe'
newAddress = 'Cesame Street'
mockedUpdatedContact= Contact(newName, newAddress, phone)
Repository.updateContact(mockedUpdatedContact)

#Checking if the contact was updated
foundContact = Repository.findByPhone(phone)
print('\n\nUpdated:\n',foundContact)

input('\nPress ENTER for the next step (Contact Deletion)')
#Deleting the contact
foundContact = Repository.deleteContact(phone)
print('\n\nUsers found:\n',foundContact)