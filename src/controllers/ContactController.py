from src.models.Contact import Contact
from src.models.ContactRepository import ContactRepository
import json 
class ContactController:
    Repository = ContactRepository()

    def __init__(self):
        pass


    def index(self):
        return 'HTTP/1.1 200 OK', '/contacts.html'

    #getAllContacts returns the data that must be displayed on the index
    def getContacts(self, search):
        if (search == ''):
            contactRepository = self.Repository.fetchAllContacts()
            contactString = ''
            for contact in contactRepository:
                string = f''' 
                <pre>Name: {contact['name']}
                Phone: {contact['phone']}
                Address: {contact['address']}</pre>
                <a href="/updateContact?phone={contact['phone']}">Update</a>
                <a href="/deleteContact?phone={contact['phone']}">Delete</a>
                <br/><br/>
                '''

                contactString = contactString + string
                contactString = contactString.replace('+', ' ')
            return 'HTTP/1.1 200 OK', contactString

        
        else:
            contact = self.Repository.findByPhone(search)
            print(contact)
            if contact == '' or contact == None:
                return 'HTTP/1.1 200 OK', 'Contact not found'
            contactString = f''' 
                <pre>Name: {contact['name']}
                Phone: {contact['phone']}
                Address: {contact['address']}</pre>
                <a href="/updateContact?phone={contact['phone']}">Update</a>
                <a href="/deleteContact?phone={contact['phone']}">Delete</a>
                <br/><br/>
                '''
            contactString = contactString.replace('+', ' ')
            return 'HTTP/1.1 200 OK', contactString

    
    def showSearchPage(self):
        return 'HTTP/1.1 200 OK', '/contactSearch.html'

    def showCreatePage(self):
        return 'HTTP/1.1 200 OK', '/contactCreation.html'

    def create(self,name, address, phone):
        contact = Contact(name, address, phone)

        if self.Repository.findByPhone(contact.phone) != None:
            self.error()
        
        self.Repository.saveContact(contact)
        _, page = self.index()
        return 'HTTP/1.1 201 CREATED', page


    
    def showUpdatePage(self): 
        return 'HTTP/1.1 200 OK', '/contactUpdate.html'

    def update(self,name, address, phone, pastPhone):
        contact = Contact(name, address, phone)

        if self.Repository.findByPhone(pastPhone) == None:
            self.error()

        self.Repository.updateContact(contact, pastPhone)
        _, page = self.index()
        return 'HTTP/1.1 200 OK', page

    def showDeletionPage(self):
        return 'HTTP/1.1 200 OK', '/contactDeletion.html'

    def delete(self,phone):
        if self.Repository.findByPhone(phone) == None:
            return 'HTTP/1.1 404 NOT FOUND', '/error.html'

        self.Repository.deleteContact(phone)
        return 'HTTP/1.1 200 OK', '/contacts.html'


    def error(self):
        return 'HTTP/1.1 404 NOT FOUND', '/error.html'

