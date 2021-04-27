from src.models.Contact import Contact
from src.models.ContactRepository import ContactRepository
import json 
class ContactController:
    Repository = ContactRepository()

    def __init__(self):
        pass


    def index(self):
        contactRepository = self.Repository.fetchAllContacts()
        return contactRepository, 'HTTP/1.1 200 OK', '/contacts.html'


    def show(self,phone):
        contact = self.Repository.findByPhone(phone)

        if contact == None:
            return "Contact not found", 'HTTP/1.1 404 NOT FOUND', '/error.html'

        return contact, 'HTTP/1.1 200 OK', '/contact.html'


    def create(self,name, address, phone):
        contact = Contact(name, address, phone)

        if self.Repository.findByPhone(contact.getPhone()) != None:
            return 'HTTP/1.1 400 BAD REQUEST', '/error.html'
        
        self.Repository.saveContact(contact)
        return 'HTTP/1.1 201 CREATED', '/contact.html'


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

