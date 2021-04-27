from src.models.Contact import Contact
import json

class ContactRepository:

    def __init__(self):
        pass


    def fetchAllContacts(self):   
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file)
        
            return data


    def findByPhone(self, desiredPhone):   
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file)
        
            desiredPerson = None
            for person in data:
                if person['phone'] == desiredPhone:
                    return person

        return


    def saveContact(self,contact):
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file)
            data.append(contact)

        with open("src/data/contacts.json", "w") as file:
            dataString = json.dumps(data, indent = 4) 
            file.write(dataString)


    def updateContact(self, updatedContact): 
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file)
    
        lenght = len(data)
        for i in range(lenght):
            if data[i]['phone'] == updatedContact.phone:
                data[i] = updatedContact.getContact()

        with open("src/data/contacts.json", "w") as file:
            dataString = json.dumps(data, indent = 4) 
            file.write(dataString)


    def deleteContact(self,contactPhone): 
        with open("src/data/contacts.json", "r") as file:
            data = json.load(file)
    
        lenght = len(data)
        for i in range(lenght):
            if data[i]['phone'] == contactPhone:
                data.pop(i)

        with open("src/data/contacts.json", "w") as file:
            dataString = json.dumps(data, indent = 4) 
            file.write(dataString)