from src.models.Contact import Contact
from src.models.ContactRepository import ContactRepository
from src.views import contacts as contactTemplate
from src.views import contactCreation as creatContactTemplate
from src.views import error as errorTemplate
import json 
class ContactController:
    Repository = ContactRepository()

    def __init__(self):
        pass


    def index(self):
        #contactRepository returns all contacts from the json
        contactRepository = self.Repository.fetchAllContacts()
        contactString = ''
        for contact in contactRepository:
            string = f''' 
            <pre>Name: {contact['name']}
            Phone: {contact['phone']}
            Address: {contact['address']}</pre>
            <br/>
            '''
            contactString = contactString + string
        #then we send the json data with the http status code and the html string returned by src/views/contacts.py
        return contactRepository, 'HTTP/1.1 200 OK', contactTemplate.displayPage(contactString) 


    def show(self,phone):
        contact = self.Repository.findByPhone(phone)

        if contact == None:
            return "Contact not found", 'HTTP/1.1 404 NOT FOUND', '/error.html'

        return contact, 'HTTP/1.1 200 OK', contactTemplate.displayPage(contact)

    
    def showCreatePage(self):
        return 'HTTP/1.1 200 OK', creatContactTemplate.displayPage()


    def create(self,name, address, phone):
        contact = Contact(name, address, phone)

        if self.Repository.findByPhone(contact.phone) != None:
            self.error()
        
        self.Repository.saveContact(contact)

        contactRepository = self.Repository.fetchAllContacts()
        contactString = ''
        for contact in contactRepository:
            string = f''' 
            <pre>Name: {contact['name']}
            Phone: {contact['phone']}
            Address: {contact['address']}</pre>
            <br/>
            '''
            contactString = contactString + string
        return 'HTTP/1.1 201 CREATED', contactTemplate.displayPage(contactString) 


    def update(self,name, address, phone):
        contact = Contact(name, address, phone)

        if self.Repository.findByPhone(contact.getPhone()) == None:
            return 'HTTP/1.1 404 NOT FOUND', '/error.html'

        self.Repository.updateContact(contact.getPhone(), contact)
        return 'HTTP/1.1 204 No Content', '/contacts.html'


    def delete(self,phone):
        if self.Repository.findByPhone(contact.getPhone()) == None:
            return 'HTTP/1.1 404 NOT FOUND', '/error.html'

        self.Repository.deleteContact(phone)
        return 'HTTP/1.1 200 OK', '/contacts.html'


    def error(self):
        return 'HTTP/1.1 404 NOT FOUND', errorTemplate.displayPage()

