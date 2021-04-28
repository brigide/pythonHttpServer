from src.models.Contact import Contact
import json

class ContactRepository:

    def __init__(self):
        pass


    def fetchAllContacts(self):   
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file) # Reads the data from the .json
        
            return data


    def findByPhone(self, desiredPhone):   
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file) # Reads the data from the .json
        
            desiredPerson = None
            for person in data:
                if person['phone'] == desiredPhone: # If the person is not found, this will return void
                    return person 

        return


    def saveContact(self,contact):
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file) # Reads the data from the .json
            data.append(contact) # data is a json converted to dict, here the new contact is appended

        with open("src/data/contacts.json", "w") as file:
            dataString = json.dumps(data, indent = 4)  # Format the data string as a JSOn with indent 4
            file.write(dataString)


    def updateContact(self, updatedContact): 
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file) # Reads the data from the .json
    
        lenght = len(data)
        for i in range(lenght): # Search the dict for the desired contact
            if data[i]['phone'] == updatedContact.phone:
                data[i] = updatedContact.getContact()

        with open("src/data/contacts.json", "w") as file:
            dataString = json.dumps(data, indent = 4)  # Format the data string as a JSOn with indent 4
            file.write(dataString)


    def deleteContact(self,contactPhone): 
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file) # Reads the data from the .json
    
        lenght = len(data)
        for i in range(lenght): # Search the dict for the desired contact
            if data[i]['phone'] == contactPhone:
                data.pop(i)

        with open("src/data/contacts.json", "w") as file:
            dataString = json.dumps(data, indent = 4)  # Format the data string as a JSOn with indent 4
            file.write(dataString)